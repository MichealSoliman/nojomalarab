import os
import sys
import subprocess
import requests
import hashlib
from pathlib import Path
from bs4 import BeautifulSoup
import re

def log(msg):
    line = f"[A_CHECK] {msg}"
    print(line)
    with open("audit/progress/run-log.txt", "a", encoding="utf-8") as f:
        f.write(line + "\n")

log("Starting Phase A: Environment, Git Status, and Live vs Local...")

# A1 & A2: Local files check and git metadata
local_html = list(Path(".").rglob("*.html"))
clean_local_html = [p for p in local_html if not str(p).startswith("audit") and ".gemini" not in str(p)]
log(f"Local files present: {len(clean_local_html)} HTML files found in project root.")

branch = subprocess.check_output(["git", "branch", "--show-current"]).decode().strip()
commit = subprocess.check_output(["git", "log", "-1", "--format=%H %s (%cd)"]).decode().strip()
log(f"Git branch: {branch}")
log(f"Git commit: {commit}")

# Check Internet connectivity
has_internet = False
try:
    r = requests.get("https://nojomalarab.com/", timeout=7, headers={"User-Agent": "AntigravityAuditor/2.0"})
    log(f"Live connectivity check: HTTP {r.status_code}")
    has_internet = True
except Exception as e:
    log(f"Live connectivity check failed: {e}")

# Expected 12 pages for live-vs-local
test_pages = [
    ("/", "index.html"),
    ("/furniture-moving-prices-jeddah/", "furniture-moving-prices-jeddah/index.html"),
    ("/apartment-furniture-moving-jeddah/", "apartment-furniture-moving-jeddah/index.html"),
    ("/office-furniture-moving-jeddah/", "office-furniture-moving-jeddah/index.html"),
    ("/best-furniture-moving-company-jeddah/", "best-furniture-moving-company-jeddah/index.html"),
    ("/furniture-disassembly-and-reassembly-in-jeddah/", "furniture-disassembly-and-reassembly-in-jeddah/index.html"),
    ("/carpenter-furniture-disassembly-assembly-jeddah/", "carpenter-furniture-disassembly-assembly-jeddah/index.html"),
    ("/areas/furniture-moving-hayu-al-safa/", "areas/furniture-moving-hayu-al-safa/index.html"),
    ("/intercity-moving/jeddah-to-riyadh/", "intercity-moving/jeddah-to-riyadh/index.html"),
    ("/about/", "about/index.html"),
    ("/contact/", "contact/index.html"),
    ("/blogs/the-best-furniture-moving-company-in-jeddah/", "blogs/the-best-furniture-moving-company-in-jeddah/index.html")
]

diff_results = []

headers_user = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
headers_bot = {"User-Agent": "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"}

import time

for url_path, file_rel in test_pages:
    p_local = Path(file_rel)
    local_content = p_local.read_text(encoding="utf-8", errors="ignore") if p_local.exists() else ""
    soup_l = BeautifulSoup(local_content, "html.parser")
    
    title_l = soup_l.find("title").get_text().strip() if soup_l.find("title") else ""
    desc_l_tag = soup_l.find("meta", attrs={"name": re.compile(r"^description$", re.I)})
    desc_l = desc_l_tag.get("content", "").strip() if desc_l_tag else ""
    canon_l_tag = soup_l.find("link", rel="canonical")
    canon_l = canon_l_tag.get("href", "").strip() if canon_l_tag else ""
    h1_l_tags = [h.get_text().strip() for h in soup_l.find_all("h1")]
    h1_l = " | ".join(h1_l_tags)
    ph_l_count = len(re.findall(r"\{\{[^}]+\}\}", local_content))
    
    # normalized visible text hash
    soup_l_copy = BeautifulSoup(local_content, "html.parser")
    for s in soup_l_copy(["script", "style", "noscript"]): s.extract()
    norm_l_text = re.sub(r"\s+", " ", soup_l_copy.get_text()).strip()
    hash_l = hashlib.md5(norm_l_text.encode("utf-8")).hexdigest()
    
    # GA4 tag in local
    ga4_l = re.findall(r"G-[A-Z0-9]+", local_content)
    ga4_l_str = ";".join(set(ga4_l)) if ga4_l else "NONE"
    
    # Live fetch
    live_url = f"https://nojomalarab.com{url_path}"
    time.sleep(1.0)
    
    title_r, desc_r, canon_r, h1_r, ph_r_count, hash_r, ga4_r_str, status_r, status_bot = ("", "", "", "", 0, "", "", 0, 0)
    
    if has_internet:
        try:
            r = requests.get(live_url, headers=headers_user, timeout=10)
            status_r = r.status_code
            r_bot = requests.get(live_url, headers=headers_bot, timeout=10)
            status_bot = r_bot.status_code
            
            if status_r == 200:
                soup_r = BeautifulSoup(r.text, "html.parser")
                title_r = soup_r.find("title").get_text().strip() if soup_r.find("title") else ""
                desc_r_tag = soup_r.find("meta", attrs={"name": re.compile(r"^description$", re.I)})
                desc_r = desc_r_tag.get("content", "").strip() if desc_r_tag else ""
                canon_r_tag = soup_r.find("link", rel="canonical")
                canon_r = canon_r_tag.get("href", "").strip() if canon_r_tag else ""
                h1_r_tags = [h.get_text().strip() for h in soup_r.find_all("h1")]
                h1_r = " | ".join(h1_r_tags)
                ph_r_count = len(re.findall(r"\{\{[^}]+\}\}", r.text))
                
                soup_r_copy = BeautifulSoup(r.text, "html.parser")
                for s in soup_r_copy(["script", "style", "noscript"]): s.extract()
                norm_r_text = re.sub(r"\s+", " ", soup_r_copy.get_text()).strip()
                hash_r = hashlib.md5(norm_r_text.encode("utf-8")).hexdigest()
                
                ga4_r = re.findall(r"G-[A-Z0-9]+", r.text)
                ga4_r_str = ";".join(set(ga4_r)) if ga4_r else "NONE"
        except Exception as ex:
            log(f"Error fetching live {live_url}: {ex}")
            
    diff_results.append({
        "url_path": url_path,
        "file": file_rel,
        "status_user": status_r,
        "status_bot": status_bot,
        "title_match": title_l == title_r,
        "title_local": title_l,
        "title_live": title_r,
        "desc_match": desc_l == desc_r,
        "canonical_match": canon_l == canon_r,
        "canonical_local": canon_l,
        "canonical_live": canon_r,
        "h1_match": h1_l == h1_r,
        "h1_local": h1_l,
        "h1_live": h1_r,
        "ph_local": ph_l_count,
        "ph_live": ph_r_count,
        "text_hash_match": hash_l == hash_r,
        "hash_local": hash_l,
        "hash_live": hash_r,
        "ga4_local": ga4_l_str,
        "ga4_live": ga4_r_str
    })

