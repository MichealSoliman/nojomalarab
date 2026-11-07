import glob
import re

html_files = [f.replace('\\', '/') for f in glob.glob('**/*.html', recursive=True) if not f.startswith('.git') and f != 'components/footer.html']

ga_snippet = '''    <!-- Google tag (gtag.js) -->
    <script async src="https://www.googletagmanager.com/gtag/js?id={{G-XXXXXXX}}"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());
      gtag('config', '{{G-XXXXXXX}}');
    </script>
    <script src="/assets/js/analytics.js" defer></script>'''

for filepath in sorted(html_files):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    orig = content
    
    # Check if GA snippet already exists
    if '{{G-XXXXXXX}}' not in content:
        # insert before </head>
        content = content.replace('</head>', f'{ga_snippet}\n</head>')
    elif '/assets/js/analytics.js' not in content:
        content = content.replace('</head>', '    <script src="/assets/js/analytics.js" defer></script>\n</head>')
        
    if content != orig:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'Added GA4 tag to {filepath}')

