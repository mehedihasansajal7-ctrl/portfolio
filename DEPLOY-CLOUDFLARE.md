# Cloudflare deployment (free) — LIVE

```
🌍 https://mehedi-portfolio.mehedihasansajal7.workers.dev/
```

Same site as GitHub Pages, on Cloudflare's edge. Free plan: **unlimited bandwidth and
requests**, 20,000 files, 25 MiB per file.

> **Why `workers.dev` and not `pages.dev`?**
> Cloudflare merged **Pages into Workers** in 2026 — `wrangler pages project create` now
> provisions a Worker with static assets, and the CLI recommends `wrangler deploy`.
> Also, `mehedi-portfolio.pages.dev` was **already taken by another user**, so it was never
> available to us. The Workers route is the supported path and behaves the same for a static
> site (`_headers`, custom domains, unlimited bandwidth).

---

## What gets deployed

`deploy/` — 14 files, ~1.05 MB:

```
deploy/
├── index.html                 ← the site (CV as a same-origin download)
├── Mehedi-Hasan-Sajal-CV.pdf
├── mehedi-hasan-sajal.jpeg
├── robots.txt
├── _headers                   ← security headers (Workers static assets honours this)
├── assets/                    detail.css · inter.woff2
└── projects/                  7 individual project pages
```

The Worker is configured by `wrangler.deploy.jsonc` in this folder:

```jsonc
{
  "name": "mehedi-portfolio",
  "compatibility_date": "2026-11-10",
  "assets": { "directory": "./deploy" }
}
```

---

## Redeploy after a change

```bash
cd portfolio
python build.py                        # rebuild index.hosted.html + the offline single file
python make_deploy.py                  # (or copy the changed files into deploy/ by hand)
npx wrangler deploy --config wrangler.deploy.jsonc
```

Wrangler is already logged in on this machine (OAuth token in
`%APPDATA%\xdg.config\.wrangler\config\default.toml`). If the login ever expires:
`npx wrangler login`.

---

## Shorter URL (optional)

The subdomain part comes from the account, not the project. To shorten it:

**Dashboard → Workers & Pages → (your) subdomain → change** — e.g. `mehedisajal`,
which would make the URL `https://mehedi-portfolio.mehedisajal.workers.dev`.
A **custom domain** (e.g. `mehedisajal.com`, ~$10/year) is set per Worker under
*Settings → Domains & Routes → Add custom domain*; SSL is automatic.

---

## Notes

- **Both hosts stay live** — GitHub Pages (`mehedihasansajal7-ctrl.github.io/portfolio/`) and
  this Workers URL serve the same content. Share whichever is easier; the `workers.dev` one is
  useful when a network blocks `github.io`.
- The pages are **host-agnostic**: project links are relative (`projects/<name>.html`), so the
  same files work on any host. The offline single file keeps absolute links so it still works
  from a USB stick.
- The site loads **zero external resources** — font, CSS, icons, photo are embedded or
  same-origin. Nothing can break because a CDN is blocked.
- A failed first attempt had uploaded the whole `portfolio/` source folder (wrangler wrote a
  stray `wrangler.jsonc` with `assets.directory: "."`). That was removed and the Worker was
  redeployed from `deploy/` only — `/cv.html`, `/cv-templates/…`, `/deploy/…` and
  `/index.src.html` all return 404.
