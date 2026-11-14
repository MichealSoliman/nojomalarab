import os
import re
import csv
from pathlib import Path
from bs4 import BeautifulSoup
from urllib.parse import urlparse

def log(msg):
    with open("audit/run-log.txt", "a", encoding="utf-8") as f:
        f.write(f"[LINKS-AUDIT] {msg}\n")
    print(msg)

log("Starting links audit...")

html_files = []
for p in Path(".").rglob("*.html"):
    rel = p.as_posix()
    if rel.startswith("audit/") or ".gemini" in rel:
        continue
    html_files.append(p)

# Mapping of file to clean path
def get_clean_path(rel):
    p = rel.replace("\\", "/")
    if p == "index.html": return "/"
    if p == "404.html": return "/404.html"
    if p.endswith("/index.html"): return "/" + p[:-10] + "/"
    if p.endswith(".html"): return "/" + p[:-5] + "/"
    return "/" + p

all_links = []
page_out_links = {get_clean_path(f.as_posix()): set() for f in html_files}
page_in_links = {get_clean_path(f.as_posix()): set() for f in html_files}

# Known existing local paths
valid_local_paths = set(page_out_links.keys())

for fpath in sorted(html_files):
    source_path = get_clean_path(fpath.as_posix())
    with open(fpath, "r", encoding="utf-8", errors="ignore") as f:
        soup = BeautifulSoup(f.read(), "html.parser")
        
    for a in soup.find_all("a", href=True):
        href = a["href"].strip()
        anchor_text = re.sub(r"\s+", " ", a.get_text()).strip()
        rel_attr = a.get("rel", "")
        if isinstance(rel_attr, list):
            rel_attr = " ".join(rel_attr)
        target_attr = a.get("target", "")
        
        # Categorize href
        link_type = "unknown"
        target_clean = href
        is_broken = False
        
        if href.startswith("tel:"):
            link_type = "tel"
        elif href.startswith("mailto:"):
            link_type = "mailto"
        elif href.startswith("https://wa.me") or "whatsapp.com" in href:
            link_type = "whatsapp"
        elif href.startswith("#"):
            link_type = "anchor_jump"
        elif href.startswith("http://") or href.startswith("https://"):
            parsed = urlparse(href)
            if "nojomalarab.com" in parsed.netloc:
                link_type = "internal"
                target_clean = parsed.path
                if not target_clean.endswith("/") and not target_clean.endswith(".html") and not target_clean.endswith(".xml"):
                    target_clean += "/"
                if target_clean == "": target_clean = "/"
            else:
                link_type = "external"
        else:
            link_type = "internal"
            # Normalize relative paths
            if href.startswith("/"):
                target_clean = href
            else:
                # relative to source
                target_clean = "/" + href
            if not target_clean.endswith("/") and not target_clean.endswith(".html") and not target_clean.endswith(".xml") and "#" not in target_clean:
                target_clean += "/"

        # Check internal target validity
        if link_type == "internal":
            base_target = target_clean.split("#")[0].split("?")[0]
            if base_target not in valid_local_paths and base_target != "/sitemap.xml":
                is_broken = True
            else:
                page_out_links[source_path].add(base_target)
                if base_target in page_in_links:
                    page_in_links[base_target].add(source_path)

        all_links.append({
            "source_file": fpath.as_posix(),
            "source_path": source_path,
            "target_href": href,
            "target_clean": target_clean,
            "link_type": link_type,
            "anchor_text": anchor_text,
            "rel": rel_attr,
            "target": target_attr,
            "is_broken": is_broken
        })

# Write 04-links.csv
with open("audit/04-links.csv", "w", encoding="utf-8-sig", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=all_links[0].keys())
    writer.writeheader()
    writer.writerows(all_links)

log(f"Written 04-links.csv ({len(all_links)} total link instances)")

# Calculate Breadth-First-Search (BFS) click depth from home "/"
depth_map = {p: -1 for p in valid_local_paths}
depth_map["/"] = 0
queue = ["/"]

while queue:
    curr = queue.pop(0)
    curr_depth = depth_map[curr]
    for neighbor in page_out_links.get(curr, []):
        if neighbor in depth_map and depth_map[neighbor] == -1:
            depth_map[neighbor] = curr_depth + 1
            queue.append(neighbor)

# Write 05-link-graph.md
with open("audit/05-link-graph.md", "w", encoding="utf-8") as f:
    f.write("# Internal Link Graph & Architecture Analysis\n\n")
    f.write("## 1. Summary Statistics\n")
    f.write(f"- Total Local Pages Monitored: {len(valid_local_paths)}\n")
    f.write(f"- Total Link Instances Found: {len(all_links)}\n")
    
    broken_count = sum(1 for l in all_links if l["is_broken"])
    f.write(f"- Broken Internal Links Detected: {broken_count}\n\n")
    
    f.write("## 2. Inbound / Outbound Link Density & Click Depth\n\n")
    f.write("| Page Path | Inbound Internal Links | Outbound Unique Links | Click Depth from / | Orphan Risk (<3 inbound) |\n")
    f.write("| :--- | :--- | :--- | :--- | :--- |\n")
    
    orphan_pages = []
    deep_pages = []
    
    for path in sorted(valid_local_paths):
        in_c = len(page_in_links.get(path, set()))
        out_c = len(page_out_links.get(path, set()))
        depth = depth_map.get(path, -1)
        is_orphan = "YES (Warning)" if in_c < 3 else "No"
        if in_c < 3:
            orphan_pages.append(path)
        if depth > 3 or depth == -1:
            deep_pages.append((path, depth))
        f.write(f"| `{path}` | {in_c} | {out_c} | {depth} | {is_orphan} |\n")
        
    f.write("\n## 3. Orphan Pages & Deep Pages\n")
    f.write(f"### Orphan Pages (< 3 inbound internal links): {len(orphan_pages)}\n")
    for op in orphan_pages:
        f.write(f"- `{op}` (Inbound count: {len(page_in_links.get(op, set()))})\n")
        
    f.write(f"\n### Deep Pages (Depth > 3 or Unreachable): {len(deep_pages)}\n")
    for dp, d in deep_pages:
        f.write(f"- `{dp}` (Depth: {d})\n")

log("Link graph analysis complete.")

