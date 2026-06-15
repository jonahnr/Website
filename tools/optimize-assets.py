from pathlib import Path

from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"
MIN_BYTES = 450 * 1024
MAX_DIMENSION = 1400
PALETTE_COLORS = 192


def optimized_copy(image: Image.Image) -> Image.Image:
    image = image.copy()
    image.thumbnail((MAX_DIMENSION, MAX_DIMENSION), Image.Resampling.LANCZOS)

    if image.mode == "RGBA":
        return image.quantize(colors=PALETTE_COLORS, method=Image.Quantize.FASTOCTREE)

    if image.mode not in ("RGB", "P"):
        image = image.convert("RGB")

    return image.convert("P", palette=Image.Palette.ADAPTIVE, colors=PALETTE_COLORS)


def optimize_png(path: Path) -> tuple[int, int, bool]:
    original_size = path.stat().st_size
    if original_size < MIN_BYTES:
        return original_size, original_size, False

    with Image.open(path) as image:
        candidate = optimized_copy(image)
        temp_path = path.with_suffix(path.suffix + ".tmp")
        candidate.save(temp_path, format="PNG", optimize=True)

    new_size = temp_path.stat().st_size
    if new_size < original_size * 0.88:
        temp_path.replace(path)
        return original_size, new_size, True

    temp_path.unlink(missing_ok=True)
    return original_size, original_size, False


def main() -> None:
    before = 0
    after = 0
    changed = []

    for path in sorted(ASSETS.rglob("*.png")):
      original, current, did_change = optimize_png(path)
      before += original
      after += current
      if did_change:
          changed.append((path.relative_to(ROOT), original, current))

    for rel_path, original, current in sorted(changed, key=lambda item: item[1] - item[2], reverse=True):
        saved = (original - current) / 1024
        print(f"{saved:8.1f} KB saved  {rel_path}")

    print(
        f"Optimized {len(changed)} PNG files. "
        f"Total PNG bytes: {before / 1024 / 1024:.2f} MB -> {after / 1024 / 1024:.2f} MB."
    )


if __name__ == "__main__":
    main()
