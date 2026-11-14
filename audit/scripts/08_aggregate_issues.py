import os
import re
import csv
import json
from pathlib import Path

def log(msg):
    with open("audit/run-log.txt", "a", encoding="utf-8") as f:
        f.write(f"[ISSUES-AGGREGATE] {msg}\n")
    print(msg)

log("Aggregating all audit issues...")

issues = []
issue_counter = 1

def add_issue(severity, category, affected_pages, description, proof, recommended_fix):
    global issue_counter
    issues.append({
        "issue_id": f"ISSUE-{issue_counter:03d}",
        "severity": severity, # Critical, High, Medium, Low
        "category": category, # Indexability, Content, Links, Images, Schema, Claims
        "affected_pages_count": len(affected_pages) if isinstance(affected_pages, list) else 1,
        "affected_sample": "; ".join(affected_pages[:5]) if isinstance(affected_pages, list) else str(affected_pages),
        "description": description,
        "proof": proof,
        "recommended_fix": recommended_fix
    })
    issue_counter += 1

# 1. Broken Links Check
with open("audit/04-links.csv", "r", encoding="utf-8-sig") as f:
    broken = [r for r in csv.DictReader(f) if r.get("is_broken") == "True"]
    if broken:
        pages = sorted(list(set(r["source_path"] for r in broken)))
        sample_links = [f"{r['source_path']} -> {r['target_href']}" for r in broken[:3]]
        add_issue(
            "High",
            "Links",
            pages,
            f"تم رصد {len(broken)} رابطاً داخلياً معطلاً أو موجهاً لمسارات غير موجودة محلياً.",
            " | ".join(sample_links),
            "تصحيح الروابط المعطلة لتوجه إلى المسارات الصحيحة مع السلاش النهائي."
        )

# 2. Image Issues Check
with open("audit/06-images.csv", "r", encoding="utf-8-sig") as f:
    imgs = list(csv.DictReader(f))
    missing_alt = [r for r in imgs if "MISSING_ALT" in r.get("issues", "")]
    missing_dims = [r for r in imgs if "MISSING_DIMENSIONS" in r.get("issues", "")]
    not_found = [r for r in imgs if "FILE_NOT_FOUND_404" in r.get("issues", "")]
    
    if not_found:
        pages = sorted(list(set(r["page"] for r in not_found)))
        add_issue(
            "Critical",
            "Images",
            pages,
            f"يوجد {len(not_found)} صور غير موجودة (404) على الخادم ومشار إليها في صفحات الموقع.",
            "; ".join(r["src"] for r in not_found[:3]),
            "رفع الصور المفقودة إلى assets/img/ أو تصحيح مسارات الصور."
        )
    if missing_alt:
        pages = sorted(list(set(r["page"] for r in missing_alt)))
        add_issue(
            "Medium",
            "Images",
            pages,
            f"يوجد {len(missing_alt)} صورة تفتقر للنص البديل (alt text) مما يضعف أرشفة صور جوجل وإمكانية الوصول.",
            "; ".join(r["src"] for r in missing_alt[:3]),
            "إضافة وصف دقيق وغني بالكلمات المفتاحية لكل صورة عبر سمة alt."
        )
    if missing_dims:
        pages = sorted(list(set(r["page"] for r in missing_dims)))
        add_issue(
            "Low",
            "Images",
            pages,
            f"يوجد {len(missing_dims)} صورة بدون سمات العرض والارتفاع المحددة (width/height).",
            "; ".join(r["src"] for r in missing_dims[:3]),
            "تحديد width و height في كود HTML لمنع انزياح التخطيط التراكمي (CLS)."
        )

