import glob
import re
import json

def get_page_info(filepath, content):
    rel = filepath.replace('\\', '/')
    if rel == 'index.html':
        return None
    
    # Extract h1 or title
    h1_match = re.search(r'<h1[^>]*>(.*?)</h1>', content, re.I | re.S)
    h1_text = re.sub(r'<[^>]+>', '', h1_match.group(1)).strip() if h1_match else ''
    # remove newlines and multi spaces
    h1_text = re.sub(r'\s+', ' ', h1_text)
    
    parent_name = None
    parent_url = None
    
    if rel == 'about/index.html':
        name = "من نحن"
        url = "https://nojomalarab.com/about/"
    elif rel == 'contact/index.html':
        name = "اتصل بنا"
        url = "https://nojomalarab.com/contact/"
    elif rel == 'services/index.html':
        name = "خدماتنا"
        url = "https://nojomalarab.com/services/"
    elif rel == 'areas/index.html':
        name = "أحياء جدة"
        url = "https://nojomalarab.com/areas/"
    elif rel == 'blogs/index.html':
        name = "المدونة"
        url = "https://nojomalarab.com/blogs/"
    elif rel == 'privacy-policy.html':
        name = "سياسة الخصوصية"
        url = "https://nojomalarab.com/privacy-policy.html"
    elif rel == 'terms.html':
        name = "الشروط والأحكام"
        url = "https://nojomalarab.com/terms.html"
    elif rel == '404.html':
        name = "الصفحة غير موجودة"
        url = "https://nojomalarab.com/404.html"
    elif rel.startswith('areas/'):
        parent_name = "أحياء جدة"
        parent_url = "https://nojomalarab.com/areas/"
        m = re.search(r'حي\s+([\u0621-\u064A]+)', h1_text)
        if m:
            name = f"حي {m.group(1).strip()}"
        else:
            name = h1_text[:30]
        url = f"https://nojomalarab.com/{rel[:-len('index.html')]}"
    elif rel.startswith('blogs/'):
        parent_name = "المدونة"
        parent_url = "https://nojomalarab.com/blogs/"
        name = h1_text if len(h1_text) < 40 else h1_text[:37] + '...'
        url = f"https://nojomalarab.com/{rel[:-len('index.html')]}"
    elif rel.startswith('intercity-moving/') and rel != 'intercity-moving/index.html':
        parent_name = "نقل بين المدن"
        parent_url = "https://nojomalarab.com/intercity-moving/"
        name = h1_text if len(h1_text) < 35 else h1_text[:32] + '...'
        url = f"https://nojomalarab.com/{rel[:-len('index.html')]}"
    elif rel == 'intercity-moving/index.html':
        name = "نقل عفش بين المدن"
        url = "https://nojomalarab.com/intercity-moving/"
    else:
        parent_name = "خدماتنا"
        parent_url = "https://nojomalarab.com/services/"
        name = h1_text if len(h1_text) < 35 else h1_text[:32] + '...'
        if rel.endswith('/index.html'):
            url = f"https://nojomalarab.com/{rel[:-len('index.html')]}"
        else:
            url = f"https://nojomalarab.com/{rel}"
            
    name = re.sub(r'[\r\n\t]+', ' ', name).strip()
    return {
        'name': name,
        'url': url,
        'parent_name': parent_name,
        'parent_url': parent_url,
        'h1': h1_text
    }

def fix_breadcrumbs():
    targets = [
        'carpenter-furniture-disassembly-assembly-jeddah/index.html',
        'intercity-moving/jeddah-to-dammam/index.html',
        'intercity-moving/jeddah-to-makkah/index.html',
        'intercity-moving/jeddah-to-riyadh/index.html',
        'intercity-moving/jeddah-to-taif/index.html'
    ]
    for filepath in targets:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        info = get_page_info(filepath, content)
        items = [
            {
                "@type": "ListItem",
                "position": 1,
                "name": "الرئيسية",
                "item": "https://nojomalarab.com/"
            }
        ]
        if info['parent_name'] and info['parent_url']:
            items.append({
                "@type": "ListItem",
                "position": 2,
                "name": info['parent_name'],
                "item": info['parent_url']
            })
            items.append({
                "@type": "ListItem",
                "position": 3,
                "name": info['name'],
                "item": info['url']
            })
        else:
            items.append({
                "@type": "ListItem",
                "position": 2,
                "name": info['name'],
                "item": info['url']
            })
            
        bc_schema_dict = {
            "@context": "https://schema.org",
            "@type": "BreadcrumbList",
            "itemListElement": items
        }
        bc_schema_json = json.dumps(bc_schema_dict, ensure_ascii=False, indent=2)
        content = re.sub(
            r'<script\s+type=["\']application/ld\+json["\']>\s*\{\s*"@context":\s*"https://schema\.org",\s*"@type":\s*"BreadcrumbList"[\s\S]*?</script>',
            f'<script type="application/ld+json">\n{bc_schema_json}\n</script>',
            content,
            flags=re.I
        )
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'Fixed breadcrumb schema in {filepath}')

if __name__ == '__main__':
    fix_breadcrumbs()

