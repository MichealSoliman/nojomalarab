import os
import re
from pathlib import Path
from bs4 import BeautifulSoup
from collections import Counter

print("=== Starting Check-Head Audit ===")

def get_canonical_path(file_path):
    p = file_path.as_posix()
    if p == "index.html": return "/"
    elif p == "404.html": return "/404.html"
    elif p.endswith("/index.html"): return "/" + p[:-11] + "/"
    elif p.endswith(".html"): return "/" + p[:-5] + "/"
    return "/" + p

all_html = [p for p in Path('.').rglob('*.html') if not str(p).startswith('audit') and '.gemini' not in str(p) and 'node_modules' not in p.as_posix() and 'components/' not in p.as_posix()]

records = []
titles = []
descs = []
canonicals = []

for p in sorted(all_html):
    rel = p.as_posix()
    c_path = get_canonical_path(p)
    expected_canon = f"https://nojomalarab.com{c_path}" if c_path != "/" else "https://nojomalarab.com/"
    
    soup = BeautifulSoup(p.read_text(encoding='utf-8', errors='ignore'), 'html.parser')
    
    t_tag = soup.find('title')
    title = t_tag.get_text().strip() if t_tag else ""
    t_len = len(title)
    
    d_tag = soup.find('meta', attrs={'name': re.compile(r'^description$', re.I)})
    desc = d_tag.get('content', '').strip() if d_tag else ""
    d_len = len(desc)
    
    c_tag = soup.find('link', rel='canonical')
    canon = c_tag.get('href', '').strip() if c_tag else ""
    
    rob_tag = soup.find('meta', attrs={'name': re.compile(r'^robots$', re.I)})
    robots = rob_tag.get('content', '').strip() if rob_tag else ""
    
    og_img_tag = soup.find('meta', property='og:image')
    og_img = og_img_tag.get('content', '').strip() if og_img_tag else ""
    
    h1s = [h.get_text().strip() for h in soup.find_all('h1')]
    
    titles.append(title)
    descs.append(desc)
    canonicals.append(canon)
    
    records.append({
        'file': rel,
        'c_path': c_path,
        'title': title,
        't_len': t_len,
        'desc': desc,
        'd_len': d_len,
        'canon': canon,
        'expected_canon': expected_canon,
        'canon_ok': canon == expected_canon,
        'robots': robots,
        'og_img': og_img,
        'h1_count': len(h1s)
    })

title_counts = Counter(titles)
desc_counts = Counter(descs)

dup_titles = [t for t, c in title_counts.items() if c > 1 and t]
dup_descs = [d for d, c in desc_counts.items() if c > 1 and d]
canon_errors = [r for r in records if not r['canon_ok']]

print(f"Total Pages Checked: {len(records)}")
print(f"Duplicate Titles: {len(dup_titles)}")
for dt in dup_titles:
    print(f"  DUP TITLE: '{dt}'")
    
print(f"Duplicate Descriptions: {len(dup_descs)}")
for dd in dup_descs:
    print(f"  DUP DESC: '{dd}'")
    
print(f"Canonical Mismatches: {len(canon_errors)}")
for ce in canon_errors:
    print(f"  CANON ERROR: {ce['file']} -> {ce['canon']} (expected {ce['expected_canon']})")

h1_errors = [r for r in records if r['h1_count'] != 1 and r['file'] != '404.html']
print(f"H1 Count Errors (!= 1): {len(h1_errors)}")
for he in h1_errors:
    print(f"  H1 ERROR: {he['file']} has {he['h1_count']} H1 tags")

if len(dup_titles) == 0 and len(dup_descs) == 0 and len(canon_errors) == 0 and len(h1_errors) == 0:
    print("ALL HEAD AND CANONICAL CHECKS PASSED: ZERO DUPLICATES OR MISMATCHES!")
