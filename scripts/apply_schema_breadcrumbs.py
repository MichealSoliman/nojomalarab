import os
import glob
import re
import json

def get_page_info(filepath, content):
    # Determine page type, parent, and current name
    rel = filepath.replace('\\', '/')
    if rel == 'index.html':
        return None
    
    # Extract h1 or title
    h1_match = re.search(r'<h1[^>]*>(.*?)</h1>', content, re.I | re.S)
    h1_text = re.sub(r'<[^>]+>', '', h1_match.group(1)).strip() if h1_match else ''
    
    # Defaults
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
        # extract neighborhood name
        m = re.search(r'حي\s+([\u0621-\u064A\s]+)', h1_text)
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
        # Service page
        parent_name = "خدماتنا"
        parent_url = "https://nojomalarab.com/services/"
        name = h1_text if len(h1_text) < 35 else h1_text[:32] + '...'
        if rel.endswith('/index.html'):
            url = f"https://nojomalarab.com/{rel[:-len('index.html')]}"
        else:
            url = f"https://nojomalarab.com/{rel}"
            
    return {
        'name': name,
        'url': url,
        'parent_name': parent_name,
        'parent_url': parent_url,
        'h1': h1_text
    }

def update_schema_and_breadcrumbs():
    html_files = [f.replace('\\', '/') for f in glob.glob('**/*.html', recursive=True) if not f.startswith('.git') and f != 'components/footer.html']
    
    for filepath in sorted(html_files):
        if filepath == 'index.html' or filepath == '404.html':
            continue
            
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        orig_content = content
        info = get_page_info(filepath, content)
        if not info:
            continue
            
        # 1. Ensure BreadcrumbList JSON-LD exists
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
        
        # Check if BreadcrumbList already in content
        if 'BreadcrumbList' in content:
            # Replace existing BreadcrumbList schema block
            content = re.sub(
                r'<script\s+type=["\']application/ld\+json["\']>\s*\{\s*"@context":\s*"https://schema\.org",\s*"@type":\s*"BreadcrumbList"[\s\S]*?</script>',
                f'<script type="application/ld+json">\n{bc_schema_json}\n</script>',
                content,
                flags=re.I
            )
        else:
            # Append before </head>
            content = content.replace('</head>', f'    <script type="application/ld+json">\n{bc_schema_json}\n    </script>\n</head>')

        # 2. Check MovingCompany / WebPage schema
        # In subpages, replace duplicate standalone MovingCompany schemas with reference to https://nojomalarab.com/#organization
        # If schema has "@type": "MovingCompany", check if it has provider/parentOrganization
        # We can add a clean WebPage schema if not present
        if 'WebPage' not in content and 'Article' not in content and 'BlogPosting' not in content:
            webpage_schema = {
                "@context": "https://schema.org",
                "@type": "WebPage",
                "@id": f"{info['url']}#webpage",
                "url": info['url'],
                "name": info['name'],
                "isPartOf": {
                    "@type": "WebSite",
                    "@id": "https://nojomalarab.com/#website",
                    "url": "https://nojomalarab.com/",
                    "name": "شركة نجوم العرب لنقل الأثاث بجدة"
                },
                "publisher": {
                    "@id": "https://nojomalarab.com/#organization"
                }
            }
            wp_json = json.dumps(webpage_schema, ensure_ascii=False, indent=2)
            content = content.replace('</head>', f'    <script type="application/ld+json">\n{wp_json}\n    </script>\n</head>')

        # 3. Visible breadcrumbs check
        # Check if visible breadcrumb exists
        has_vis_bc = bool(re.search(r'class="[^"]*breadcrumb[^"]*"|<nav[^>]*aria-label=["\'](?:Breadcrumb|مسار التصفح|مسار التنقل)["\']', content, re.I))
        if not has_vis_bc:
            # Generate breadcrumb HTML
            bc_html_items = [
                f'<a href="https://nojomalarab.com/" class="hover:text-primary transition-colors">الرئيسية</a>',
                '<span class="mx-2 text-gray-400">/</span>'
            ]
            if info['parent_name'] and info['parent_url']:
                bc_html_items.append(f'<a href="{info["parent_url"]}" class="hover:text-primary transition-colors">{info["parent_name"]}</a>')
                bc_html_items.append('<span class="mx-2 text-gray-400">/</span>')
            bc_html_items.append(f'<span class="text-secondary font-bold">{info["name"]}</span>')
            
            breadcrumb_html = f'''
        <!-- Breadcrumb Bar -->
        <nav aria-label="مسار التنقل" class="flex items-center text-xs md:text-sm text-gray-500 mb-6 bg-white p-3 rounded-lg shadow-sm">
            {' '.join(bc_html_items)}
        </nav>
'''
            # Insert breadcrumb HTML after navbar or at top of main container
            # Try finding container mx-auto pt-[... or <main
            if '<div class="container mx-auto px-4 py-8 pt-[100px]">' in content:
                content = content.replace(
                    '<div class="container mx-auto px-4 py-8 pt-[100px]">',
                    '<div class="container mx-auto px-4 py-8 pt-[100px]">' + breadcrumb_html
                )
            elif '<div class="container mx-auto px-4 py-8 pt-[110px]">' in content:
                content = content.replace(
                    '<div class="container mx-auto px-4 py-8 pt-[110px]">',
                    '<div class="container mx-auto px-4 py-8 pt-[110px]">' + breadcrumb_html
                )
            elif '<main class="' in content:
                content = re.sub(
                    r'(<main[^>]*>)',
                    r'\1\n<div class="container mx-auto px-4 pt-4">' + breadcrumb_html + '</div>',
                    content,
                    count=1
                )
            elif '<main id="main-content"' in content:
                content = re.sub(
                    r'(<main id="main-content"[^>]*>)',
                    r'\1\n<div class="container mx-auto px-4 pt-4">' + breadcrumb_html + '</div>',
                    content,
                    count=1
                )
            elif '</nav>' in content:
                # after the navbar closing tag
                # find the first section/div after </nav>
                content = re.sub(
                    r'(</nav>\s*)(<div|<section|<main)',
                    r'\1<div class="container mx-auto px-4 pt-24 -mb-16 relative z-10">' + breadcrumb_html + r'</div>\n\2',
                    content,
                    count=1
                )
            print(f'Added visible breadcrumb to {filepath}')

        if content != orig_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f'Updated schema/breadcrumb in {filepath}')

if __name__ == '__main__':
    update_schema_and_breadcrumbs()

