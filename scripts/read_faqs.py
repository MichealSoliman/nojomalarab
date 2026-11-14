import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

faq_sec = re.search(r'<section id="faq"[\s\S]*?</section>', text)
if faq_sec:
    items = re.findall(r'<div class="faq-item[\s\S]*?</div>\s*</div>', faq_sec.group(0))
    print(f'Total FAQ items: {len(items)}')
    for i, item in enumerate(items):
        q = re.search(r'<button[^>]*>([\s\S]*?)</button>', item)
        a = re.search(r'<div id="faq-answer-\d+"[^>]*>([\s\S]*?)</div>', item)
        q_text = re.sub(r'<[^>]+>', '', q.group(1)).strip() if q else 'No Q'
        a_text = re.sub(r'<[^>]+>', '', a.group(1)).strip() if a else 'No A'
        print(f'{i+1}. Q: {q_text}\n   A: {a_text}\n')