# 3. Schema Issues Check
with open("audit/07-schema-validation.csv", "r", encoding="utf-8-sig") as f:
    schemas = list(csv.DictReader(f))
    placeholders = [r for r in schemas if r.get("has_placeholders") == "True"]
    invalid_json = [r for r in schemas if r.get("valid_json") == "False"]
    missing_fields = [r for r in schemas if r.get("missing_recommended_fields")]
    
    if placeholders:
        pages = sorted(list(set(r["page"] for r in placeholders)))
        add_issue(
            "Critical",
            "Schema",
            pages,
            f"تم رصد عناصر نائبة {{...}} داخل أكواد Schema JSON-LD في {len(placeholders)} موضعاً.",
            "; ".join(r["placeholders"] for r in placeholders[:3]),
            "تنظيف وإزالة العناصر النائبة واستبدالها ببيانات حقيقية ثابتة."
        )
    if invalid_json:
        pages = sorted(list(set(r["page"] for r in invalid_json)))
        add_issue(
            "Critical",
            "Schema",
            pages,
            f"يوجد خطأ في تركيب كود JSON-LD (Syntax Parse Error) في {len(invalid_json)} صفحة.",
            "; ".join(r["error_msg"] for r in invalid_json[:3]),
            "تصحيح الفواصل والأقواس في أكواد السكيما."
        )

# 4. Duplicate Content Check
with open("audit/11-duplicates.csv", "r", encoding="utf-8-sig") as f:
    dupes = list(csv.DictReader(f))
    crit_dupes = [r for r in dupes if r.get("severity") == "CRITICAL"]
    if crit_dupes:
        pages = sorted(list(set(r["page_a"] for r in crit_dupes).union(set(r["page_b"] for r in crit_dupes))))
        add_issue(
            "High",
            "Content",
            pages,
            f"تم رصد تطابق محتوى شديد (أعلى من 75% تشابه) بين {len(crit_dupes)} زوجاً من الصفحات (Doorway Pages Risk).",
            f"أعلى نسبة تشابه: {crit_dupes[0]['cosine_similarity_pct']}% بين {crit_dupes[0]['page_a']} و {crit_dupes[0]['page_b']}",
            "إعادة صياغة محتوى صفحات الأحياء والخدمات المتشابهة وإضافة تفاصيل مميزة لكل حي وخدمة لمنع عقوبات جوجل للمحتوى المكرر."
        )

# 5. Claims and Promises Check
with open("audit/08-claims-and-facts.csv", "r", encoding="utf-8-sig") as f:
    claims = list(csv.DictReader(f))
    hours_claims = [r for r in claims if r.get("claim_type") == "24_HOURS"]
    if hours_claims:
        pages = sorted(list(set(r["page"] for r in hours_claims)))
        add_issue(
            "Medium",
            "Claims",
            pages,
            f"وجود ادعاءات 'خدمة 24 ساعة' في {len(hours_claims)} موضعاً بينما ساعات العمل الرسمية محددة 9ص-9م والجمعة مغلق.",
            "; ".join(r["matched_text"] for r in hours_claims[:3]),
            "تعديل العبارات إلى 'خدمة سريعة طوال ساعات العمل الرسمية' والتوافق مع ساعات العمل الحقيقية."
        )

# 6. Orphan Pages Check
with open("audit/05-link-graph.md", "r", encoding="utf-8") as f:
    graph_text = f.read()
    orphan_matches = re.findall(r"- `(/[^`]+)` \(Inbound count: (\d+)\)", graph_text)
    if orphan_matches:
        orphan_paths = [m[0] for m in orphan_matches]
        add_issue(
            "Medium",
            "Links",
            orphan_paths,
            f"يوجد {len(orphan_paths)} صفحة يتيمة أو ضعيفة الربط الداخلي (أقل من 3 روابط داخلية واردة إليها).",
            "; ".join(orphan_paths[:5]),
            "تعزيز الروابط الداخلية إلى هذه الصفحات من خلال الفوتر أو أقسام الخدمات في الصفحات الرئيسية وذات الصلة."
        )

with open("audit/13-issues.csv", "w", encoding="utf-8-sig", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=issues[0].keys())
    writer.writeheader()
    writer.writerows(issues)

log(f"Issues aggregation complete. {len(issues)} aggregate issues recorded.")

