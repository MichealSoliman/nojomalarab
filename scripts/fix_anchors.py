import glob
import re
import csv

files = glob.glob('*/*.html') + glob.glob('*/*/*.html') + glob.glob('*.html')
files = [f for f in files if 'backup' not in f and f != 'index.html']

records = []

# Regex to match <a> tags
a_regex = re.compile(r'<a\s+([^>]*?)>(.*?)</a>', re.DOTALL | re.IGNORECASE)
href_regex = re.compile(r'href=["\']([^"\']*)["\']', re.IGNORECASE)

patterns_to_home = [
    'شركة نقل عفش جدة',
    'شركة نقل عفش بجدة',
    'نقل عفش جدة',
    'نقل عفش بجدة',
    'شركة نقل اثاث',
    'شركة نقل أثاث',
    'نقل العفش والأثاث بجدة',
    'نقل وتجهيز الأثاث بجدة'
]

for f in files:
    with open(f, 'r', encoding='utf-8', errors='ignore') as fp:
        content = fp.read()
        
    modified = [False]
    
    def make_replacer(f_name):
        def replacer(match):
            attrs = match.group(1)
            inner_html = match.group(2)
            
            href_match = href_regex.search(attrs)
            if not href_match:
                return match.group(0)
                
            href = href_match.group(1).strip()
            anchor_text = re.sub(r'<[^>]+>', '', inner_html).strip()
            
            if anchor_text == 'الرئيسية':
                return match.group(0)
                
            is_target_anchor = any(p in anchor_text for p in patterns_to_home)
            
            if 'best-furniture-moving-company-jeddah' in href and is_target_anchor:
                new_href = '/'
                new_attrs = href_regex.sub(f'href="{new_href}"', attrs)
                records.append({
                    'file': f_name,
                    'old_anchor': anchor_text,
                    'old_href': href,
                    'new_href': new_href
                })
                modified[0] = True
                return f'<a {new_attrs}>{inner_html}</a>'
                
            return match.group(0)
        return replacer

    new_content = a_regex.sub(make_replacer(f), content)
    if modified[0]:
        with open(f, 'w', encoding='utf-8') as fp:
            fp.write(new_content)

with open('anchors-report.csv', 'w', encoding='utf-8-sig', newline='') as fp:
    writer = csv.DictWriter(fp, fieldnames=['file', 'old_anchor', 'old_href', 'new_href'])
    writer.writeheader()
    for r in records:
        writer.writerow(r)

print(f"Total anchors updated: {len(records)}")
