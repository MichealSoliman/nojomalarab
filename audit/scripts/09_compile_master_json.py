import os
import json
import csv
from pathlib import Path

def log(msg):
    with open("audit/run-log.txt", "a", encoding="utf-8") as f:
        f.write(f"[MASTER-JSON] {msg}\n")
    print(msg)

log("Compiling master audit.json...")

def load_csv(path):
    if not Path(path).exists():
        return []
    with open(path, "r", encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))

inventory = load_csv("audit/01-pages-inventory.csv")
headings = load_csv("audit/03-headings.csv")
links = load_csv("audit/04-links.csv")
images = load_csv("audit/06-images.csv")
schema_val = load_csv("audit/07-schema-validation.csv")
claims = load_csv("audit/08-claims-and-facts.csv")
prices = load_csv("audit/09-prices.csv")
keywords = load_csv("audit/10-keywords-map.csv")
duplicates = load_csv("audit/11-duplicates.csv")
issues = load_csv("audit/13-issues.csv")
indexability = load_csv("audit/15-indexability.csv")

audit_summary = {
    "audit_metadata": {
        "domain": "https://nojomalarab.com",
        "entity_name": "شركة نجوم العرب لنقل الأثاث بجدة",
        "timestamp": "2026-11-10T11:20:00Z",
        "total_pages_inventoried": len(inventory),
        "total_headings": len(headings),
        "total_links": len(links),
        "total_images": len(images),
        "total_issues_identified": len(issues),
        "connectivity_mode": "Local Files + Live Internet (Status 200 Verified)"
    },
    "pages_inventory": inventory,
    "issues": issues,
    "indexability_summary": {
        "indexable_count": sum(1 for r in indexability if r.get("indexability_verdict") == "INDEXABLE"),
        "non_indexable_count": sum(1 for r in indexability if r.get("indexability_verdict") == "NON_INDEXABLE"),
        "risk_count": sum(1 for r in indexability if r.get("indexability_verdict") == "RISK")
    },
    "images_summary": {
        "total": len(images),
        "missing_alt": sum(1 for r in images if "MISSING_ALT" in r.get("issues", "")),
        "missing_dimensions": sum(1 for r in images if "MISSING_DIMENSIONS" in r.get("issues", "")),
        "missing_404": sum(1 for r in images if "FILE_NOT_FOUND_404" in r.get("issues", ""))
    },
    "links_summary": {
        "total": len(links),
        "broken_internal": sum(1 for r in links if r.get("is_broken") == "True")
    }
}

with open("audit/audit.json", "w", encoding="utf-8") as f:
    json.dump(audit_summary, f, ensure_ascii=False, indent=2)

log("Master audit.json compiled successfully.")

