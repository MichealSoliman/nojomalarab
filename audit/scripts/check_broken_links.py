import csv

with open("audit/04-links.csv", "r", encoding="utf-8-sig") as f:
    reader = csv.DictReader(f)
    broken = [r for r in reader if r.get("is_broken") == "True"]
    print(f"Total broken link references: {len(broken)}")
    sample_targets = set(r["target_href"] for r in broken)
    print("Sample targets marked broken:")
    for t in list(sample_targets)[:15]:
        print(f" - {t}")
