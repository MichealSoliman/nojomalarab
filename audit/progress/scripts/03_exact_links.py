import os
import re
import csv
from pathlib import Path
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin

def log(msg):
    line = f"[CLEAN_LINKS] {msg}"
    print(line)
    with open("audit/progress/run-log.txt", "a", encoding="utf-8") as f:
        f.write(line + "\n")

log("Starting corrected canonical path link audit...")

def get_canonical_path(file_path):
    p = file_path.as_posix()
    if p == "index.html":
        return "/"
    elif p == "404.html":
        return "/404.html"
    elif p.endswith("/index.html"):
        return "/" + p[:-11] + "/"
    elif p.endswith(".html"):
        return "/" + p[:-5] + "/"
    return "/" + p

all_files = [p for p in Path(".").rglob("*.html") if not str(p).startswith("audit") and ".gemini" not in str(p)]
publishable_files = [p for p in all_files if "node_modules" not in p.as_posix() and "components/" not in p.as_posix()]

valid_paths = set(get_canonical_path(p) for p in publishable_files)
valid_paths.add("/sitemap.xml")

log(f"Normalized valid canonical paths ({len(valid_paths)} routes):")
for vp in sorted(valid_paths)[:15]:
    log(f"  {vp}")

all_links = []
broken_links = []

for p in sorted(publishable_files):
    rel = p.as_posix()
    c_path = get_canonical_path(p)
    base_url = f"https://nojomalarab.com{c_path}"
    
    soup = BeautifulSoup(p.read_text(encoding="utf-8", errors="ignore"), "html.parser")
    
    for a in soup.find_all("a", href=True):
        href = a["href"].strip()
        anchor = re.sub(r"\s+", " ", a.get_text()).strip()
        rel_attr = a.get("rel", "")
        if isinstance(rel_attr, list): rel_attr = " ".join(rel_attr)
        
        link_type = "unknown"
        target_path = href
        is_broken = False
        
        if href.startswith("tel:"):
            link_type = "tel"
        elif href.startswith("mailto:"):
            link_type = "mailto"
        elif "wa.me" in href or "whatsapp" in href:
            link_type = "whatsapp"
        elif href.startswith("#"):
            link_type = "anchor_jump"
        else:
            full = urljoin(base_url, href)
            parsed = urlparse(full)
            if "nojomalarab.com" in parsed.netloc or not parsed.netloc:
                link_type = "internal"
                target_path = parsed.path
                if not target_path.endswith("/") and not target_path.endswith(".html") and not target_path.endswith(".xml"):
                    target_path += "/"
                if target_path == "": target_path = "/"
                
                target_canon = target_path
                if target_path.endswith(".html") and target_path != "/404.html":
                    target_canon = target_path[:-5] + "/"
                    
                if target_path not in valid_paths and target_canon not in valid_paths:
                    is_broken = True
                    broken_links.append((rel, href, target_path, anchor))
            else:
                link_type = "external"
                
        all_links.append({
            "source_file": rel,
            "source_path": c_path,
            "href": href,
            "target_path": target_path,
            "link_type": link_type,
            "anchor": anchor,
            "rel": rel_attr,
            "is_broken": is_broken
        })

log(f"Total links evaluated: {len(all_links)}")
log(f"Internal links: {sum(1 for l in all_links if l['link_type'] == 'internal')}")
log(f"ACTUAL broken internal links: {len(broken_links)}")

if broken_links:
    log("Detailed list of broken links:")
    for b in broken_links:
        log(f"  Page: {b[0]} | href='{b[1]}' (resolved: {b[2]}) | anchor='{b[3]}'")

# Save exact links CSV
with open("audit/progress/02-exact-links.csv", "w", encoding="utf-8-sig", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=all_links[0].keys())
    writer.writeheader()
    writer.writerows(all_links)

log("Written corrected audit/progress/02-exact-links.csv")
