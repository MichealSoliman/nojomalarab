from pathlib import Path

# Fix privacy-policy.html
p_priv = Path('privacy-policy.html')
c_priv = p_priv.read_text(encoding='utf-8')

replacements = [
    ('href="./"', 'href="/"'),
    ('src="./assets/img/', 'src="/assets/img/'),
    ('src="./assets/js/', 'src="/assets/js/'),
    ('href="./about/"', 'href="/about/"'),
    ('href="./services/"', 'href="/services/"'),
    ('href="./office-furniture-moving-jeddah/"', 'href="/office-furniture-moving-jeddah/"'),
    ('href="./furniture-moving-prices-jeddah/"', 'href="/furniture-moving-prices-jeddah/"'),
    ('href="./blogs/"', 'href="/blogs/"'),
    ('href="./#whyus"', 'href="/#whyus"'),
    ('href="./#faq"', 'href="/#faq"'),
    ('href="./contact/"', 'href="/contact/"'),
    ('href="./#contact"', 'href="/#contact"'),
]

for old, new in replacements:
    c_priv = c_priv.replace(old, new)
p_priv.write_text(c_priv, encoding='utf-8')

# Fix terms.html
p_terms = Path('terms.html')
c_terms = p_terms.read_text(encoding='utf-8')

for old, new in replacements:
    c_terms = c_terms.replace(old, new)
p_terms.write_text(c_terms, encoding='utf-8')

print("Fixed relative paths in privacy-policy.html and terms.html successfully.")
