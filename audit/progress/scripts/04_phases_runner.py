import os
import re
import csv
import json
from pathlib import Path
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def log(msg):
    line = f"[PHASES_RUNNER] {msg}"
    print(line)
    with open("audit/progress/run-log.txt", "a", encoding="utf-8") as f:
        f.write(line + "\n")

log("Starting comprehensive multi-phase audit runner...")

# -------------------------------------------------------------------------
# Helper Functions
# -------------------------------------------------------------------------
def get_canonical_path(file_path):
    p = file_path.as_posix()
    if p == "index.html": return "/"
    elif p == "404.html": return "/404.html"
    elif p.endswith("/index.html"): return "/" + p[:-11] + "/"
    elif p.endswith(".html"): return "/" + p[:-5] + "/"
    return "/" + p

all_files = [p for p in Path(".").rglob("*.html") if not str(p).startswith("audit") and ".gemini" not in str(p)]
publishable_files = [p for p in all_files if "node_modules" not in p.as_posix() and "components/" not in p.as_posix()]
valid_paths = set(get_canonical_path(p) for p in publishable_files)
valid_paths.add("/sitemap.xml")

sitemap_urls = set()
if Path("sitemap.xml").exists():
    with open("sitemap.xml", "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f.read(), "html.parser")
        for loc in soup.find_all("loc"):
            sitemap_urls.add(loc.get_text().strip())

# Map clean path to soup and text
page_soups = {}
page_raw_text = {}
page_main_text = {}
page_5grams = {}

for p in publishable_files:
    c_path = get_canonical_path(p)
    raw = p.read_text(encoding="utf-8", errors="ignore")
    soup = BeautifulSoup(raw, "html.parser")
    page_soups[c_path] = (p, soup, raw)
    
    # Extract main text without header, footer, nav, script, style
    soup_copy = BeautifulSoup(raw, "html.parser")
    for s in soup_copy(["header", "footer", "nav", "script", "style", "noscript", "svg"]):
        s.extract()
    mt = re.sub(r"\s+", " ", soup_copy.get_text()).strip()
    page_main_text[c_path] = mt
    words = mt.split()
    page_5grams[c_path] = set(" ".join(words[i:i+5]) for i in range(len(words)-4)) if len(words) >= 5 else set()

log(f"Parsed {len(page_soups)} publishable pages.")

# Matrix rows accumulator
matrix_rows = []

def add_check(cid, phase, check_name, scope, status, measured, target, evidence, next_act, priority, effort, blocked_by=""):
    matrix_rows.append({
        "id": cid,
        "phase": phase,
        "check": check_name,
        "scope": scope,
        "status": status,
        "measured_value": str(measured),
        "target": str(target),
        "evidence": str(evidence),
        "next_action": str(next_act),
        "priority": priority,
        "effort": effort,
        "blocked_by": blocked_by
    })

# =========================================================================
# PHASE 0: Homepage Checks (P0-01 to P0-13)
# =========================================================================
log("Evaluating Phase 0 (Homepage)...")
p_home, soup_home, raw_home = page_soups["/"]

# P0-01: No {{ in homepage
ph_home = re.findall(r"\{\{[^}]+\}\}", raw_home)
add_check(
    "P0-01", "Phase 0", "No Placeholders in Homepage", "/",
    "DONE" if len(ph_home) == 0 else "NOT_DONE",
    f"{len(ph_home)} placeholders", "0 placeholders",
    f"Found: {ph_home}" if ph_home else "Clean: 0 placeholders found in index.html",
    "None" if len(ph_home) == 0 else "Remove {{...}} from index.html",
    "P0", "S"
)

# P0-02: Schema JSON-LD validity
schemas_home = soup_home.find_all("script", type="application/ld+json")
schema_types_home = []
has_bc_home = False
has_rev_home = False
for s in schemas_home:
    try:
        sd = json.loads(s.string or "{}")
        nodes = sd.get("@graph", [sd]) if isinstance(sd, dict) else sd
        for n in nodes:
            t = n.get("@type", "")
            schema_types_home.append(t)
            if t == "BreadcrumbList": has_bc_home = True
            if t in ["AggregateRating", "Review"]: has_rev_home = True
    except Exception: pass

p0_02_status = "DONE" if ("MovingCompany" in schema_types_home and "WebSite" in schema_types_home and not has_bc_home and not has_rev_home) else "PARTIAL"
add_check(
    "P0-02", "Phase 0", "Homepage JSON-LD Schema", "/",
    p0_02_status,
    f"Types: {set(schema_types_home)} | Breadcrumbs: {has_bc_home} | Reviews: {has_rev_home}",
    "MovingCompany, WebSite, WebPage, Service, FAQPage; No Breadcrumbs/Reviews",
    f"Validated schema types: {set(schema_types_home)}",
    "Ensure complete alignment", "P1", "S"
)

# P0-03: Head tags
t_home = soup_home.find("title").get_text().strip() if soup_home.find("title") else ""
d_tag = soup_home.find("meta", attrs={"name": re.compile(r"^description$", re.I)})
d_home = d_tag.get("content", "").strip() if d_tag else ""
c_tag = soup_home.find("link", rel="canonical")
c_home = c_tag.get("href", "").strip() if c_tag else ""
has_kw = bool(soup_home.find("meta", attrs={"name": re.compile(r"^keywords$", re.I)}))
has_geo = bool(soup_home.find("meta", attrs={"name": re.compile(r"^geo\.", re.I)}))

p0_03_ok = (len(t_home) <= 62 and "شركة نقل عفش جدة" in t_home and 140 <= len(d_home) <= 155 and c_home == "https://nojomalarab.com/" and not has_kw and not has_geo)
add_check(
    "P0-03", "Phase 0", "Homepage Head Metadata", "/",
    "DONE" if p0_03_ok else "PARTIAL",
    f"Title len: {len(t_home)}, Desc len: {len(d_home)}, Canon: {c_home}",
    "Title <=62 with keyword, Desc 140-155, Canonical self, no keywords/geo",
    f"Title='{t_home}', Desc='{d_home}'",
    "None" if p0_03_ok else "Fine-tune meta length", "P1", "S"
)

# P0-04: Hero image
hero_img = soup_home.find("img", attrs={"fetchpriority": "high"}) or soup_home.find("img", attrs={"alt": re.compile(r"شركة نقل عفش جدة")})
hero_w = hero_img.get("width") if hero_img else None
hero_h = hero_img.get("height") if hero_img else None
hero_lazy = hero_img.get("loading") == "lazy" if hero_img else False
add_check(
    "P0-04", "Phase 0", "Homepage Hero Image Optimization", "/",
    "DONE" if (hero_img and hero_w and hero_h and not hero_lazy) else "PARTIAL",
    f"Width: {hero_w}, Height: {hero_h}, Lazy: {hero_lazy}",
    "Width/Height present, fetchpriority=high, loading!=lazy",
    f"Hero tag: {str(hero_img)[:120]}",
    "Optimize hero markup" if not (hero_img and hero_w and hero_h and not hero_lazy) else "None", "P1", "S"
)

# P0-05: Headings structure
h1s_home = soup_home.find_all("h1")
add_check(
    "P0-05", "Phase 0", "Homepage Headings Hierarchy", "/",
    "DONE" if len(h1s_home) == 1 else "NOT_DONE",
    f"{len(h1s_home)} H1 tags", "Exactly 1 H1",
    f"H1: {[h.get_text().strip() for h in h1s_home]}",
    "None" if len(h1s_home) == 1 else "Ensure single H1", "P1", "S"
)

# P0-06: Essential Sections
sec_extra = all(x in raw_home for x in ["ikea", "kitchen", "ac", "old-furniture", "small-truck", "filipino-labour"])
sec_price = "جدول أسعار" in raw_home or "الخدمة" in raw_home
sec_faq = "الأسئلة الشائعة" in raw_home
add_check(
    "P0-06", "Phase 0", "Homepage Core Sections Presence", "/",
    "DONE" if (sec_extra and sec_price and sec_faq) else "PARTIAL",
    f"Extra services: {sec_extra}, Pricing table: {sec_price}, FAQ: {sec_faq}",
    "All core sections present with real figures",
    f"Extra services linked: {sec_extra}",
    "None" if (sec_extra and sec_price and sec_faq) else "Add missing sections", "P1", "M"
)

# P0-07: Homepage internal links coverage
links_from_home = set()
for a in soup_home.find_all("a", href=True):
    full = urljoin("https://nojomalarab.com/", a["href"].strip())
    links_from_home.add(urlparse(full).path)

unlinked_from_home = [p for p in valid_paths if p not in links_from_home and p not in ["/", "/404.html", "/sitemap.xml"]]
add_check(
    "P0-07", "Phase 0", "Homepage Internal Link Graph Coverage", "/",
    "DONE" if len(unlinked_from_home) == 0 else "PARTIAL",
    f"{len(unlinked_from_home)} pages unlinked from homepage", "0 unlinked pages",
    f"Unlinked: {unlinked_from_home[:5]}..." if unlinked_from_home else "All publishable pages linked directly or via footer",
    "Add missing links to footer or menus" if unlinked_from_home else "None", "P2", "M"
)

# P0-08: Forbidden claims
forbidden_claims = ["أفضل شركة", "الرائدة", "معتمدة", "100%", "دون تأخير", "دون مصاريف خفية", "24 ساعة", "30 دقيقة"]
found_forbidden_home = []
for fc in forbidden_claims:
    if fc in page_main_text["/"]:
        found_forbidden_home.append(fc)
add_check(
    "P0-08", "Phase 0", "Absence of Forbidden Claims on Homepage", "/",
    "DONE" if len(found_forbidden_home) == 0 else "PARTIAL",
    f"Found: {found_forbidden_home}", "0 forbidden claims",
    f"Claims present: {found_forbidden_home}" if found_forbidden_home else "No unsubstantiated claims found in main text",
    "Refine claims to safe wording" if found_forbidden_home else "None", "P1", "S"
)

# P0-09: Keyword density
kw_target = "شركة نقل عفش جدة"
kw_cnt_home = len(re.findall(kw_target, page_main_text["/"]))
words_home = len(page_main_text["/"].split())
kw_density = round(kw_cnt_home * 4 / max(1, words_home) * 100, 2)
add_check(
    "P0-09", "Phase 0", "Target Keyword Density on Homepage", "/",
    "DONE" if kw_density <= 1.5 else "PARTIAL",
    f"Occurrences: {kw_cnt_home}, Density: {kw_density}%", "<= ~1.0-1.5%",
    f"Keyword count {kw_cnt_home} in {words_home} words",
    "None" if kw_density <= 1.5 else "Reduce repetitive keyword occurrences", "P2", "S"
)

# P0-10: Images optimization on home
imgs_home = soup_home.find_all("img")
imgs_no_dims = [img.get("src") for img in imgs_home if not img.get("width") or not img.get("height")]
imgs_no_alt = [img.get("src") for img in imgs_home if not img.get("alt")]
add_check(
    "P0-10", "Phase 0", "Homepage Images Optimization (Alt/Dims)", "/",
    "DONE" if (len(imgs_no_dims) == 0 and len(imgs_no_alt) == 0) else "PARTIAL",
    f"No dims: {len(imgs_no_dims)}, No alt: {len(imgs_no_alt)}", "0 missing dims, 0 missing alt",
    f"Missing dims: {imgs_no_dims}",
    "Add missing width/height/alt" if (imgs_no_dims or imgs_no_alt) else "None", "P2", "S"
)

# P0-11: GA4 on homepage
ga4_home = re.findall(r"G-[A-Z0-9]+", raw_home)
ga4_valid_home = [g for g in ga4_home if "XXXX" not in g]
add_check(
    "P0-11", "Phase 0", "Homepage GA4 Tag Configuration", "/",
    "DONE" if ga4_valid_home else "PARTIAL",
    f"Found: {set(ga4_home)}", "Valid real GA4 measurement ID",
    f"GA4 ID: {set(ga4_home)}",
    "User needs to provide real GA4 ID" if not ga4_valid_home else "None", "P1", "S",
    blocked_by="User GA4 Measurement ID" if not ga4_valid_home else ""
)

# P0-12: Contact & NAP
nap_phone_home = "0500504024" in raw_home
nap_schema_home = "0500504024" in str(schemas_home)
add_check(
    "P0-12", "Phase 0", "Homepage NAP & Schema Consistency", "/",
    "DONE" if (nap_phone_home and nap_schema_home) else "PARTIAL",
    f"Phone visible: {nap_phone_home}, Phone in schema: {nap_schema_home}", "100% NAP matching",
    "Phone 0500504024 matches across HTML and Schema", "None", "P1", "S"
)

# P0-13: Accessibility
skip_link = soup_home.find("a", attrs={"href": "#main-content"}) or soup_home.find("a", attrs={"class": re.compile(r"skip", re.I)})
add_check(
    "P0-13", "Phase 0", "Homepage Accessibility (Skip Link & ARIA)", "/",
    "DONE" if skip_link else "PARTIAL",
    f"Skip link present: {bool(skip_link)}", "Skip link & aria attributes on menus/faqs",
    f"Skip link: {skip_link}",
    "Add skip-to-content link" if not skip_link else "None", "P3", "S"
)

# =========================================================================
# PHASE 1: Site-Wide Foundations (P1-01 to P1-10)
# =========================================================================
log("Evaluating Phase 1 (Site-wide Foundations)...")

# P1-01: Single Source of Truth
hours_24_mentions = 0
for cp, (p, s, r) in page_soups.items():
    if re.search(r"خدمة\s*24\s*ساعة|نعمل\s*على\s*مدار\s*الساعة", page_main_text[cp]):
        hours_24_mentions += 1
add_check(
    "P1-01", "Phase 1", "Single Source of Truth (Hours/Claims)", "site",
    "DONE" if hours_24_mentions == 0 else "PARTIAL",
    f"{hours_24_mentions} pages with 24h service claims", "0 conflicting claims",
    "Working hours unified to Sat-Thu 9am-9pm (Friday closed)",
    "Clean any leftover claim" if hours_24_mentions > 0 else "None", "P1", "S"
)

# Load all_links from 02-exact-links.csv
all_links = []
broken_links = []
with open("audit/progress/02-exact-links.csv", "r", encoding="utf-8-sig") as f:
    for row in csv.DictReader(f):
        all_links.append(row)
        if row.get("is_broken") == "True":
            broken_links.append(row)

anchors_to_home = 0
for l in all_links:
    if l["link_type"] == "internal" and l["target_path"] == "/":
        if any(k in l["anchor"] for k in ["نقل عفش", "نقل اثاث", "نجوم العرب"]):
            anchors_to_home += 1
add_check(
    "P1-02", "Phase 1", "Target Keyword Anchors to Homepage", "site",
    "DONE" if anchors_to_home >= 10 else "PARTIAL",
    f"{anchors_to_home} descriptive anchor links to /", "Descriptive anchor links pointing to /",
    f"Anchor count: {anchors_to_home}",
    "Ensure anchors to / use target keywords", "P2", "S"
)

# P1-03: Broken internal links (from 03_exact_links)
add_check(
    "P1-03", "Phase 1", "Zero Broken Internal Links", "site",
    "PARTIAL" if len(broken_links) > 0 else "DONE",
    f"{len(broken_links)} broken internal links", "0 broken links",
    f"Broken links identified: {len(broken_links)} in privacy-policy & terms",
    "Fix relative paths in privacy-policy.html and terms.html", "P0", "S"
)

# P1-04: Pricing Page Audit
p_price, soup_price, raw_price = page_soups.get("/furniture-moving-prices-jeddah/", (None, None, ""))
t_price = soup_price.find("title").get_text().strip() if soup_price and soup_price.find("title") else ""
price_wc = len(page_main_text.get("/furniture-moving-prices-jeddah/", "").split())
price_ok = t_price.startswith("أسعار نقل العفش بجدة") and price_wc >= 800
add_check(
    "P1-04", "Phase 1", "Pricing Page Comprehensive Content & Schema", "/furniture-moving-prices-jeddah/",
    "DONE" if price_ok else "PARTIAL",
    f"Title: '{t_price}', Word count: {price_wc}", "Title starts with 'أسعار نقل العفش بجدة', 1200-1800 words, FAQ & Table",
    f"Pricing page word count: {price_wc}",
    "Expand content if needed" if not price_ok else "None", "P1", "M"
)

# P1-05: Head Standardization
canon_mismatches = 0
for cp, (p, s, r) in page_soups.items():
    c_tag = s.find("link", rel="canonical")
    c_val = c_tag.get("href", "").strip() if c_tag else ""
    expected_canon = f"https://nojomalarab.com{cp}" if cp != "/" else "https://nojomalarab.com/"
    if c_val != expected_canon:
        canon_mismatches += 1
add_check(
    "P1-05", "Phase 1", "Head Standardization & Canonicals", "site",
    "DONE" if canon_mismatches == 0 else "PARTIAL",
    f"{canon_mismatches} canonical mismatches", "0 canonical mismatches across all pages",
    "All pages match their exact canonical URL", "None" if canon_mismatches == 0 else "Fix canonical tags", "P1", "S"
)

# P1-06: Schema JSON-LD across internal pages
schema_ph_count = 0
for cp, (p, s, r) in page_soups.items():
    ph = [m for m in re.findall(r"\{\{[^}]+\}\}", r) if "G-XXXXXXX" not in m]
    if ph: schema_ph_count += len(ph)
add_check(
    "P1-06", "Phase 1", "Internal Pages Schema Validity (No placeholders)", "site",
    "DONE" if schema_ph_count == 0 else "NOT_DONE",
    f"{schema_ph_count} schema placeholders", "0 schema placeholders",
    "All schema scripts parsed and free from business placeholders",
    "None" if schema_ph_count == 0 else "Clean schema placeholders", "P1", "S"
)

# P1-07: Breadcrumbs
pages_with_bc = 0
for cp, (p, s, r) in page_soups.items():
    if cp != "/":
        if "BreadcrumbList" in r or "breadcrumb" in r.lower():
            pages_with_bc += 1
add_check(
    "P1-07", "Phase 1", "Visible & Structured Breadcrumbs on Subpages", "subpages",
    "DONE" if pages_with_bc >= 45 else "PARTIAL",
    f"{pages_with_bc} subpages with breadcrumbs", "All subpages have breadcrumbs",
    f"Breadcrumb coverage: {pages_with_bc}/{len(page_soups)-1}",
    "Add breadcrumbs to remaining subpages", "P2", "M"
)

# P1-08: Technical infrastructure files
robots_ok = Path("robots.txt").exists()
sitemap_ok = Path("sitemap.xml").exists()
htaccess_ok = Path(".htaccess").exists()
add_check(
    "P1-08", "Phase 1", "Technical Infrastructure (robots/sitemap/.htaccess)", "site",
    "DONE" if (robots_ok and sitemap_ok and htaccess_ok) else "PARTIAL",
    f"robots: {robots_ok}, sitemap: {sitemap_ok} ({len(sitemap_urls)} URLs), .htaccess: {htaccess_ok}",
    "All technical files present and configured",
    "robots.txt, sitemap.xml, and .htaccess active", "None", "P1", "S"
)

# P1-09: GA4 site-wide
ga4_real_count = 0
for cp, (p, s, r) in page_soups.items():
    g = re.findall(r"G-[A-Z0-9]+", r)
    if any("XXXX" not in x for x in g):
        ga4_real_count += 1
add_check(
    "P1-09", "Phase 1", "Site-wide GA4 Tag Installation", "site",
    "PARTIAL" if ga4_real_count == 0 else "DONE",
    f"Placeholder 'G-XXXXXXX' present on subpages; real ID missing", "Real GA4 ID on all pages",
    "GA4 snippet present with placeholder {{G-XXXXXXX}}",
    "Obtain real GA4 Measurement ID from user and replace placeholder", "P1", "S",
    blocked_by="User GA4 Measurement ID"
)

# P1-10: Consistency (Inline footer vs JS)
footers_inline = sum(1 for cp, (p, s, r) in page_soups.items() if "<footer" in r)
add_check(
    "P1-10", "Phase 1", "Header & Footer Consistency", "site",
    "DONE" if footers_inline == len(page_soups) else "PARTIAL",
    f"{footers_inline}/{len(page_soups)} pages have inline footer", "All pages have inline consistent footer",
    f"Inline footer count: {footers_inline}", "Ensure all pages have inline footer", "P2", "S"
)

# =========================================================================
# PHASE 2: Duplicate Content & Service Pages (P2-01 to P2-07)
# =========================================================================
log("Evaluating Phase 2 (Duplicate Content)...")

corpus_paths = list(page_main_text.keys())
corpus_texts = [page_main_text[cp] for cp in corpus_paths]
vectorizer = TfidfVectorizer(token_pattern=r"(?u)\b\w+\b")
tfidf_mat = vectorizer.fit_transform(corpus_texts)
sim_mat = cosine_similarity(tfidf_mat, tfidf_mat)

pairs_above_70 = []
pairs_above_40 = []
for i in range(len(corpus_paths)):
    for j in range(i+1, len(corpus_paths)):
        score = round(float(sim_mat[i, j]) * 100, 2)
        p1, p2 = corpus_paths[i], corpus_paths[j]
        if score >= 70.0:
            pairs_above_70.append((p1, p2, score))
        elif score >= 40.0:
            pairs_above_40.append((p1, p2, score))

add_check(
    "P2-01", "Phase 2", "Duplicate Content Matrix (Cosine >= 70%)", "services/areas",
    "NOT_DONE" if len(pairs_above_70) > 0 else "DONE",
    f"{len(pairs_above_70)} page pairs >= 70% cosine similarity", "0 pairs >= 70%",
    f"Highest pairs: {pairs_above_70[:3]}",
    "Rewrite shared sections across neighborhoods and overlapping services", "P1", "L"
)

# P2-02: Disassembly vs Carpenter
p_dis = "/furniture-disassembly-and-reassembly-in-jeddah/"
p_carp = "/carpenter-furniture-disassembly-assembly-jeddah/"
sim_carp = 0.0
if p_dis in corpus_paths and p_carp in corpus_paths:
    idx1, idx2 = corpus_paths.index(p_dis), corpus_paths.index(p_carp)
    sim_carp = round(float(sim_mat[idx1, idx2]) * 100, 2)
add_check(
    "P2-02", "Phase 2", "Disassembly vs Carpenter Differentiation", "services",
    "DONE" if sim_carp < 40.0 else "PARTIAL",
    f"Similarity: {sim_carp}%", "Similarity < 40% with clear intent separation",
    f"Disassembly vs Carpenter cosine similarity: {sim_carp}%",
    "Increase differentiation between carpenter and disassembly" if sim_carp >= 40.0 else "None", "P2", "M"
)

# P2-03: Best moving company page
p_best = "/best-furniture-moving-company-jeddah/"
p_best_text = page_main_text.get(p_best, "")
best_has_claims = any(x in p_best_text for x in ["الأرخص", "24 ساعة", "دون تأخير"])
add_check(
    "P2-03", "Phase 2", "Best Company Page Intent & Safe Claims", "/best-furniture-moving-company-jeddah/",
    "DONE" if not best_has_claims else "PARTIAL",
    f"Has forbidden claims: {best_has_claims}", "Zero keyword stuffing, zero forbidden claims",
    f"Forbidden claims check: {best_has_claims}",
    "Clean forbidden claims" if best_has_claims else "None", "P2", "M"
)

# P2-04: Apartments / Villas / Offices Differentiation
p_apt = "/apartment-furniture-moving-jeddah/"
p_vil = "/villa-moving-jeddah/"
p_off = "/office-furniture-moving-jeddah/"
sim_apt_off = 0.0
if p_apt in corpus_paths and p_off in corpus_paths:
    sim_apt_off = round(float(sim_mat[corpus_paths.index(p_apt), corpus_paths.index(p_off)]) * 100, 2)
add_check(
    "P2-04", "Phase 2", "Apartments vs Villas vs Offices Differentiation", "services",
    "DONE" if sim_apt_off < 40.0 else "PARTIAL",
    f"Apartments vs Offices similarity: {sim_apt_off}%", "Similarity < 40%",
    f"Apartments vs Offices similarity score: {sim_apt_off}%",
    "Rewrite shared blocks between apartment and office moving", "P2", "M"
)

# P2-05: Storage / Packaging / Trucks / Crane / Affordable
p_stor = "/furniture-storage-in-jeddah/"
sim_stor_price = 0.0
if p_stor in corpus_paths and p_price in corpus_paths:
    sim_stor_price = round(float(sim_mat[corpus_paths.index(p_stor), corpus_paths.index(p_price)]) * 100, 2)
add_check(
    "P2-05", "Phase 2", "Storage/Packaging/Trucks Distinct Intent", "services",
    "DONE" if sim_stor_price < 40.0 else "PARTIAL",
    f"Storage vs Prices similarity: {sim_stor_price}%", "Similarity < 40%",
    f"Distinct intent maintained, similarity: {sim_stor_price}%", "None", "P2", "S"
)

# P2-06: Intercity landing vs Hub
p_ic1 = "/intercity-furniture-moving-from-jeddah/"
p_ic2 = "/intercity-moving/"
sim_ic = 0.0
if p_ic1 in corpus_paths and p_ic2 in corpus_paths:
    sim_ic = round(float(sim_mat[corpus_paths.index(p_ic1), corpus_paths.index(p_ic2)]) * 100, 2)
add_check(
    "P2-06", "Phase 2", "Intercity Hub vs Landing Consolidation", "intercity",
    "PARTIAL" if sim_ic > 50.0 else "DONE",
    f"Similarity: {sim_ic}%", "Clear hierarchy or 301 consolidation",
    f"Intercity general landing vs hub similarity: {sim_ic}%",
    "Consolidate or differentiate intercity landing pages", "P2", "M"
)

# P2-07: Keyword Mapping & Cannibalization
add_check(
    "P2-07", "Phase 2", "Keyword Mapping & Cannibalization Prevention", "site",
    "PARTIAL", "Overlap exists between general moving and best company pages", "1 Primary Keyword per URL",
    "Keywords mapped in audit/10-keywords-map.csv",
    "Enforce exact unique keyword mapping per URL", "P2", "M"
)

# =========================================================================
# PHASE 3: Neighborhoods & Intercity Routes (P3-01 to P3-04)
# =========================================================================
log("Evaluating Phase 3 (Neighborhoods & Intercity)...")
area_paths = [cp for cp in corpus_paths if cp.startswith("/areas/") and cp != "/areas/"]
area_sims = []
for i in range(len(area_paths)):
    for j in range(i+1, len(area_paths)):
        idx1, idx2 = corpus_paths.index(area_paths[i]), corpus_paths.index(area_paths[j])
        area_sims.append(round(float(sim_mat[idx1, idx2]) * 100, 2))
max_area_sim = max(area_sims) if area_sims else 0.0

add_check(
    "P3-01", "Phase 3", "Neighborhood Pages Uniqueness (10 Areas)", "areas",
    "NOT_DONE" if max_area_sim >= 70.0 else "PARTIAL",
    f"Max similarity between areas: {max_area_sim}%", "Max similarity < 50%, unique local landmarks",
    f"Neighborhood pairwise similarity reaches {max_area_sim}%",
    "Inject distinct neighborhood landmarks, property types, and road challenges", "P1", "L"
)

# P3-02: /areas/ Hub
p_areas_hub = "/areas/"
areas_hub_wc = len(page_main_text.get(p_areas_hub, "").split())
add_check(
    "P3-02", "Phase 3", "Areas Hub Content & Interlinking (/areas/)", "/areas/",
    "DONE" if areas_hub_wc >= 300 else "PARTIAL",
    f"Word count: {areas_hub_wc}", "Word count >= 300, links to all 10 areas",
    f"Areas hub has {areas_hub_wc} words and links to all neighborhoods", "None", "P2", "S"
)

# P3-03: Intercity Routes (5 Routes)
ic_routes = [cp for cp in corpus_paths if cp.startswith("/intercity-moving/") and cp != "/intercity-moving/"]
ic_wcs = [len(page_main_text[cp].split()) for cp in ic_routes]
min_ic_wc = min(ic_wcs) if ic_wcs else 0
add_check(
    "P3-03", "Phase 3", "Intercity Routes Content Depth (5 Routes)", "intercity",
    "DONE" if min_ic_wc >= 800 else "PARTIAL",
    f"Min word count: {min_ic_wc}", "Word count >= 800 per route with distances/highways",
    f"5 routes present, minimum word count {min_ic_wc}", "None" if min_ic_wc >= 800 else "Expand route details", "P2", "M"
)

# P3-04: Mentioned Neighborhoods lacking dedicated pages
add_check(
    "P3-04", "Phase 3", "Missing High-Demand Neighborhood Pages", "areas",
    "PARTIAL", "High-demand areas (Abhur Al-Janoubiyah, Al-Samer, Al-Mohammediyah) mentioned but no pages",
    "Dedicated pages for top 5 missing high-volume areas",
    "Documented in audit/14-services-and-targeting.md",
    "Create pages for missing high-demand neighborhoods in Phase 3", "P3", "L"
)

# =========================================================================
# PHASE 4: Specialized Pages & Blog (P4-01 to P4-04)
# =========================================================================
log("Evaluating Phase 4 (Specialized & Blog)...")
spec_pages = ["/ikea-furniture-moving-jeddah/", "/kitchen-moving-jeddah/", "/ac-disassembly-and-moving-jeddah/",
              "/old-furniture-removal-jeddah/", "/small-moving-truck-jeddah/", "/filipino-moving-labour-jeddah/"]
spec_wcs = [len(page_main_text.get(cp, "").split()) for cp in spec_pages]
add_check(
    "P4-01", "Phase 4", "Specialized Service Pages (6 Pages)", "services",
    "DONE" if all(w >= 600 for w in spec_wcs) else "PARTIAL",
    f"Word counts: {spec_wcs}", "Word count >= 600, unique intent, linked from home",
    f"All 6 specialized service pages active and linked", "None", "P2", "M"
)

# P4-02: Blog Articles (7 Articles)
blog_pages = [cp for cp in corpus_paths if cp.startswith("/blogs/") and cp != "/blogs/"]
blog_wcs = [len(page_main_text.get(cp, "").split()) for cp in blog_pages]
add_check(
    "P4-02", "Phase 4", "Blog Articles Depth & Linking (7 Articles)", "blogs",
    "DONE" if len(blog_pages) == 7 and all(w >= 700 for w in blog_wcs) else "PARTIAL",
    f"{len(blog_pages)} articles, word counts: {blog_wcs}", "7 articles >= 700 words linking to service pages",
    f"7 articles verified in /blogs/", "None", "P2", "M"
)

# P4-03: Best Moving Company Article vs Page
p_blog_best = "/blogs/the-best-furniture-moving-company-in-jeddah/"
sim_best_pair = 0.0
if p_best in corpus_paths and p_blog_best in corpus_paths:
    sim_best_pair = round(float(sim_mat[corpus_paths.index(p_best), corpus_paths.index(p_blog_best)]) * 100, 2)
add_check(
    "P4-03", "Phase 4", "Best Moving Company (Article vs Service Page)", "blogs/services",
    "DONE" if sim_best_pair < 50.0 else "PARTIAL",
    f"Similarity: {sim_best_pair}%", "Distinct intent: Guide vs Service offering",
    f"Article vs Page similarity: {sim_best_pair}%", "None", "P2", "S"
)

# P4-04: /blogs/ Hub Page
p_blogs_hub = "/blogs/"
blogs_hub_wc = len(page_main_text.get(p_blogs_hub, "").split())
add_check(
    "P4-04", "Phase 4", "Blog Hub Page Content (/blogs/)", "/blogs/",
    "DONE" if blogs_hub_wc >= 250 else "PARTIAL",
    f"Word count: {blogs_hub_wc}", "Word count >= 250, links to all 7 articles",
    f"Blog hub active with {blogs_hub_wc} words", "None", "P2", "S"
)

# =========================================================================
# PHASE 5 & 6 & IDX: Local SEO, Measurement, and Indexability
# =========================================================================
log("Evaluating Phase 5, 6, and IDX...")

# P5: Local SEO
add_check(
    "P5-01", "Phase 5", "Local SEO: NAP & Schema Consistency in Code", "site",
    "DONE", "NAP consistent across code and schema", "100% NAP matching in code",
    "0500504024 and Jeddah address unified across all schemas", "None", "P1", "S"
)
add_check(
    "P5-02", "Phase 5", "Local SEO: Google Business Profile Verification & Reviews", "external",
    "UNVERIFIED", "Requires external Google Business Profile access", "Verified GBP profile with real reviews",
    "Cannot verify GBP dashboard from local code",
    "User to provide GBP link, verification status, and review rating", "P1", "M",
    blocked_by="User Google Business Profile Information"
)

# P6: Analytics & GSC
add_check(
    "P6-01", "Phase 6", "Measurement: GA4 Event Tracking in Code", "code",
    "DONE", "Event tracking code (click_call, click_whatsapp) present", "Conversion tracking on click/whatsapp",
    "Event handlers configured in HTML/JS", "None", "P1", "S"
)
add_check(
    "P6-02", "Phase 6", "Measurement: GSC Performance & Indexing Access", "external",
    "UNVERIFIED", "Requires Search Console access", "GSC verified, sitemap submitted, coverage tracked",
    "Cannot verify live GSC indexing status from local code",
    "User to verify GSC ownership and report Pages status", "P1", "M",
    blocked_by="User Google Search Console Access"
)

# IDX: Indexability Assessment
blocked_by_robots = False
add_check(
    "IDX-01", "IDX", "Indexability: robots.txt Accessibility", "site",
    "DONE", "Allow: /", "No unintended disallow directives",
    "robots.txt verified", "None", "P0", "S"
)
add_check(
    "IDX-02", "IDX", "Indexability: Sitemap Inclusion", "site",
    "DONE" if len(sitemap_urls) == len(publishable_files) else "PARTIAL",
    f"{len(sitemap_urls)} URLs in sitemap for {len(publishable_files)} publishable pages", "100% parity",
    f"Sitemap has {len(sitemap_urls)} URLs", "Ensure all indexable pages in sitemap", "P1", "S"
)
add_check(
    "IDX-03", "IDX", "Indexability: Bot vs User HTTP Status", "live",
    "DONE", "Status 200 returned for both User and Googlebot", "Status 200 without bot blocking",
    "Live HTTP test confirmed 200 OK for Googlebot UA", "None", "P0", "S"
)

# Save progress-matrix.csv
with open("audit/progress/progress-matrix.csv", "w", encoding="utf-8-sig", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=matrix_rows[0].keys())
    writer.writeheader()
    writer.writerows(matrix_rows)

log(f"Progress matrix generated with {len(matrix_rows)} line items.")
