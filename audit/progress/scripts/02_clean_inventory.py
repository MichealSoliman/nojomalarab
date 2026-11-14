import os
import re
import csv
import json
import time
from pathlib import Path
from bs4 import BeautifulSoup
from urllib.parse import urlparse

def log(msg):
    line = f"[CLEAN_INVENTORY] {msg}"
    print(line)
    with open("audit/progress/run-log.txt", "a", encoding="utf-8") as f:
        f.write(line + "\n")

log("Starting clean inventory & route normalization...")

# Clean canonical mapping rule
def get_canonical_path(file_path):
    p = file_path.as_posix()
    if p == "index.html":
        return "/"
    elif p == "404.html":
        return "/404.html"
    elif p.endswith("/index.html"):
        return "/" + p[:-10] + "/"
    elif p.endswith(".html"):
        return "/" + p[:-5] + "/"
    return "/" + p

# All local HTML files excluding audit and hidden
all_files = [p for p in Path(".").rglob("*.html") if not str(p).startswith("audit") and ".gemini" not in str(p)]
log(f"Total HTML files found: {len(all_files)}")

# Identify invalid / should-not-publish files
invalid_files = []
publishable_files = []
for p in all_files:
    posix = p.as_posix()
    if "node_modules" in posix or "components/" in posix:
        invalid_files.append(p)
    else:
        publishable_files.append(p)

log(f"Publishable files: {len(publishable_files)} | Non-publishable files: {len(invalid_files)}")

# Load sitemap.xml
sitemap_urls = set()
sitemap_path = Path("sitemap.xml")
if sitemap_path.exists():
    with open(sitemap_path, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f.read(), "html.parser")
        for loc in soup.find_all("loc"):
            sitemap_urls.add(loc.get_text().strip())
log(f"Sitemap URLs count: {len(sitemap_urls)}")

# Map clean paths
path_to_file = {}
for p in publishable_files:
    c_path = get_canonical_path(p)
    path_to_file[c_path] = p

inventory_rows = []
all_links = []
all_images = []

for p in sorted(publishable_files):
    rel = p.as_posix()
    c_path = get_canonical_path(p)
    full_url = f"https://nojomalarab.com{c_path}" if c_path != "/" else "https://nojomalarab.com/"
    
    content = p.read_text(encoding="utf-8", errors="ignore")
    soup = BeautifulSoup(content, "html.parser")
    
    # Title
    t_tag = soup.find("title")
    title = t_tag.get_text().strip() if t_tag else ""
    
    # Meta Description
    d_tag = soup.find("meta", attrs={"name": re.compile(r"^description$", re.I)})
    desc = d_tag.get("content", "").strip() if d_tag else ""
    
    # Canonical
    c_tag = soup.find("link", rel="canonical")
    canon = c_tag.get("href", "").strip() if c_tag else ""
    
    # H1
    h1s = [h.get_text().strip() for h in soup.find_all("h1")]
    h1_text = " | ".join(h1s)
    
    # Schema check
    schemas = soup.find_all("script", type="application/ld+json")
    has_schema = len(schemas) > 0
    
    # Word count
    soup_copy = BeautifulSoup(content, "html.parser")
    for s in soup_copy(["script", "style", "noscript", "svg"]): s.extract()
    wc = len(soup_copy.get_text().split())
    
    # Check Placeholders
    ph_matches = re.findall(r"\{\{[^}]+\}\}", content)
    
    inventory_rows.append({
        "url_path": c_path,
        "full_url": full_url,
        "file": rel,
        "title": title,
        "title_len": len(title),
        "desc": desc,
        "desc_len": len(desc),
        "canonical": canon,
        "canonical_valid": canon == full_url,
        "h1_count": len(h1s),
        "h1_text": h1_text,
        "word_count": wc,
        "in_sitemap": full_url in sitemap_urls,
        "placeholders_count": len(ph_matches),
        "placeholders": ";".join(ph_matches)
    })
    
    # Links audit
    for a in soup.find_all("a", href=True):
        href = a["href"].strip()
        anchor = re.sub(r"\s+", " ", a.get_text()).strip()
        rel_attr = a.get("rel", "")
        if isinstance(rel_attr, list): rel_attr = " ".join(rel_attr)
        
        # Resolve target
        link_type = "unknown"
        target_clean = href
        is_broken = False
        
        if href.startswith("tel:"):
            link_type = "tel"
        elif href.startswith("mailto:"):
            link_type = "mailto"
        elif "wa.me" in href or "whatsapp" in href:
            link_type = "whatsapp"
        elif href.startswith("#"):
            link_type = "anchor"
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
            # Relative resolution
            if href.startswith("/"):
                target_clean = href
            else:
                # Resolve relative to current c_path
                parent = c_path if c_path.endswith("/") else c_path + "/"
                parts = (parent + href).split("/")
                resolved = []
                for pt in parts:
                    if pt == "..":
                        if resolved: resolved.pop()
                    elif pt == "." or pt == "":
                        continue
                    else:
                        resolved.append(pt)
                target_clean = "/" + "/".join(resolved)
                if not href.endswith(".html") and not href.endswith(".xml") and not target_clean.endswith("/"):
                    target_clean += "/"
                    
        if link_type == "internal":
            base_target = target_clean.split("#")[0].split("?")[0]
            if base_target.endswith(".html") and base_target != "/404.html":
                # Check canonical equivalent
                base_target = base_target[:-5] + "/"
            if base_target not in path_to_file and base_target != "/sitemap.xml":
                is_broken = True
                
        all_links.append({
            "source_file": rel,
            "source_path": c_path,
            "href": href,
            "target_clean": target_clean,
            "link_type": link_type,
            "anchor": anchor,
            "rel": rel_attr,
            "is_broken": is_broken
        })

    # Images audit
    for img in soup.find_all("img"):
        src = img.get("src", "").strip()
        alt = img.get("alt", "")
        w = img.get("width", "")
        h = img.get("height", "")
        loading = img.get("loading", "")
        decoding = img.get("decoding", "")
        
        # Check existence on disk
        clean_src = src.lstrip("/")
        if clean_src.startswith("../"):
            clean_src = clean_src.replace("../", "")
        img_p = Path(clean_src)
        exists = img_p.exists() and img_p.is_file()
        
        all_images.append({
            "page": rel,
            "src": src,
            "exists": exists,
            "alt": alt,
            "width": w,
            "height": h,
            "loading": loading,
            "decoding": decoding
        })

log(f"Total links parsed: {len(all_links)}")
broken_links = [l for l in all_links if l["is_broken"]]
log(f"Truly broken internal links: {len(broken_links)}")
log(f"Total images parsed: {len(all_images)}")

# Save clean inventory
with open("audit/progress/01-clean-inventory.csv", "w", encoding="utf-8-sig", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=inventory_rows[0].keys())
    writer.writeheader()
    writer.writerows(inventory_rows)

log("Clean inventory written to audit/progress/01-clean-inventory.csv")
