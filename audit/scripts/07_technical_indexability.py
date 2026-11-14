import os
import re
import csv
from pathlib import Path
from bs4 import BeautifulSoup

def log(msg):
    with open("audit/run-log.txt", "a", encoding="utf-8") as f:
        f.write(f"[TECH-INDEX] {msg}\n")
    print(msg)

log("Starting technical and indexability audit...")

# Load inventory
inventory = []
with open("audit/01-pages-inventory.csv", "r", encoding="utf-8-sig") as f:
    reader = csv.DictReader(f)
    for r in reader:
        inventory.append(r)

# Load duplicate critical pairs to check duplicate penalty risk
critical_dupes = set()
with open("audit/11-duplicates.csv", "r", encoding="utf-8-sig") as f:
    reader = csv.DictReader(f)
    for r in reader:
        if r.get("severity") == "CRITICAL":
            critical_dupes.add(r["page_a"])
            critical_dupes.add(r["page_b"])

indexability_rows = []

for row in inventory:
    url_path = row["url_path"]
    full_url = row["full_url"]
    file_rel = row["file"]
    group = row["group"]
    
    # Factors
    status_200 = True # local exists
    if file_rel == "404.html":
        status_200 = False
        
    robots_meta = row["robots_meta"].lower()
    is_noindex = "noindex" in robots_meta
    
    # Robots.txt rule
    # Our robots.txt: Allow: /
    blocked_by_robots_txt = False
    
    canonical_self = row["canonical_match"] == "True"
    in_sitemap = row["in_sitemap"] == "True"
    
    # Word count check
    wc = int(row["word_count"])
    is_thin = wc < 250 and group not in ["legal", "error"]
    
    # Duplication check
    is_high_duplicate = file_rel in critical_dupes
    
    # Indexability Verdict
    verdict = "INDEXABLE"
    reasons = []
    
    if file_rel == "404.html":
        verdict = "NON_INDEXABLE"
        reasons.append("404 Error Template")
    elif is_noindex:
        verdict = "NON_INDEXABLE"
        reasons.append("Meta robots noindex")
    elif not canonical_self:
        verdict = "RISK"
        reasons.append("Canonical mismatch or cross-domain")
    
    if not in_sitemap and verdict == "INDEXABLE":
        reasons.append("Missing from sitemap.xml")
    if is_thin:
        reasons.append("Thin content (<250 words)")
    if is_high_duplicate:
        reasons.append("High duplicate content risk (Cosine similarity > 75%)")
        
    indexability_rows.append({
        "url_path": url_path,
        "full_url": full_url,
        "file": file_rel,
        "group": group,
        "indexability_verdict": verdict,
        "status_code": 404 if file_rel == "404.html" else 200,
        "in_robots_txt_allowed": not blocked_by_robots_txt,
        "in_sitemap": in_sitemap,
        "has_canonical": bool(row["canonical"]),
        "canonical_self": canonical_self,
        "word_count": wc,
        "flags_and_risks": "; ".join(reasons) if reasons else "None"
    })

with open("audit/15-indexability.csv", "w", encoding="utf-8-sig", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=indexability_rows[0].keys())
    writer.writeheader()
    writer.writerows(indexability_rows)

log(f"Indexability audit written ({len(indexability_rows)} records)")

