import os
import re
import csv
from pathlib import Path
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin

print("=== Starting Check-Links Audit ===")

# Canonical routes calculation
def get_canonical_path(file_path):
    p = file_path.as_posix()
    if p == "index.html": return "/"
    elif p == "404.html": return "/404.html"
    elif p.endswith("/index.html"): return "/" + p[:-11] + "/"
    elif p.endswith(".html"): return "/" + p[:-5] + "/"
    return "/" + p

all_html = [p for p in Path('.').rglob('*.html') if not str(p).startswith('audit') and '.gemini' not in str(p) and 'node_modules' not in p.as_posix()]
valid_routes = set(get_canonical_path(p) for p in all_html)
valid_routes.add("/sitemap.xml")

missing_links = []
total_internal = 0

for p in sorted(all_html):
    rel = p.as_posix()
    c_path = get_canonical_path(p)
    base_url = f"https://nojomalarab.com{c_path}"
    
    soup = BeautifulSoup(p.read_text(encoding='utf-8', errors='ignore'), 'html.parser')
    
    # 1. Check <a> links
    for a in soup.find_all('a', href=True):
        href = a['href'].strip()
        if href.startswith('tel:') or href.startswith('mailto:') or 'wa.me' in href or 'whatsapp' in href or href.startswith('#'):
            continue
            
        full = urljoin(base_url, href)
        parsed = urlparse(full)
        if "nojomalarab.com" in parsed.netloc or not parsed.netloc:
            total_internal += 1
            target = parsed.path
            if not target.endswith('/') and not target.endswith('.html') and not target.endswith('.xml'):
                target += '/'
            if target == '': target = '/'
            
            target_canon = target[:-5] + '/' if target.endswith('.html') and target != '/404.html' else target
            
            if target not in valid_routes and target_canon not in valid_routes:
                missing_links.append((rel, href, target, '<a> link'))
                
    # 2. Check <img> src
    for img in soup.find_all('img', src=True):
        src = img['src'].strip()
        if src.startswith('http://') or src.startswith('https://'):
            parsed = urlparse(src)
            if 'nojomalarab.com' in parsed.netloc:
                src_path = parsed.path.lstrip('/')
                if not Path(src_path).exists():
                    missing_links.append((rel, src, src_path, '<img> src'))
        else:
            clean_src = src.lstrip('/')
            if clean_src.startswith('../'):
                clean_src = clean_src.replace('../', '')
            if not Path(clean_src).exists():
                missing_links.append((rel, src, clean_src, '<img> src'))

print(f"Total internal links evaluated: {total_internal}")
print(f"Total missing targets: {len(missing_links)}")
for m in missing_links:
    print(f"  MISSING: {m[0]} -> {m[1]} ({m[3]})")

if len(missing_links) == 0:
    print("ALL INTERNAL LINKS AND IMAGES RESOLVED: ZERO MISSING!")
