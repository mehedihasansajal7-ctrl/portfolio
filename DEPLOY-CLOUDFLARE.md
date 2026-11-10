# Deploying the portfolio to Cloudflare Pages (free)

`deploy/` is a ready-to-upload static site — no build step, no server, no dependencies.

```
deploy/                        1.05 MB · 14 files
├── index.html                 282 KB  ← the site (hosted build: CV is a file link)
├── Mehedi-Hasan-Sajal-CV.pdf  632 KB
├── mehedi-hasan-sajal.jpeg     75 KB
├── robots.txt
├── _headers                   basic security headers (Cloudflare reads this)
├── assets/
│   ├── detail.css             styles for the project pages
│   └── inter.woff2            the font
└── projects/                  7 individual project pages
```

Cloudflare free plan limits: 20,000 files · 25 MiB per file · 500 builds/month ·
**unlimited bandwidth and requests**. We are far below all of them.

---

## Deploy — dashboard drag & drop (easiest, ~2 minutes)

1. Go to **https://dash.cloudflare.com/sign-up** and create a free account
   (email only — **no credit card**). Verify the email.
2. In the dashboard: **Workers & Pages → Create → Pages → Upload assets**
   (on some screens: *Direct Upload*).
3. Project name: e.g. `mehedi-portfolio` → **Create project**.
4. **Drag the whole `deploy` folder** into the upload box (or click *select from computer*
   and pick the folder). Do not drag the *contents* one by one — the folder keeps the
   `assets/` and `projects/` structure.
5. **Deploy site**. You get a URL like:

```
https://mehedi-portfolio.pages.dev
```

That link works on any device, any network, HTTPS included.

---

## Deploy — CLI (alternative)

```bash
npm install -g wrangler          # once
wrangler login                   # opens the browser once
cd "C:\Users\user\Downloads\Open code project\portfolio"
wrangler pages deploy deploy --project-name mehedi-portfolio
```

---

## After a change

The pages are generated, so after editing anything:

```bash
cd portfolio
python build.py                  # rebuilds index.hosted.html + the offline single file
python make_deploy.py            # (or just re-copy the changed files into deploy/)
```

…then either re-drag the folder in the dashboard, or re-run `wrangler pages deploy deploy`.

> If you change the CV, replace `portfolio/Mehedi-Hasan-Sajal-CV.pdf`, run `python build.py`,
> and copy the new PDF into `deploy/`.

---

## Custom domain (optional, free)

Cloudflare Pages → your project → **Custom domains → Set up a custom domain**.
If the domain's DNS is already on Cloudflare, SSL is issued automatically.
(A custom domain removes the `*.pages.dev` name from the URL entirely.)

---

## Notes

- **GitHub Pages can stay live in parallel.** Both hosts serve the same content; the
  `pages.dev` one is the one to share if a network blocks `github.io`.
- The project pages use **relative** links, so the site works on any host
  (`projects/<name>.html`). The offline single file (`Mehedi-Hasan-Sajal-Portfolio.html`)
  keeps **absolute** links so it still works when opened from a USB stick.
- `_headers` sets `X-Content-Type-Options`, `Referrer-Policy`, `X-Frame-Options` and a
  restrictive `Permissions-Policy`. Nothing else is needed — the site loads **zero external
  resources** (font, CSS, icons, photo all embedded or same-origin).
