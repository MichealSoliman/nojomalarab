import os
import sys
import glob
import re
import csv
import json
import time
from pathlib import Path
from bs4 import BeautifulSoup

def log(msg):
    line = f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] {msg}"
    print(line)
    with open("audit/run-log.txt", "a", encoding="utf-8") as f:
        f.write(line + "\n")

log("Starting 01_discover_and_inventory.py")

# Check connectivity
has_internet = False
try:
    import requests
    resp = requests.get("https://nojomalarab.com/", timeout=5, headers={"User-Agent": "AntigravitySEOBot/1.0"})
    log(f"Internet check to nojomalarab.com: Status {resp.status_code}")
    has_internet = True
except Exception as e:
    log(f"Internet check failed or offline: {e}")

# Read sitemap.xml if exists
sitemap_urls = set()
sitemap_path = Path("sitemap.xml")
if sitemap_path.exists():
    with open(sitemap_path, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f.read(), "lxml-xml" if "lxml" in sys.modules else "html.parser")
        for loc in soup.find_all("loc"):
            sitemap_urls.add(loc.get_text().strip())
    log(f"Loaded {len(sitemap_urls)} URLs from sitemap.xml")

# Read robots.txt
robots_txt = ""
if Path("robots.txt").exists():
    with open("robots.txt", "r", encoding="utf-8") as f:
        robots_txt = f.read()
    log("Loaded robots.txt")

# Find all local HTML files
workspace_root = Path(".")
html_files = []
for p in workspace_root.rglob("*.html"):
    rel = p.as_posix()
    if rel.startswith("audit/") or ".gemini" in rel:
        continue
    html_files.append(p)

log(f"Found {len(html_files)} local HTML files")

# Map file to canonical/slug/group
def categorize_file(rel_path):
    p_str = rel_path.replace("\\", "/")
    if p_str == "index.html":
        return "home", "/"
    elif p_str == "404.html":
        return "error", "/404.html"
    elif p_str.startswith("areas/"):
        if p_str == "areas/index.html":
            return "category", "/areas/"
        slug = p_str.replace("areas/", "").replace(".html", "")
        return "area", f"/areas/{slug}/"
    elif p_str.startswith("blogs/"):
        if p_str == "blogs/index.html":
            return "category", "/blogs/"
        slug = p_str.replace("blogs/", "").replace(".html", "")
        return "blog", f"/blogs/{slug}/"
    elif p_str.startswith("intercity-moving/"):
        slug = p_str.replace("intercity-moving/", "").replace(".html", "")
        return "intercity", f"/intercity-moving/{slug}/"
    elif p_str == "services/index.html":
        return "category", "/services/"
    elif p_str == "about/index.html":
        return "core", "/about/"
    elif p_str == "contact/index.html":
        return "core", "/contact/"
    elif p_str == "privacy-policy.html":
        return "legal", "/privacy-policy/"
    elif p_str == "terms.html":
        return "legal", "/terms/"
    else:
        slug = p_str.replace(".html", "")
        return "service", f"/{slug}/"

inventory_rows = []
headings_rows = []
fulltext_records = []

