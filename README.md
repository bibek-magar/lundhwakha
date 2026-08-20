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

## Adding the rest of your ~30 PDFs

1. Copy each PDF into `pdfs/` named like this (number = issue number):
   ```
   pdfs/lundhwakha-122.pdf
   pdfs/lundhwakha-123.pdf
   ```
2. Rebuild covers and the issue list (needs Python 3 + poppler-utils):
   ```bash
   python3 generate.py
   ```
   (macOS: `brew install poppler qpdf` · Ubuntu: `sudo apt install poppler-utils qpdf`)
3. Redeploy (re-drag the folder, or `vercel --prod`, or git push).

That's it — the new issues appear on the homepage automatically, newest first.

If you can't run the script, you can also add an entry to `issues.json` by hand and place a `covers/cover-122.jpg` image yourself.

## Reader features

- One page at a time, book style — swipe left/right or use ‹ › buttons
- Pinch to zoom, double-tap to zoom, +/− buttons, "मिले" to fit
- Page slider to jump anywhere; page numbers in Devanagari
- Remembers where you stopped reading in each issue
- Streams the PDF — readers never have to download the file
- Works on any phone browser; also supports keyboard arrows on desktop
