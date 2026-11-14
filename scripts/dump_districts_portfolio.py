with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
print('=== JEDDAH-DISTRICTS ===')
jd = re.search(r'<section id="jeddah-districts"[\s\S]*?</section>', text)
if jd: print(jd.group(0)[:1500])

print('=== PORTFOLIO ===')
pf = re.search(r'<section id="portfolio"[\s\S]*?</section>', text)
if pf: print(pf.group(0)[:1500])

print('=== WHYUS ===')
wu = re.search(r'<section id="whyus"[\s\S]*?</section>', text)
if wu: print(wu.group(0)[:1500])

