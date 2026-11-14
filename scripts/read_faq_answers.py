import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

faq_sec = re.search(r'<section id="faq"[\s\S]*?</section>', text)
if faq_sec:
    ans = re.findall(r'<div id="faq-answer-\d+"[\s\S]*?</div>\s*</div>', faq_sec.group(0))
    for i, a in enumerate(ans):
        clean = re.sub(r'<[^>]+>', ' ', a)
        clean = ' '.join(clean.split())
        print(f'{i+1}: {clean[:150]}...')