for file_path in sorted(html_files):
    rel_path = file_path.as_posix()
    group, expected_url_path = categorize_file(rel_path)
    file_size_bytes = file_path.stat().st_size
    
    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()
    
    soup = BeautifulSoup(content, "html.parser")
    
    # Title
    title_tag = soup.find("title")
    title = title_tag.get_text().strip() if title_tag else ""
    title_len = len(title)
    
    # Meta Description
    meta_desc_tag = soup.find("meta", attrs={"name": re.compile(r"^description$", re.I)})
    meta_desc = meta_desc_tag.get("content", "").strip() if meta_desc_tag else ""
    meta_desc_len = len(meta_desc)
    
    # Canonical
    canon_tag = soup.find("link", attrs={"rel": "canonical"})
    canonical = canon_tag.get("href", "").strip() if canon_tag else ""
    
    # Robots meta
    robots_meta_tag = soup.find("meta", attrs={"name": re.compile(r"^robots$", re.I)})
    robots_meta = robots_meta_tag.get("content", "").strip() if robots_meta_tag else ""
    
    # OpenGraph & Twitter
    og_title = soup.find("meta", property="og:title")
    og_title = og_title.get("content", "").strip() if og_title else ""
    og_desc = soup.find("meta", property="og:description")
    og_desc = og_desc.get("content", "").strip() if og_desc else ""
    og_img = soup.find("meta", property="og:image")
    og_img = og_img.get("content", "").strip() if og_img else ""
    tw_card = soup.find("meta", attrs={"name": "twitter:card"})
    tw_card = tw_card.get("content", "").strip() if tw_card else ""
    
    # Schema check
    schemas = soup.find_all("script", type="application/ld+json")
    has_schema = len(schemas) > 0
    schema_types = []
    for s in schemas:
        try:
            sd = json.loads(s.string or "{}")
            if isinstance(sd, dict):
                t = sd.get("@type", "")
                if t: schema_types.append(t)
                if "@graph" in sd:
                    for g in sd["@graph"]:
                        gt = g.get("@type", "")
                        if gt: schema_types.append(gt)
            elif isinstance(sd, list):
                for item in sd:
                    t = item.get("@type", "")
                    if t: schema_types.append(t)
        except Exception:
            pass
    schema_summary = ";".join(sorted(set(str(st) for st in schema_types)))
    
    # Headings
    h1s = [h.get_text().strip() for h in soup.find_all("h1")]
    h2s = [h.get_text().strip() for h in soup.find_all("h2")]
    h3s = [h.get_text().strip() for h in soup.find_all("h3")]
    h4s = [h.get_text().strip() for h in soup.find_all("h4")]
    
    # Record headings
    order = 1
    for h in soup.find_all(["h1", "h2", "h3", "h4", "h5", "h6"]):
        htext = re.sub(r"\s+", " ", h.get_text()).strip()
        headings_rows.append({
            "url_path": expected_url_path,
            "file": rel_path,
            "level": h.name.upper(),
            "order": order,
            "text": htext,
            "length": len(htext)
        })
        order += 1
        
    # Extract visible text (exclude script, style, noscript, etc.)
    for elem in soup(["script", "style", "noscript", "svg", "header", "footer", "nav"]):
        elem.extract()
        
    main_text = re.sub(r"\s+", " ", soup.get_text()).strip()
    word_count = len(main_text.split())
    
    # In sitemap check
    full_url = f"https://nojomalarab.com{expected_url_path}" if expected_url_path != "/" else "https://nojomalarab.com/"
    in_sitemap = full_url in sitemap_urls
    
    inventory_rows.append({
        "url_path": expected_url_path,
        "full_url": full_url,
        "file": rel_path,
        "group": group,
        "file_size_bytes": file_size_bytes,
        "title": title,
        "title_length": title_len,
        "meta_description": meta_desc,
        "meta_desc_length": meta_desc_len,
        "canonical": canonical,
        "canonical_match": canonical == full_url,
        "robots_meta": robots_meta,
        "h1_count": len(h1s),
        "h1_text": " | ".join(h1s),
        "h2_count": len(h2s),
        "h3_count": len(h3s),
        "h4_count": len(h4s),
        "word_count": word_count,
        "has_schema": has_schema,
        "schema_types": schema_summary,
        "in_sitemap": in_sitemap,
        "og_title": og_title,
        "og_image": og_img,
        "twitter_card": tw_card
    })

# Write 01-pages-inventory.csv
with open("audit/01-pages-inventory.csv", "w", encoding="utf-8-sig", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=inventory_rows[0].keys())
    writer.writeheader()
    writer.writerows(inventory_rows)
log(f"Written audit/01-pages-inventory.csv ({len(inventory_rows)} pages)")

# Write 03-headings.csv
if headings_rows:
    with open("audit/03-headings.csv", "w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=headings_rows[0].keys())
        writer.writeheader()
        writer.writerows(headings_rows)
    log(f"Written audit/03-headings.csv ({len(headings_rows)} headings)")

log("Inventory and Headings extraction completed successfully.")

