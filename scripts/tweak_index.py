with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace(
    'src="/assets/img/logo-128.webp" alt="شعار شركة نجوم العرب لنقل الأثاث بجدة" width="56" height="56"',
    'src="/assets/img/logo-128.webp" alt="شعار شركة نجوم العرب لنقل الأثاث بجدة" width="56" height="56" decoding="async"'
)

text = text.replace(
    'src="/assets/img/logo-128.webp" alt="شعار نجوم العرب" width="48" height="48"',
    'src="/assets/img/logo-128.webp" alt="شعار نجوم العرب" width="48" height="48" decoding="async"'
)

old_desc = 'شركة نقل عفش جدة – نجوم العرب: نقل أثاث مع فك وتركيب وتغليف للشقق والفلل والمكاتب بسيارات مجهزة في كل أحياء جدة. معاينة مجانية: 0500504024'
new_desc = 'شركة نقل عفش جدة – نجوم العرب: نقل أثاث مع فك وتركيب وتغليف للشقق والفلل والمكاتب بسيارات مجهزة في كل أحياء جدة. احجز معاينتك المجانية: 0500504024'
text = text.replace(old_desc, new_desc)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(text)

print('Updated successfully.')

