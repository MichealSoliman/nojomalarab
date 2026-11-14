import os
import re
import csv
from pathlib import Path
from bs4 import BeautifulSoup

def log(msg):
    with open("audit/run-log.txt", "a", encoding="utf-8") as f:
        f.write(f"[CLAIMS-PRICES-AUDIT] {msg}\n")
    print(msg)

log("Starting claims, facts, and prices audit...")

html_files = []
for p in Path(".").rglob("*.html"):
    rel = p.as_posix()
    if rel.startswith("audit/") or ".gemini" in rel:
        continue
    html_files.append(p)

CLAIM_PATTERNS = [
    ("24_HOURS", r"(24\s*ساعة|على\s*مدار\s*الساعة|خدمة\s*24)"),
    ("GUARANTEE", r"(ضمان\s*(100%|شامل|أكيد|معتمد)?|معتمدة|شركة\s*معتمدة)"),
    ("SUPERLATIVE_BEST", r"(أفضل\s*شركة|الشركة\s*الأولى|رائدة|الأرخص)"),
    ("FAST_MINUTES", r"(خلال\s*\d+\s*دقيقة|نصف\s*ساعة)"),
    ("DISCOUNT_PERCENT", r"(\b\d{1,2}\s*%\s*(خصم)?|خصم\s*\d{1,2}\s*%)"),
    ("YEARS_EXPERIENCE", r"(\b\d+\s*(سنوات|سنة)\s*خبرة|خبرة\s*\d+\s*(سنوات|سنة))"),
    ("ZERO_DAMAGE", r"(دون\s*(أي\s*)?(تأخير|أضرار|كسور|خدش))"),
    ("RATINGS_REVIEWS", r"(\b\d(\.\d)?\s*نجمة|تقييم\s*5|أكثر\s*من\s*\d+\s*عميل)")
]

PRICE_PATTERNS = [
    r"(\d+[\s\-]*(?:إلى|وحتى|–|-)?\s*\d*)\s*(?:ريال|ر\.س|SAR)",
    r"(?:سعر|تبدأ\s*من|ابتداءً\s*من)\s*(\d+)\s*(?:ريال|ر\.س|SAR)?"
]

claims_data = []
prices_data = []

for fpath in sorted(html_files):
    rel = fpath.as_posix()
    with open(fpath, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()
        
    soup = BeautifulSoup(content, "html.parser")
    # Remove script and style
    for tag in soup(["script", "style", "noscript"]):
        tag.extract()
        
    text_content = soup.get_text()
    
    # Check Phone, WhatsApp, Address consistency
    tels = re.findall(r"tel:([0-9+]+)", content)
    was = re.findall(r"wa\.me/([0-9+]+)", content)
    
    # Check Claims
    for claim_type, pat in CLAIM_PATTERNS:
        matches = list(re.finditer(pat, text_content, re.IGNORECASE))
        for m in matches:
            start = max(0, m.start() - 40)
            end = min(len(text_content), m.end() + 40)
            context = "..." + text_content[start:end].replace("\n", " ").strip() + "..."
            claims_data.append({
                "page": rel,
                "claim_type": claim_type,
                "matched_text": m.group(0),
                "context": context,
                "requires_proof": "نعم (بحاجة لإثبات أو صياغة آمنة)"
            })
            
    # Check Prices
    for pat in PRICE_PATTERNS:
        matches = list(re.finditer(pat, text_content, re.IGNORECASE))
        for m in matches:
            start = max(0, m.start() - 30)
            end = min(len(text_content), m.end() + 30)
            context = "..." + text_content[start:end].replace("\n", " ").strip() + "..."
            prices_data.append({
                "page": rel,
                "extracted_price": m.group(0),
                "context": context
            })

with open("audit/08-claims-and-facts.csv", "w", encoding="utf-8-sig", newline="") as f:
    if claims_data:
        writer = csv.DictWriter(f, fieldnames=claims_data[0].keys())
        writer.writeheader()
        writer.writerows(claims_data)
    else:
        f.write("page,claim_type,matched_text,context,requires_proof\n")

with open("audit/09-prices.csv", "w", encoding="utf-8-sig", newline="") as f:
    if prices_data:
        writer = csv.DictWriter(f, fieldnames=prices_data[0].keys())
        writer.writeheader()
        writer.writerows(prices_data)
    else:
        f.write("page,extracted_price,context\n")

log(f"Claims audit finished: {len(claims_data)} claims identified, {len(prices_data)} price mentions found.")

