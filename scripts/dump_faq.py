with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

faq_idx = text.find('id="faq"')
if faq_idx != -1:
    print(text[faq_idx:faq_idx+2500])

