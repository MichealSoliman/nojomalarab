import os
import re
import csv
import json
from pathlib import Path
from bs4 import BeautifulSoup

def log(msg):
    with open("audit/run-log.txt", "a", encoding="utf-8") as f:
        f.write(f"[SCHEMA-AUDIT] {msg}\n")
    print(msg)

log("Starting schema audit...")

html_files = []
for p in Path(".").rglob("*.html"):
    rel = p.as_posix()
    if rel.startswith("audit/") or ".gemini" in rel:
        continue
    html_files.append(p)

all_schemas = {}
validation_rows = []

# Required/recommended fields by Schema Type
SCHEMA_REQUIREMENTS = {
    "LocalBusiness": ["@type", "name", "telephone", "address"],
    "MovingCompany": ["@type", "name", "telephone", "address"],
    "FAQPage": ["@type", "mainEntity"],
    "BreadcrumbList": ["@type", "itemListElement"],
    "Article": ["@type", "headline", "author", "datePublished"],
    "BlogPosting": ["@type", "headline", "author", "datePublished"],
    "Service": ["@type", "name", "provider"]
}

for fpath in sorted(html_files):
    rel = fpath.as_posix()
    with open(fpath, "r", encoding="utf-8", errors="ignore") as f:
        soup = BeautifulSoup(f.read(), "html.parser")
        
    script_tags = soup.find_all("script", type="application/ld+json")
    all_schemas[rel] = []
    
    for idx, tag in enumerate(script_tags):
        raw_content = tag.string or ""
        # Check for placeholders
        placeholders = re.findall(r"\{\{[^}]+\}\}", raw_content)
        
        try:
            parsed = json.loads(raw_content)
            all_schemas[rel].append(parsed)
            
            # Flatten @graph if present
            nodes = []
            if isinstance(parsed, dict):
                if "@graph" in parsed and isinstance(parsed["@graph"], list):
                    nodes.extend(parsed["@graph"])
                else:
                    nodes.append(parsed)
            elif isinstance(parsed, list):
                nodes.extend(parsed)
                
            for node_idx, node in enumerate(nodes):
                if not isinstance(node, dict):
                    continue
                node_type = str(node.get("@type", "Unknown"))
                node_id = str(node.get("@id", ""))
                
                # Check required fields
                missing_fields = []
                reqs = SCHEMA_REQUIREMENTS.get(node_type, ["@type"])
                for r in reqs:
                    if r not in node:
                        missing_fields.append(r)
                        
                # Check FAQ sync if FAQPage
                faq_mismatch = False
                if node_type == "FAQPage":
                    # extract visible faq questions from html
                    pass
                    
                validation_rows.append({
                    "page": rel,
                    "script_index": idx,
                    "node_index": node_idx,
                    "type": node_type,
                    "id": node_id,
                    "has_placeholders": len(placeholders) > 0,
                    "placeholders": ";".join(placeholders),
                    "missing_recommended_fields": ";".join(missing_fields),
                    "valid_json": True,
                    "error_msg": ""
                })
        except Exception as e:
            validation_rows.append({
                "page": rel,
                "script_index": idx,
                "node_index": -1,
                "type": "PARSE_ERROR",
                "id": "",
                "has_placeholders": len(placeholders) > 0,
                "placeholders": ";".join(placeholders),
                "missing_recommended_fields": "",
                "valid_json": False,
                "error_msg": str(e)
            })

# Save full schema JSON
with open("audit/07-schema.json", "w", encoding="utf-8") as f:
    json.dump(all_schemas, f, ensure_ascii=False, indent=2)

# Save validation CSV
with open("audit/07-schema-validation.csv", "w", encoding="utf-8-sig", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=validation_rows[0].keys())
    writer.writeheader()
    writer.writerows(validation_rows)

log(f"Schema audit finished. {len(validation_rows)} schema nodes validated.")

