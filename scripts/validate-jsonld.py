import os
import json
import re
from pathlib import Path
from bs4 import BeautifulSoup

print("=== Starting Schema JSON-LD Validation ===")

html_files = [p for p in Path('.').rglob('*.html') if not str(p).startswith('audit') and '.gemini' not in str(p) and 'node_modules' not in p.as_posix()]
errors = []
total_nodes = 0

for p in sorted(html_files):
    rel = p.as_posix()
    content = p.read_text(encoding='utf-8')
    soup = BeautifulSoup(content, 'html.parser')
    
    scripts = soup.find_all('script', type='application/ld+json')
    for idx, s in enumerate(scripts):
        raw = s.string or ""
        if not raw.strip():
            continue
            
        # 1. Check for {{ in raw (or unmatched placeholder)
        if re.search(r"\{\{[^}]*\}\}", raw) or "{{" in raw:
            errors.append(f"{rel}: script #{idx+1} contains placeholder {{...}}")
            
        # 2. Check JSON validity
        try:
            data = json.loads(raw)
            # check empty string values recursively
            def check_empty(node, path=""):
                if isinstance(node, dict):
                    for k, v in node.items():
                        if v == "":
                            errors.append(f"{rel}: empty string at {path}.{k}")
                        elif v is None:
                            errors.append(f"{rel}: null value at {path}.{k}")
                        else:
                            check_empty(v, f"{path}.{k}")
                elif isinstance(node, list):
                    for i, item in enumerate(node):
                        check_empty(item, f"{path}[{i}]")
                        
            check_empty(data)
            total_nodes += 1
            
            # Specific rule for homepage: no BreadcrumbList
            if rel == "index.html":
                nodes = data.get("@graph", [data]) if isinstance(data, dict) else data
                for n in nodes:
                    if isinstance(n, dict):
                        if n.get("@type") == "BreadcrumbList":
                            errors.append(f"index.html: forbidden BreadcrumbList on homepage")
                        if n.get("@type") in ["AggregateRating", "Review"]:
                            errors.append(f"index.html: forbidden Review/AggregateRating without reviews")
                            
        except Exception as ex:
            errors.append(f"{rel}: script #{idx+1} JSON.loads error: {ex}")

print(f"Validated {total_nodes} JSON-LD blocks across {len(html_files)} files.")
print(f"Total Errors: {len(errors)}")
for e in errors:
    print(f"  ERROR: {e}")

if len(errors) == 0:
    print("ALL JSON-LD SCHEMAS OK!")
