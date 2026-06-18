import json
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "image-optimization-report.json"

data = json.loads(REPORT.read_text(encoding="utf-8"))
social = {}
for stem in ["social-preview", "assets/social-preview"]:
    entry = {}
    for ext in ["png", "jpg", "webp"]:
        path = ROOT / f"{stem}.{ext}"
        if path.exists():
            entry[ext] = {
                "bytes": path.stat().st_size,
                "size": list(Image.open(path).size),
                "path": path.relative_to(ROOT).as_posix(),
            }
    social[stem] = entry
data["social_preview_final"] = social
REPORT.write_text(json.dumps(data, indent=2), encoding="utf-8")
print(json.dumps(social, indent=2))
