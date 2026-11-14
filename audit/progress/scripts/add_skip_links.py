import re
from pathlib import Path

html_files = [p for p in Path('.').rglob('*.html') if not str(p).startswith('audit') and '.gemini' not in str(p)]
skip_link_html = '''
    <!-- Skip Link for Accessibility -->
    <a href="#main-content"
        class="sr-only focus:not-sr-only focus:fixed focus:top-4 focus:right-4 focus:z-50 focus:bg-orange-500 focus:text-white focus:px-4 focus:py-2 focus:rounded-lg focus:shadow-xl focus:outline-none focus:ring-2 focus:ring-white">
        تخطي إلى المحتوى الرئيسي
    </a>
'''

added_count = 0
for p in html_files:
    if p.as_posix() == "index.html":
        continue # Already present
        
    c = p.read_text(encoding='utf-8')
    if '#main-content' in c:
        continue
        
    # Add skip link right after <body ...>
    body_match = re.search(r'<body[^>]*>', c)
    if body_match:
        end_idx = body_match.end()
        c = c[:end_idx] + skip_link_html + c[end_idx:]
        
        # Add id="main-content" to <main> or first <section> or container
        if '<main' in c and 'id="main-content"' not in c:
            c = re.sub(r'<main([^>]*)>', r'<main id="main-content"\1>', c, count=1)
        elif '<main' not in c:
            # find first <section>
            c = re.sub(r'<section([^>]*)>', r'<main id="main-content"><section\1>', c, count=1)
            # close before <footer>
            if '<footer' in c:
                c = re.sub(r'(<footer[^>]*>)', r'</main>\1', c, count=1)
            else:
                c = re.sub(r'(</body[^>]*>)', r'</main>\1', c, count=1)
                
        p.write_text(c, encoding='utf-8')
        added_count += 1

print(f"Added skip-to-content accessibility link to {added_count} subpages.")
