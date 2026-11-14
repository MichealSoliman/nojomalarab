with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
print('=== ABOUT ===')
about = re.search(r'<section id="about"[\s\S]*?</section>', text)
if about: print(about.group(0))

print('=== SERVICES ===')
srv = re.search(r'<section id="services"[\s\S]*?</section>', text)
if srv: print(srv.group(0)[:2500])

