from __future__ import annotations

from dataclasses import dataclass, asdict
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote
import json
import os
import re

from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "image-optimization-report.json"
RASTER_EXTS = {".png", ".jpg", ".jpeg"}
SKIP_NAMES = {
    "favicon.ico",
    "favicon.png",
    "apple-touch-icon.png",
}
RESPONSIVE_WIDTHS = [480, 768, 1200, 1600]


@dataclass
class ImageOutput:
    source: str
    width: int
    height: int
    source_bytes: int
    webp: str | None
    webp_bytes: int | None
    variants: list[dict]


class ImgParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.imgs: list[tuple[str, dict[str, str]]] = []

    def handle_starttag(self, tag, attrs):
        if tag.lower() == "img":
            self.imgs.append((self.get_starttag_text(), dict(attrs)))


def is_external(value: str) -> bool:
    return value.startswith(("http://", "https://", "data:", "//", "mailto:", "tel:", "#"))


def split_ref(value: str) -> str:
    return unquote(value.split("#", 1)[0].split("?", 1)[0])


def resolve_ref(owner: Path, value: str) -> Path | None:
    if not value or is_external(value):
        return None
    ref = split_ref(value)
    if not ref:
        return None
    if ref.startswith("/"):
        return (ROOT / ref.lstrip("/")).resolve()
    return (owner.parent / ref).resolve()


def rel_from_owner(owner: Path, target: Path) -> str:
    return Path(os.path.relpath(Path(target).resolve(), owner.parent.resolve())).as_posix()


def referenced_rasters() -> set[Path]:
    refs: set[Path] = set()
    for owner in list(ROOT.rglob("*.html")) + list(ROOT.rglob("*.css")) + list(ROOT.rglob("*.js")):
        if ".git" in owner.parts:
            continue
        text = owner.read_text(encoding="utf-8", errors="ignore")
        candidates = re.findall(r'["\']([^"\']+\.(?:png|jpg|jpeg)(?:\?[^"\']*)?)["\']', text, flags=re.I)
        candidates += re.findall(r"url\((?:'|\")?([^'\"\)]+\.(?:png|jpg|jpeg)(?:\?[^'\"\)]*)?)(?:'|\")?\)", text, flags=re.I)
        for cand in candidates:
            path = resolve_ref(owner, cand)
            if path and path.exists() and path.suffix.lower() in RASTER_EXTS and path.name not in SKIP_NAMES:
                refs.add(path)
    # Metadata social image may be absolute but maps to the local file.
    for p in [ROOT / "social-preview.webp", ROOT / "assets" / "social-preview.webp"]:
        if p.exists():
            refs.add(p)
    return refs


def quality_for(path: Path) -> int:
    s = path.as_posix().lower()
    if "social-preview" in s:
        return 82
    if "insights" in s:
        return 82
    if "hero" in s or "background" in s or "home-generated" in s:
        return 80
    if "logo" in s or "parallax_data_lab" in s or "jonah" in s:
        return 88
    return 84


def load_image(path: Path) -> Image.Image:
    img = Image.open(path)
    # Keep alpha where present; otherwise use RGB for smaller WebP.
    if img.mode in ("RGBA", "LA") or ("transparency" in img.info):
        return img.convert("RGBA")
    return img.convert("RGB")


def save_webp(img: Image.Image, path: Path, quality: int) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    img.save(path, "WEBP", quality=quality, method=6)


def optimize_one(path: Path) -> ImageOutput | None:
    if path.name in SKIP_NAMES:
        return None
    img = load_image(path)
    w, h = img.size
    source_bytes = path.stat().st_size

    webp = path.with_suffix(".webp")
    save_webp(img, webp, quality_for(path))

    variants = []
    for width in RESPONSIVE_WIDTHS:
        if width >= w:
            continue
        ratio = width / w
        height = max(1, round(h * ratio))
        resized = img.resize((width, height), Image.Resampling.LANCZOS)
        variant = path.with_name(f"{path.stem}-{width}.webp")
        save_webp(resized, variant, quality_for(path))
        variants.append({
            "path": variant.relative_to(ROOT).as_posix(),
            "width": width,
            "height": height,
            "bytes": variant.stat().st_size,
        })

    return ImageOutput(
        source=path.relative_to(ROOT).as_posix(),
        width=w,
        height=h,
        source_bytes=source_bytes,
        webp=webp.relative_to(ROOT).as_posix(),
        webp_bytes=webp.stat().st_size,
        variants=variants,
    )


