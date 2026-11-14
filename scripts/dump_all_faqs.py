import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

faq_sec = re.search(r'<section id="faq"[\s\S]*?</section>', text)
if faq_sec:
    btns = re.findall(r'<button[^>]*id="(faq-btn-\d+)"[^>]*>([\s\S]*?)</button>', faq_sec.group(0))
    for btn_id, btn_html in btns:
        ans_id = btn_id.replace('btn', 'ans')
        ans_match = re.search(rf'<div id="{ans_id}"[\s\S]*?<div class="[^"]*text-gray-600[^"]*">([\s\S]*?)</div>', faq_sec.group(0))
        q = re.sub(r'<[^>]+>', '', btn_html).strip()
        a = re.sub(r'<[^>]+>', '', ans_match.group(1)).strip() if ans_match else 'MISSING'
        print(f'Q: {q}\nA: {a}\n')

