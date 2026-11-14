import os
import re
import csv
from pathlib import Path
from bs4 import BeautifulSoup
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def log(msg):
    with open("audit/run-log.txt", "a", encoding="utf-8") as f:
        f.write(f"[KEYWORDS-DUPES] {msg}\n")
    print(msg)

log("Starting keywords and duplication audit...")

html_files = []
for p in Path(".").rglob("*.html"):
    rel = p.as_posix()
    if rel.startswith("audit/") or ".gemini" in rel:
        continue
    html_files.append(p)

KEYWORDS_TO_TRACK = [
    "شركة نقل عفش جدة",
    "نقل عفش جدة",
    "نقل اثاث جدة",
    "نقل عفش بجدة",
    "دينا نقل عفش",
    "دينا نقل عفش جدة",
    "اسعار نقل العفش",
    "افضل شركة نقل عفش",
    "ارخص شركة نقل عفش",
    "ونش رفع عفش",
    "تغليف اثاث",
    "فك وتركيب اثاث"
]

page_keywords_map = []
page_main_texts = {}

for fpath in sorted(html_files):
    rel = fpath.as_posix()
    with open(fpath, "r", encoding="utf-8", errors="ignore") as f:
        soup = BeautifulSoup(f.read(), "html.parser")
        
    # Remove boilerplate elements (header, footer, nav, script, style) to measure pure content duplication
    for tag in soup(["header", "footer", "nav", "script", "style", "noscript", "svg"]):
        tag.extract()
        
    main_text = re.sub(r"\s+", " ", soup.get_text()).strip()
    page_main_texts[rel] = main_text
    word_count = len(main_text.split())
    
    # Check frequencies
    counts = {}
    for kw in KEYWORDS_TO_TRACK:
        # Match with or without hamzas / alif variants
        pattern = re.escape(kw)
        pattern = pattern.replace("أ", "[أاإآ]").replace("ا", "[أاإآ]").replace("إ", "[أاإآ]")
        pattern = pattern.replace("ة", "[ةه]").replace("ه", "[ةه]")
        cnt = len(re.findall(pattern, main_text, re.IGNORECASE))
        density = round((cnt * len(kw.split()) / max(1, word_count)) * 100, 2)
        counts[kw] = (cnt, density)
        
    for kw, (c, d) in counts.items():
        if c > 0:
            page_keywords_map.append({
                "page": rel,
                "keyword": kw,
                "occurrences": c,
                "density_percent": d,
                "total_words": word_count,
                "risk_stuffing": "HIGH" if d > 3.0 else ("MODERATE" if d > 1.5 else "SAFE")
            })

# Save 10-keywords-map.csv
with open("audit/10-keywords-map.csv", "w", encoding="utf-8-sig", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=page_keywords_map[0].keys())
    writer.writeheader()
    writer.writerows(page_keywords_map)
log(f"Keywords map written ({len(page_keywords_map)} entries)")

# Compute TF-IDF Cosine Similarity across main texts
pages_list = list(page_main_texts.keys())
corpus = [page_main_texts[p] for p in pages_list]

vectorizer = TfidfVectorizer(token_pattern=r"(?u)\b\w+\b")
tfidf_matrix = vectorizer.fit_transform(corpus)
sim_matrix = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Compute 5-gram Jaccard Similarity
def get_ngrams(text, n=5):
    words = text.split()
    if len(words) < n:
        return set()
    return set(" ".join(words[i:i+n]) for i in range(len(words)-n+1))

page_5grams = {p: get_ngrams(page_main_texts[p], 5) for p in pages_list}

duplicates_rows = []
n_pages = len(pages_list)

for i in range(n_pages):
    for j in range(i + 1, n_pages):
        p1 = pages_list[i]
        p2 = pages_list[j]
        cos_sim = round(float(sim_matrix[i, j]) * 100, 2)
        
        set1 = page_5grams[p1]
        set2 = page_5grams[p2]
        inter = len(set1.intersection(set2))
        union = len(set1.union(set2))
        jaccard = round((inter / union * 100), 2) if union > 0 else 0.0
        
        # We record anything with cosine similarity >= 40% or Jaccard >= 25%
        if cos_sim >= 40.0 or jaccard >= 25.0:
            severity = "CRITICAL" if (cos_sim >= 75.0 or jaccard >= 50.0) else "HIGH"
            
            # Find verbatim overlap excerpt if possible
            common = list(set1.intersection(set2))
            sample_overlap = common[0] if common else "N/A"
            
            duplicates_rows.append({
                "page_a": p1,
                "page_b": p2,
                "cosine_similarity_pct": cos_sim,
                "jaccard_5gram_pct": jaccard,
                "severity": severity,
                "sample_overlap_5gram": sample_overlap
            })

duplicates_rows.sort(key=lambda x: x["cosine_similarity_pct"], reverse=True)

with open("audit/11-duplicates.csv", "w", encoding="utf-8-sig", newline="") as f:
    if duplicates_rows:
        writer = csv.DictWriter(f, fieldnames=duplicates_rows[0].keys())
        writer.writeheader()
        writer.writerows(duplicates_rows)
    else:
        f.write("page_a,page_b,cosine_similarity_pct,jaccard_5gram_pct,severity,sample_overlap_5gram\n")

log(f"Duplication analysis finished. {len(duplicates_rows)} pairs identified above threshold.")

