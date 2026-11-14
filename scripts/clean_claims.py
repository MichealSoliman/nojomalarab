import os
import re
import csv
from pathlib import Path

html_files = [p for p in Path('.').rglob('*.html') if not str(p).startswith('audit') and '.gemini' not in str(p) and 'node_modules' not in p.as_posix() and 'components/' not in p.as_posix()]

patterns = [
    ("24_HOURS", r"(24\s*ساعة|على\s*مدار\s*الساعة|خدمة\s*24)", "خلال ساعات العمل الرسمية (السبت-الخميس: 9ص-9م)"),
    ("GUARANTEE", r"(ضمان\s*(100%|شامل|أكيد|معتمد)?|معتمدة|شركة\s*معتمدة)", "عناية فائقة وتعهد بالسلامة"),
    ("SUPERLATIVE", r"(أفضل\s*شركة|الشركة\s*الأولى|الرائدة|الأرخص)", "شركة موثوقة ومتميزة"),
    ("30_MINUTES", r"(خلال\s*30\s*دقيقة)", "بأعلى سرعة ممكنة وبجدولة منظمة"),
    ("HUNDRED_PERCENT", r"(100%)", "بأعلى معايير الجودة"),
    ("NO_DELAY", r"(دون\s*تأخير|بلا\s*تأخير)", "مع الحرص على الالتزام بالموعد المحدد"),
    ("NO_HIDDEN_FEES", r"(دون\s*مصاريف\s*خفية|بلا\s*تكاليف\s*خفية)", "بشفافية تامة في الأسعار")
]

claims_rows = []
total_cleaned = 0

for p in sorted(html_files):
    rel = p.as_posix()
    content = p.read_text(encoding='utf-8')
    orig = content
    lines = content.splitlines()
    
    for i, l in enumerate(lines):
        # Exclude legitimate context (e.g. storage temperature cooling 24/7 or defrosting fridge 24h before moving)
        if "افصل الثلاجة" in l or "تفريغ الثلاجات" in l or "تكييف وتجفيف" in l or "تبريد" in l:
            continue
            
        for c_type, pat, repl in patterns:
            # For "أفضل شركة", keep it in canonical URL or breadcrumb title if part of slug
            if "best-furniture-moving-company-jeddah" in l and c_type == "SUPERLATIVE":
                continue
                
            m = re.search(pat, l)
            if m:
                matched_text = m.group(0)
                new_line = re.sub(pat, repl, l)
                claims_rows.append({
                    'file': rel,
                    'line': i + 1,
                    'claim_type': c_type,
                    'old_text': matched_text,
                    'new_text': repl,
                    'context': l.strip()[:100]
                })
                lines[i] = new_line
                
    new_content = '\n'.join(lines)
    if new_content != orig:
        p.write_text(new_content, encoding='utf-8')
        total_cleaned += 1

print(f"Recorded and cleaned {len(claims_rows)} claims across {total_cleaned} files.")

with open("claims-report.csv", "w", encoding="utf-8-sig", newline="") as f:
    if claims_rows:
        writer = csv.DictWriter(f, fieldnames=claims_rows[0].keys())
        writer.writeheader()
        writer.writerows(claims_rows)
    else:
        f.write("file,line,claim_type,old_text,new_text,context\n")

print("Generated claims-report.csv successfully.")
