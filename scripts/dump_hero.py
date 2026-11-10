with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
hero = re.search(r'<section id="home"[\s\S]*?</section>', text)
if hero:
    print(hero.group(0))

