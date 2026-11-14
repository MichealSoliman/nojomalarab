import re

with open('areas/furniture-moving-hayu-alhamdaniyah/index.html', 'r', encoding='utf-8') as f:
    c = f.read()

m = re.search(r'breadcrumb', c, re.I)
if m:
    start = max(0, m.start() - 200)
    end = min(len(c), m.end() + 200)
    print(c[start:end])

