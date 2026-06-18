from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]

for path in [ROOT / "social-preview.webp", ROOT / "assets" / "social-preview.webp"]:
    if not path.exists():
        continue
    img = Image.open(path).convert("RGB")
    if img.size != (1200, 630):
        img = img.resize((1200, 630), Image.Resampling.LANCZOS)
    # Social previews are graphic/illustrative, so a carefully dithered palette
    # usually keeps the card sharp while cutting PNG size dramatically.
    pal = img.quantize(colors=192, method=Image.Quantize.MEDIANCUT, dither=Image.Dither.FLOYDSTEINBERG)
    pal.save(path, "PNG", optimize=True)
    print(f"{path.relative_to(ROOT).as_posix()} {path.stat().st_size}")
