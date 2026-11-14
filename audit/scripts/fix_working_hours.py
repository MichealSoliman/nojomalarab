import re
from pathlib import Path

def log(msg):
    print(msg)

# 1. Update services/index.html hours
p_services = Path('services/index.html')
if p_services.exists():
    c = p_services.read_text(encoding='utf-8')
    
    # Replace claim in intro
    c = c.replace('نغطي جميع أحياء جدة ونقدم خدماتنا على مدار الساعة', 'نغطي جميع أحياء جدة ونقدم خدماتنا بأعلى كفاءة طوال ساعات العمل الرسمية')
    
    # Replace FAQ 7
    old_faq_q = 'هل تعملون طوال أيام الأسبوع؟'
    old_faq_a = '''<p>نعمل على مدار الساعة طوال أيام الأسبوع لخدمتكم، بما في ذلك أيام الجمعة والعطلات
                                        الرسمية:</p>
                                    <ul class="mt-2 space-y-1">
                                        <li class="flex items-center gap-2">✓ السبت - الخميس: 8 صباحاً - 10 مساءً</li>
                                        <li class="flex items-center gap-2">✓ يوم الجمعة: 4 عصراً - 10 مساءً</li>
                                        <li class="flex items-center gap-2">✓ خدمات نقل مجدولة طوال أيام العمل الرسمية
                                            الأسبوع</li>
                                        <li class="flex items-center gap-2">✓ يمكنك الاتصال بنا في أي وقت لحجز الخدمة'''
    
    new_faq_a = '''<p>نستقبل اتصالاتكم ونقدم خدمات النقل طوال ساعات العمل الرسمية:</p>
                                    <ul class="mt-2 space-y-1">
                                        <li class="flex items-center gap-2">✓ السبت - الخميس: 9:00 صباحاً - 9:00 مساءً</li>
                                        <li class="flex items-center gap-2">✓ يوم الجمعة: مغلق</li>
                                        <li class="flex items-center gap-2">✓ خدمات نقل مجدولة مسبقاً وتنسيق سريع للطلبات</li>
                                        <li class="flex items-center gap-2">✓ يمكنك التواصل معنا هاتفياً أو عبر واتساب لحجز موعدك'''
    
    c = c.replace(old_faq_a, new_faq_a)
    p_services.write_text(c, encoding='utf-8')
    log('Updated services/index.html hours')

# 2. Update contact/index.html hours
p_contact = Path('contact/index.html')
if p_contact.exists():
    c = p_contact.read_text(encoding='utf-8')
    c = c.replace('<span>السبت - الخميس: 8ص - 10م</span>', '<span>السبت - الخميس: 9ص - 9م (الجمعة مغلق)</span>')
    c = c.replace('على مدار الساعة طوال أيام الأسبوع.', 'طوال ساعات العمل الرسمية (السبت - الخميس: 9ص - 9م).')
    c = c.replace('خدمة عملاء على مدار الساعة طوال أيام الأسبوع', 'خدمة عملاء طوال ساعات العمل الرسمية المعتمدة')
    p_contact.write_text(c, encoding='utf-8')
    log('Updated contact/index.html hours')

# 3. Update villa-moving-jeddah/index.html
p_villa = Path('villa-moving-jeddah/index.html')
if p_villa.exists():
    c = p_villa.read_text(encoding='utf-8')
    c = c.replace('ساعة طوال أيام الأسبوع. بالإضافة إلى ذلك', 'ساعات العمل الرسمية بنظام مجدول ومسبق التنسيق. بالإضافة إلى ذلك')
    p_villa.write_text(c, encoding='utf-8')
    log('Updated villa-moving-jeddah/index.html hours')

# 4. Update neighborhoods 24h mentions
area_files = list(Path('areas').rglob('*.html'))
for af in area_files:
    c = af.read_text(encoding='utf-8')
    original = c
    c = c.replace('لخدمتك بأعلى سرعة على مدار 24 ساعة.', 'لخدمتك بأعلى سرعة واحترافية خلال ساعات العمل الرسمية.')
    c = c.replace('على مدار 24 ساعة.', 'بأعلى جاهزية واحترافية طوال ساعات العمل الرسمية.')
    c = c.replace('على مدار الساعة.', 'بأعلى جاهزية واحترافية طوال ساعات العمل الرسمية.')
    c = c.replace('على مدار الساعة بأفضل الأسعار وأعلى معايير الضمان.', 'بأعلى جاهزية واحترافية طوال ساعات العمل الرسمية وبأفضل الأسعار المناسبة.')
    c = c.replace('على مدار الساعة، ويمكنك أيضاً الاطلاع', 'بأعلى جاهزية خلال ساعات العمل الرسمية، ويمكنك أيضاً الاطلاع')
    c = c.replace('على مدار الساعة، ويمكنك استكشاف', 'بأعلى جاهزية خلال ساعات العمل الرسمية، ويمكنك استكشاف')
    if c != original:
        af.write_text(c, encoding='utf-8')
        log(f'Updated hours in {af}')

# 5. Update blogs
p_blog_best = Path('blogs/the-best-furniture-moving-company-in-jeddah/index.html')
if p_blog_best.exists():
    c = p_blog_best.read_text(encoding='utf-8')
    c = c.replace('فإن فريقنا جاهز لتلبية طلبك على مدار 24 ساعة طوال', 'فإن فريقنا جاهز لتلبية طلبك بأعلى كفاءة طوال ساعات العمل الرسمية')
    p_blog_best.write_text(c, encoding='utf-8')
    log('Updated blog the-best-furniture-moving-company-in-jeddah hours')

# 6. Update crane
p_crane = Path('furniture-lifting-crane-in-jeddah/index.html')
if p_crane.exists():
    c = p_crane.read_text(encoding='utf-8')
    c = c.replace('متاح خلال ساعات العمل الرسمية طوال أيام الأسبوع (الجمعة مغلق) بما فيها الجمعة والعطلات الرسمية', 'متاح خلال ساعات العمل الرسمية (السبت - الخميس: 9ص - 9م، الجمعة مغلق) مع جدولة مسبقة')
    p_crane.write_text(c, encoding='utf-8')
    log('Updated crane hours')

print('All hours unified successfully!')
