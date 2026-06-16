import json

with open("image-optimization-report.json", "r", encoding="utf-8") as f:
    data = json.load(f)

optimized = data["optimized"]
before = sum(item["source_bytes"] for item in optimized)
after = sum((item["webp_bytes"] or 0) for item in optimized)
variants = sum(len(item["variants"]) for item in optimized)

print(f"optimized={len(optimized)}")
print(f"responsive_variants={variants}")
print(f"referenced_original_bytes={before}")
print(f"webp_primary_bytes={after}")
print(f"estimated_primary_savings={before - after}")
print("social_preview=" + json.dumps(data["social_preview"], sort_keys=True))
print("largest_savings:")
for item in sorted(optimized, key=lambda x: x["source_bytes"] - (x["webp_bytes"] or x["source_bytes"]), reverse=True)[:20]:
    saved = item["source_bytes"] - (item["webp_bytes"] or item["source_bytes"])
    print(f"- {item['source']} {item['source_bytes']} -> {item['webp_bytes']} saved={saved}")
