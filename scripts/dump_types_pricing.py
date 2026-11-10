with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
print('=== FURNITURE-TYPES ===')
ft = re.search(r'<section id="furniture-types"[\s\S]*?</section>', text)
if ft: print(ft.group(0)[:1500])

print('=== PRICING ===')
pr = re.search(r'<section id="pricing-section"[\s\S]*?</section>', text)
if pr: print(pr.group(0)[:2500])

