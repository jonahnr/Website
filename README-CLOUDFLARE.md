# Parallax Data Lab, Cloudflare Pages Clean URL Package

This package is designed to solve both problems:

1. The files are still flat and easy to test locally by opening `index.html` or running a normal local server.
2. Cloudflare Pages can serve clean public URLs like `/about/` and `/how-we-help/` using the `_redirects` file.

## Important

Keep your existing `assets/` folder in the repo root. This zip does not include the full assets folder.

## Local quick check

You can open `index.html`, `about.html`, or `how-we-help.html` directly and the CSS should load because this version uses relative asset paths.

## Cloudflare-style local test

Use this for testing clean URLs and redirects:

```powershell
npx wrangler pages dev .
```

Then open:

```text
http://localhost:8788/
http://localhost:8788/about/
http://localhost:8788/how-we-help/
http://localhost:8788/about.html
```

Expected behavior:

- `/about/` loads `about.html`
- `/how-we-help/` loads `how-we-help.html`
- `/about.html` redirects to `/about/`
- formatting stays intact

## Cloudflare Pages build settings

Framework preset: None
Build command: exit 0
Build output directory: /

If `/` is rejected, use `.` for the output directory.