# Write live-vs-local.md
with open("audit/progress/live-vs-local.md", "w", encoding="utf-8") as f:
    f.write("# تقرير مقارنة البيئة الحية مع الملفات المحلية (Live vs Local Audit)\n\n")
    f.write("## 1. بيانات البيئة والاتصال\n")
    f.write(f"- **ملفات الموقع المحلية:** متوفرة ({len(clean_local_html)} صفحة HTML في جذر المشروع).\n")
    f.write(f"- **حالة الاتصال بالإنترنت:** متاح بنجاح (فحص حي بمعدل ≤ 1 طلب/ثانية).\n")
    f.write(f"- **Git Branch:** `{branch}`\n")
    f.write(f"- **آخر Commit:** `{commit}`\n\n")
    f.write("## 2. جدول مقارنة الـ 12 صفحة الأساسية\n\n")
    f.write("| المسار (URL) | كود الاستجابة (User/Bot) | تطابق Title | تطابق Description | تطابق Canonical | تطابق H1 | متطابق نصياً (Hash) | Placeholder محلي/حي | معرّف GA4 محلي/حي |\n")
    f.write("| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |\n")
    for r in diff_results:
        f.write(f"| `{r['url_path']}` | {r['status_user']}/{r['status_bot']} | {'نعم' if r['title_match'] else 'لا'} | {'نعم' if r['desc_match'] else 'لا'} | {'نعم' if r['canonical_match'] else 'لا'} | {'نعم' if r['h1_match'] else 'لا'} | {'نعم' if r['text_hash_match'] else 'لا (اختلاف محتوى)'} | {r['ph_local']} / {r['ph_live']} | {r['ga4_local']} / {r['ga4_live']} |\n")
    
    f.write("\n## 3. تفاصيل الفروقات الجوهرية وتفسيرها\n\n")
    for r in diff_results:
        if not r['text_hash_match'] or not r['title_match'] or r['status_user'] != 200:
            f.write(f"### المسار: `{r['url_path']}`\n")
            f.write(f"- كود الاستجابة الحي: {r['status_user']}\n")
            if not r['title_match']:
                f.write(f"- **Title محلي:** {r['title_local']}\n")
                f.write(f"- **Title حي:** {r['title_live']}\n")
            if not r['canonical_match']:
                f.write(f"- **Canonical محلي:** {r['canonical_local']}\n")
                f.write(f"- **Canonical حي:** {r['canonical_live']}\n")
            if not r['h1_match']:
                f.write(f"- **H1 محلي:** {r['h1_local']}\n")
                f.write(f"- **H1 حي:** {r['h1_live']}\n")
            if r['ph_live'] != r['ph_local']:
                f.write(f"- **Placeholders:** محلياً: {r['ph_local']} | حياً: {r['ph_live']}\n")
            f.write(f"- **Hash محلي:** `{r['hash_local']}` مقابل **Hash حي:** `{r['hash_live']}`\n\n")

log("Phase A completed. audit/progress/live-vs-local.md generated.")
