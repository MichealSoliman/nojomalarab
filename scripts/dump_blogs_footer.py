with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
print('=== BLOGS ===')
bl = re.search(r'<section id="latest-blogs"[\s\S]*?</section>', text)
if bl: print(bl.group(0)[:1500])

print('=== FOOTER ===')
ftr = re.search(r'<footer[\s\S]*?</footer>', text)
if ftr: print(ftr.group(0)[:2500])

