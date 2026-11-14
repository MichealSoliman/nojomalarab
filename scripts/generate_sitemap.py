import os
import re
import subprocess
from pathlib import Path

def get_canonical_path(file_path):
    p = file_path.as_posix()
    if p == "index.html": return "/"
    elif p == "404.html": return "/404.html"
    elif p.endswith("/index.html"): return "/" + p[:-11] + "/"
    elif p.endswith(".html"): return "/" + p[:-5] + "/"
    return "/" + p

# All indexable pages (exclude 404.html, node_modules, components, test, audit)
all_html = [p for p in Path('.').rglob('*.html') if not str(p).startswith('audit') and '.gemini' not in str(p) and 'node_modules' not in p.as_posix() and 'components/' not in p.as_posix()]
indexable = [p for p in all_html if p.name != "404.html"]

xml_entries = []

for p in sorted(indexable):
    c_path = get_canonical_path(p)
    full_url = f"https://nojomalarab.com{c_path}" if c_path != "/" else "https://nojomalarab.com/"
    
    # Get last commit date for this file
    try:
        git_date = subprocess.check_output(["git", "log", "-1", "--format=%cs", "--", str(p)]).decode().strip()
        if not git_date:
            git_date = "2026-11-14"
    except Exception:
        git_date = "2026-11-14"
        
    priority = "1.0" if c_path == "/" else ("0.8" if "/areas/" in c_path or "/services/" in c_path or "/furniture-moving-prices-jeddah/" in c_path else "0.7")
    changefreq = "weekly" if c_path == "/" else "monthly"
    
    xml_entries.append(f"""  <url>
    <loc>{full_url}</loc>
    <lastmod>{git_date}</lastmod>
    <changefreq>{changefreq}</changefreq>
    <priority>{priority}</priority>
  </url>""")

sitemap_content = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{chr(10).join(xml_entries)}
</urlset>
"""

Path("sitemap.xml").write_text(sitemap_content, encoding="utf-8")
print(f"Generated sitemap.xml with {len(xml_entries)} URLs matching exactly {len(indexable)} indexable pages.")
