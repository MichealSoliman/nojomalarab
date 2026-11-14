import os
import re
from pathlib import Path
from bs4 import BeautifulSoup

def log(msg):
    with open("audit/run-log.txt", "a", encoding="utf-8") as f:
        f.write(f"[DUMP-CONTENT] {msg}\n")
    print(msg)

log("Starting content dumper...")

html_files = []
for p in Path(".").rglob("*.html"):
    rel = p.as_posix()
    if rel.startswith("audit/") or ".gemini" in rel:
        continue
    html_files.append(p)

site_fulltext_path = Path("audit/site-fulltext.txt")
with open(site_fulltext_path, "w", encoding="utf-8") as full_out:
    for fpath in sorted(html_files):
        rel = fpath.as_posix()
        slug = rel.replace("/", "__").replace(".html", "")
        if slug == "index":
            slug = "home"
            
        with open(fpath, "r", encoding="utf-8", errors="ignore") as f:
            raw_html = f.read()
            
        soup = BeautifulSoup(raw_html, "html.parser")
        
        # Extract title and headings before stripping
        title = soup.find("title")
        title_text = title.get_text().strip() if title else ""
        
        # We want full visible text for visitors.
        # Header and footer are part of the page visible experience, but let's separate main content and full text.
        # Remove only non-visible elements: script, style, noscript, svg, template
        for tag in soup(["script", "style", "noscript", "svg", "template"]):
            tag.extract()
            
        page_text = soup.get_text(separator="\n")
        lines = [line.strip() for line in page_text.splitlines() if line.strip()]
        clean_text = "\n".join(lines)
        
        # Write individual markdown file in audit/content/
        md_file = Path(f"audit/content/{slug}.md")
        with open(md_file, "w", encoding="utf-8") as md_out:
            md_out.write(f"# Page: {rel}\n")
            md_out.write(f"**Title:** {title_text}\n\n")
            md_out.write("## Visible Text Content\n\n")
            md_out.write(clean_text)
            md_out.write("\n")
            
        full_out.write(f"================================================================================\n")
        full_out.write(f"PAGE FILE: {rel} (Slug: {slug})\n")
        full_out.write(f"TITLE: {title_text}\n")
        full_out.write(f"================================================================================\n\n")
        full_out.write(clean_text)
        full_out.write("\n\n\n")

log(f"Content extraction complete. {len(html_files)} files processed.")

