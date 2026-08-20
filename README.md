# लुँध्वाखा — PDF Book Viewer

A mobile-first website for reading Lundhwakha (लुँध्वाखा) Newari-language newspaper issues online — no download needed. Pages stream in the browser with book-style flipping, pinch zoom, and a page slider.

## What's inside

```
index.html      → library homepage (all issues with covers)
reader.html     → the book reader (swipe / zoom / page slider)
issues.json     → list of issues (auto-generated)
generate.py     → script that rebuilds covers + issues.json
pdfs/           → the PDF issues (lundhwakha-114.pdf ... )
covers/         → auto-generated cover thumbnails
assets/logo.png → masthead logo
vendor/pdfjs/   → PDF.js (bundled, no CDN needed)
vercel.json     → caching config for Vercel
```

## Deploy to Vercel (2 minutes)

**Option A — drag and drop (easiest):**
1. Go to https://vercel.com/new
2. Choose "Deploy without Git" / drag this whole folder onto the page
3. Done — you get a URL like `lundhwakha.vercel.app`

**Option B — with the Vercel CLI:**
```bash
npm i -g vercel
cd lundhwakha
vercel --prod
```

**Option C — via GitHub (best for updates):**
1. Push this folder to a GitHub repo
2. Import the repo at https://vercel.com/new
3. Framework preset: **Other**, no build command, output directory: `./`
4. Every future git push auto-deploys

> Note: GitHub blocks single files over 100 MB and Vercel deployments are capped in total size, but these PDFs (2–8 MB each) are far below any limit even with 30+ issues.

## Adding a new issue (easiest way — no tools needed)

Everything is automated with GitHub Actions. When a new issue comes out:

1. Rename the PDF to `lundhwakha-<number>.pdf` (e.g. `lundhwakha-140.pdf` — lowercase, hyphen, no spaces).
2. Go to https://github.com/bibek-magar/lundhwakha/tree/main/pdfs
3. Click **Add file → Upload files**, drop the PDF in, click **Commit changes**.
4. Wait ~2 minutes. Done — the cover thumbnail and issue list are generated automatically, and Vercel deploys the update. The new issue appears at the top of https://lundhwakha.vercel.app

Notes: GitHub's web upload accepts files up to 25 MB (all issues so far fit). Works from a phone browser too.

## Adding issues manually (alternative)

1. Copy the PDF into `pdfs/` as `lundhwakha-<number>.pdf`
2. Run `python3 generate.py` (needs Python 3 + poppler-utils + qpdf)
3. Push to `main` — Vercel auto-deploys.

## Reader features

- One page at a time, book style — swipe left/right or use ‹ › buttons
- Pinch to zoom, double-tap to zoom, +/− buttons, "मिले" to fit
- Page slider to jump anywhere; page numbers in Devanagari
- Remembers where you stopped reading in each issue
- Streams the PDF — readers never have to download the file
- Works on any phone browser; also supports keyboard arrows on desktop
