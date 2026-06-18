from __future__ import annotations

import json
import os
import re
from pathlib import Path
from urllib.parse import unquote

from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "large-image-webp-conversion-report.json"
RASTER_EXTS = {".png", ".jpg", ".jpeg"}
TEXT_EXTS = {".html", ".css", ".js", ".py", ".md", ".json", ".xml", ".txt", ".csv"}
SKIP_NAMES = {
    "favicon.ico",
    "favicon.png",
    "apple-touch-icon.png",
    "parallax_data_lab_original_transparent.png",
}
SKIP_DIR_PARTS = {".git", "__pycache__"}
MIN_BYTES = 150 * 1024


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def text_files() -> list[Path]:
    files: list[Path] = []
    for path in ROOT.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in TEXT_EXTS:
            continue
        if any(part in SKIP_DIR_PARTS for part in path.parts):
            continue
        if path.name in {REPORT.name, "image-reference-inventory.json"}:
            continue
        files.append(path)
    return files


def referenced_paths(files: list[Path]) -> set[Path]:
    refs: set[Path] = set()
    pattern = re.compile(r"""(?P<ref>(?:\.\./|/)?assets/[^"'()\s<>]+\.(?:png|jpe?g))(?:\?[^"'()\s<>]*)?""", re.I)
    for owner in files:
        try:
            text = owner.read_text(encoding="utf-8", errors="ignore")
        except UnicodeDecodeError:
            continue
        for match in pattern.finditer(text):
            value = unquote(match.group("ref")).split("#", 1)[0].split("?", 1)[0]
            if value.startswith("/"):
                candidate = ROOT / value.lstrip("/")
            elif value.startswith("../"):
                candidate = (owner.parent / value).resolve()
            else:
                candidate = ROOT / value
            if candidate.exists() and candidate.suffix.lower() in RASTER_EXTS:
                refs.add(candidate.resolve())
    return refs


def target_width(path: Path, width: int) -> int:
    lower = rel(path).lower()
    if "social" in lower:
        return min(width, 1200)
    if "insights" in lower:
        return min(width, 1200)
    if "hero" in lower or "background" in lower or "skyline" in lower:
        return min(width, 1600)
    if "jonah" in lower:
        return min(width, 900)
    return min(width, 1200)


def quality(path: Path) -> int:
    lower = rel(path).lower()
    if "jonah" in lower or "logo" in lower or "power-bi" in lower:
        return 86
    if "insights" in lower:
        return 82
    if "hero" in lower or "background" in lower:
        return 82
    return 80


def convert(path: Path) -> dict | None:
    if path.name in SKIP_NAMES or path.stat().st_size < MIN_BYTES:
        return None

    img = Image.open(path)
    has_alpha = img.mode in {"RGBA", "LA"} or "transparency" in img.info
    img = img.convert("RGBA" if has_alpha else "RGB")
    original_width, original_height = img.size
    width = target_width(path, original_width)
    if width < original_width:
        height = max(1, round(original_height * (width / original_width)))
        img = img.resize((width, height), Image.Resampling.LANCZOS)
    else:
        height = original_height

    webp = path.with_suffix(".webp")
    img.save(webp, "WEBP", quality=quality(path), method=6)

    return {
        "source": rel(path),
        "source_bytes": path.stat().st_size,
        "source_width": original_width,
        "source_height": original_height,
        "webp": rel(webp),
        "webp_bytes": webp.stat().st_size,
        "webp_width": width,
        "webp_height": height,
        "saved_bytes": path.stat().st_size - webp.stat().st_size,
    }


def replace_refs(files: list[Path], conversions: dict[str, str]) -> list[dict]:
    changes = []
    sorted_pairs = sorted(conversions.items(), key=lambda item: len(item[0]), reverse=True)
    for path in files:
        text = path.read_text(encoding="utf-8", errors="ignore")
        updated = text
        for old, new in sorted_pairs:
            old_name = Path(old).name
            new_name = Path(new).name
            updated = updated.replace(old, new)
            updated = updated.replace("/" + old, "/" + new)
            updated = updated.replace("../" + old, "../" + new)
            updated = updated.replace(old_name, new_name)
        if updated != text:
            path.write_text(updated, encoding="utf-8", newline="\n")
            changes.append({"file": rel(path), "bytes_delta": len(updated) - len(text)})
    return changes


def remove_originals(converted: list[dict]) -> list[str]:
    removed = []
    for item in converted:
        path = ROOT / item["source"]
        if path.exists():
            path.unlink()
            removed.append(item["source"])
    return removed


def main() -> None:
    files = text_files()
    refs = referenced_paths(files)
    converted = []
    for path in sorted(refs):
        result = convert(path)
        if result:
            converted.append(result)

    conversions = {item["source"]: item["webp"] for item in converted}
    changes = replace_refs(files, conversions)
    removed = remove_originals(converted)

    report = {
        "converted_count": len(converted),
        "removed_original_count": len(removed),
        "source_bytes": sum(item["source_bytes"] for item in converted),
        "webp_bytes": sum(item["webp_bytes"] for item in converted),
        "saved_bytes": sum(item["saved_bytes"] for item in converted),
        "converted": converted,
        "updated_files": changes,
        "removed_originals": removed,
    }
    REPORT.write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(json.dumps({
        "converted_count": report["converted_count"],
        "removed_original_count": report["removed_original_count"],
        "source_mb": round(report["source_bytes"] / 1024 / 1024, 2),
        "webp_mb": round(report["webp_bytes"] / 1024 / 1024, 2),
        "saved_mb": round(report["saved_bytes"] / 1024 / 1024, 2),
        "updated_files": len(changes),
        "report": rel(REPORT),
    }, indent=2))


if __name__ == "__main__":
    main()
