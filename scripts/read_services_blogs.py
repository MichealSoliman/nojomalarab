import re

pages = [
    'ikea-furniture-moving-jeddah',
    'kitchen-moving-jeddah',
    'ac-disassembly-and-moving-jeddah',
    'old-furniture-removal-jeddah',
    'small-moving-truck-jeddah',
    'filipino-moving-labour-jeddah'
]

for p in pages:
    path = f'{p}/index.html'
    try:
        with open(path, 'r', encoding='utf-8') as f:
            c = f.read()
        h1 = re.search(r'<h1[^>]*>(.*?)</h1>', c, re.S)
        desc = re.search(r'<meta\s+name=["\']description["\']\s+content=["\'](.*?)["\']', c, re.S)
        h1_text = re.sub(r'<[^>]+>', '', h1.group(1)).strip() if h1 else ''
        desc_text = desc.group(1).strip() if desc else ''
        print(f'=== {p} ===\nH1: {h1_text}\nDesc: {desc_text}\n')
    except Exception as e:
        print(f'Error reading {p}: {e}')

blogs = [
    'home-preparation-steps-before-moving',
    'furniture-moving-prices-jeddah-2026',
    'packing-fragile-electronics-glass-antiques',
    'protecting-furniture-jeddah-heat-humidity',
    'new-home-moving-checklist-jeddah',
    'how-to-choose-best-moving-company-in-jeddah'
]

print('\n--- BLOGS ---')
for b in blogs:
    path = f'blogs/{b}/index.html'
    try:
        with open(path, 'r', encoding='utf-8') as f:
            c = f.read()
        h1 = re.search(r'<h1[^>]*>(.*?)</h1>', c, re.S)
        desc = re.search(r'<meta\s+name=["\']description["\']\s+content=["\'](.*?)["\']', c, re.S)
        h1_text = re.sub(r'<[^>]+>', '', h1.group(1)).strip() if h1 else ''
        desc_text = desc.group(1).strip() if desc else ''
        print(f'=== blogs/{b} ===\nH1: {h1_text}\nDesc: {desc_text}\n')
    except Exception as e:
        print(f'Error reading {b}: {e}')

