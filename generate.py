#!/usr/bin/env python3
"""
Regenerates covers/ thumbnails and issues.json from whatever PDFs are in pdfs/.

Usage:
  1. Drop new PDFs into pdfs/ named like  lundhwakha-122.pdf
  2. Run:  python3 generate.py
  3. Commit & push (Vercel redeploys automatically)

Requires: poppler-utils (pdftoppm) and qpdf, or it falls back to pypdf for page counts.
"""
import json, os, re, subprocess, sys

ROOT = os.path.dirname(os.path.abspath(__file__))
PDF_DIR = os.path.join(ROOT, "pdfs")
COVER_DIR = os.path.join(ROOT, "covers")
os.makedirs(COVER_DIR, exist_ok=True)

DEV_DIGITS = str.maketrans("0123456789", "०१२३४५६७८९")

def page_count(path):
    try:
        out = subprocess.check_output(["qpdf", "--show-npages", path])
        return int(out.strip())
    except Exception:
        from pypdf import PdfReader  # pip install pypdf
        return len(PdfReader(path).pages)

issues = []
for fname in sorted(os.listdir(PDF_DIR)):
    m = re.match(r"lundhwakha-(\d+)\.pdf$", fname)
    if not m:
        continue
    num = m.group(1)
    cover = os.path.join(COVER_DIR, f"cover-{num}.jpg")
    if not os.path.exists(cover):
        subprocess.check_call([
            "pdftoppm", "-f", "1", "-l", "1", "-jpeg", "-r", "60",
            "-jpegopt", "quality=78",
            os.path.join(PDF_DIR, fname),
            os.path.join(COVER_DIR, f"cover-{num}"),
        ])
        for f in os.listdir(COVER_DIR):
            if f.startswith(f"cover-{num}-"):
                os.rename(os.path.join(COVER_DIR, f), cover)
    issues.append({
        "id": num,
        "title": f"लुँध्वाखा {num.translate(DEV_DIGITS)}",
        "file": f"pdfs/{fname}",
        "cover": f"covers/cover-{num}.jpg",
        "pages": page_count(os.path.join(PDF_DIR, fname)),
    })

# newest issue first
issues.sort(key=lambda i: int(i["id"]), reverse=True)

with open(os.path.join(ROOT, "issues.json"), "w", encoding="utf-8") as f:
    json.dump({"issues": issues}, f, ensure_ascii=False, indent=2)

print(f"Wrote issues.json with {len(issues)} issues")