def add_img_attrs(html_path: Path) -> None:
    text = html_path.read_text(encoding="utf-8")

    def repl(match: re.Match) -> str:
        tag = match.group(0)
        if " srcset=" in tag or "<img" not in tag:
            return tag
        src_m = re.search(r'\bsrc=(["\'])([^"\']+)\1', tag)
        if not src_m:
            return tag
        src = src_m.group(2)
        path = resolve_ref(html_path, src)
        if not path or not path.exists() or path.suffix.lower() not in RASTER_EXTS or path.name in SKIP_NAMES:
            return tag
        webp = path.with_suffix(".webp")
        if not webp.exists():
            return tag
        variants = []
        for width in RESPONSIVE_WIDTHS:
            variant = path.with_name(f"{path.stem}-{width}.webp")
            if variant.exists():
                variants.append(f"{rel_from_owner(html_path, variant)} {width}w")
        variants.append(f"{rel_from_owner(html_path, webp)} {Image.open(path).size[0]}w")
        srcset = ", ".join(variants)
        sizes = "(max-width: 640px) 92vw, (max-width: 1100px) 46vw, 560px"
        insert = f' srcset="{srcset}" sizes="{sizes}"'
        tag = tag[:-1] + insert + ">"
        if 'loading=' not in tag and not any(cls in tag for cls in ["hero-logo", "site-brand"]):
            tag = tag[:-1] + ' loading="lazy">'
        if 'decoding=' not in tag:
            tag = tag[:-1] + ' decoding="async">'
        return tag

    text = re.sub(r"<img\b[^>]*>", repl, text)
    html_path.write_text(text, encoding="utf-8", newline="\n")


def update_css_images(css_path: Path) -> None:
    text = css_path.read_text(encoding="utf-8")

    def repl(match: re.Match) -> str:
        quote = match.group(1) or ""
        value = match.group(2)
        if value.lower().endswith(".webp") or is_external(value):
            return match.group(0)
        path = resolve_ref(css_path, value)
        if not path or not path.exists() or path.suffix.lower() not in RASTER_EXTS or path.name in SKIP_NAMES:
            return match.group(0)
        webp = path.with_suffix(".webp")
        if not webp.exists():
            return match.group(0)
        webp_ref = rel_from_owner(css_path, webp)
        original_ref = value
        return f'image-set(url("{webp_ref}") type("image/webp"), url("{original_ref}") type("image/{path.suffix.lower().lstrip(".").replace("jpg", "jpeg")}") )'

    # Only replace url(...) values; the previous background declaration remains compatible in browsers
    # that do not support image-set because the replacement includes the original as fallback candidate.
    text = re.sub(r"url\((?:('|\")?)([^'\"\)]+\.(?:png|jpg|jpeg))(?:'|\")?\)", repl, text, flags=re.I)
    css_path.write_text(text, encoding="utf-8", newline="\n")


def update_social_preview() -> dict:
    # Ensure both social preview files are 1200x630 and below the original size; keep PNG metadata references stable.
    changed = {}
    for path in [ROOT / "social-preview.webp", ROOT / "assets" / "social-preview.webp"]:
        if not path.exists():
            continue
        img = load_image(path)
        if img.size != (1200, 630):
            img = img.resize((1200, 630), Image.Resampling.LANCZOS)
            img.save(path, "PNG", optimize=True)
        webp = path.with_suffix(".webp")
        save_webp(img, webp, 82)
        changed[path.relative_to(ROOT).as_posix()] = {
            "png_bytes": path.stat().st_size,
            "webp": webp.relative_to(ROOT).as_posix(),
            "webp_bytes": webp.stat().st_size,
            "size": img.size,
        }
    return changed


def main() -> None:
    refs = referenced_rasters()
    outputs = []
    for path in sorted(refs):
        result = optimize_one(path)
        if result:
            outputs.append(asdict(result))

    for html in ROOT.rglob("*.html"):
        if ".git" not in html.parts:
            add_img_attrs(html)
    for css in ROOT.rglob("*.css"):
        if ".git" not in css.parts:
            update_css_images(css)

    social = update_social_preview()
    REPORT.write_text(json.dumps({"optimized": outputs, "social_preview": social}, indent=2), encoding="utf-8")
    print(f"optimized_images={len(outputs)}")
    print(f"report={REPORT.relative_to(ROOT).as_posix()}")


if __name__ == "__main__":
    main()
