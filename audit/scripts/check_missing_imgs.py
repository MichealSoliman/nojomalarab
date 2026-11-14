import csv

with open("audit/06-images.csv", "r", encoding="utf-8-sig") as f:
    reader = csv.DictReader(f)
    missing = [r for r in reader if r.get("exists") == "False"]
    print(f"Total missing image references: {len(missing)}")
    for r in missing[:10]:
        print(f"Page: {r['page']} | Src: {r['src']}")
