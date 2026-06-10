# Clean URL implementation notes

This folder converts the site from file-style URLs to clean directory URLs.

Examples:
- /how-we-help/ instead of /how-we-help.html
- /analytics-health-check/ instead of /analytics-health-check.html
- /about/ instead of /about.html

What changed:
- Each old page now also exists as a folder with an index.html file.
- Internal links now point to clean URLs.
- Canonical, Open Graph, JSON-LD, sitemap, and FormSubmit redirect URLs now point to clean URLs.
- Old .html files are kept as noindex redirect pages so old links still work.
- CSS, JS, favicon, and asset references use root-relative paths so subfolder pages load correctly on parallaxdatalab.com.

How to publish:
1. Copy these files/folders into the root of the GitHub Pages repo.
2. Keep your existing assets folder in the repo.
3. Commit and push.
4. In GitHub Pages settings, confirm Enforce HTTPS is checked.


## Local preview note

This package uses relative asset paths so pages can work in GitHub Pages and during local preview.
For the most accurate preview, open the folder through a tiny local server instead of double-clicking nested HTML files:

```powershell
python -m http.server 8014
```

Then open:

```text
http://127.0.0.1:8014/
```

If images do not appear locally, make sure your existing `assets/` folder is copied into the root of this package before previewing or pushing.
