import csv

with open("audit/06-images.csv", "r", encoding="utf-8-sig") as f:
    for row in csv.DictReader(f):
        issues = row.get("issues", "")
        if "MISSING_ALT" in issues or "MISSING_DIMENSIONS" in issues:
            print(f"PAGE: {row['page']} | SRC: {row['src']} | ISSUES: {issues}")
