from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
path = ROOT / "favicon.png"
if path.exists():
    img = Image.open(path).convert("RGBA")
    img = img.resize((32, 32), Image.Resampling.LANCZOS)
    img.save(path, "PNG", optimize=True)
    print(f"favicon.png {path.stat().st_size}")
