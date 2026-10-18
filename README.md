# Mehedi Hasan Sajal — Portfolio

Personal portfolio site (single-file, dependency-free) for **Mehedi Hasan Sajal** —
Sales Operations & MIS professional and builder of business automation systems.

## 🌐 Live site

**https://mehedihasansajal7-ctrl.github.io/portfolio/**

Hosted on **GitHub Pages** from this repo (`main` branch, `/` root). The served `index.html` is the
**fully self-contained build** — fonts, Tailwind CSS, all icons, the photo and the CV are embedded —
so the live page makes **zero external requests** and cannot break because a CDN or Google Fonts is
blocked. (`index.src.html` is the editable source; after editing it, rebuild and copy the result
over `index.html`.)

> The repo has to stay **public** for GitHub Pages on the free plan. Before it was made public the
> whole git history was scanned: no tokens, API keys, ERP hosts or `.env` values (20 commits, clean).

### One page per project

Every card's **View Project** button opens that project's own page under `projects/`:

| Project | Page |
|---|---|
| Zakat Management | `projects/zakat-management.html` |
| SFUWT Welfare Portal | `projects/sfuwt-welfare-portal.html` |
| SFUWT Control Tower | `projects/sfuwt-control-tower.html` |
| Family Finance | `projects/family-finance.html` |
| Transport Management System | `projects/transport-management-system.html` |
| Small Business Manager | `projects/small-business-manager.html` |
| Sales ERP | `projects/sales-erp.html` |

Each page has: what the project is, what it does (bullet list), the stack, its links (source / live
app / APK — only where public), a "back to portfolio" link and previous/next navigation. The pages
share `assets/detail.css` + `assets/inter.woff2`, so they stay ~5 KB each and still need no CDN.
They are generated from the data in the build script; project screenshots are deliberately **not**
included (the available ones contain real applicant data).

- `index.html` — the served, self-contained build (**edit `index.src.html` instead**).
- `index.src.html` — the editable source (Tailwind CDN + Lucide icons, light/dark theme,
  scroll-reveal, responsive nav). No build step.
- `projects/` + `assets/` — the per-project pages and their shared CSS/font.
- `mehedi-hasan-sajal.jpeg` — professional headshot (hero).
- `Mehedi-Hasan-Sajal-CV.pdf` — downloadable CV used by the "Download CV" buttons.
- `Mehedi-Hasan-Sajal-Portfolio.html` — **single-file, fully offline shareable build** (~377 KB).
  Everything is embedded, so it renders with **zero network access**: the Inter font (variable
  woff2, latin subset, base64 `@font-face`), the Tailwind CSS (generated at build time and inlined),
  all 41 Lucide icons (baked as inline SVG — the theme toggle uses two SVGs toggled by
  `block dark:hidden` / `hidden dark:block`, so no JS icon library), plus the photo and the CV as
  base64 data URIs. Verified with all external requests blocked: 0 network calls, Inter available,
  photo loads, dark mode toggles, CV downloads as `Mehedi-Hasan-Sajal-CV.pdf`.
  Send this ONE file via WhatsApp/email; the recipient only needs a browser.
  ⚠️ Rebuild it after editing `index.html` (see `docs` note / build steps in the repo history):
  embed the font, bake the icons, inline the generated Tailwind CSS, drop the CDN tags, then
  base64-inline `src="mehedi-hasan-sajal.jpeg"` and both `href="Mehedi-Hasan-Sajal-CV.pdf"`.

## Featured projects

Every card has a **View Project** button that opens a **one-page summary on the GitHub profile**
(`github.com/mehedihasansajal7-ctrl#<project>`) — so a recruiter reads the project name, what it does
and the stack, instead of landing in a wall of code. Those summaries live in the special
profile-README repo `mehedihasansajal7-ctrl/mehedihasansajal7-ctrl`.

**Four of the seven repos are public** (inside each summary there is a direct source link):

| Project | Public artifacts |
|---|---|
| Family Finance | source `family-finance-app` + live PWA <https://family-finance-98333.web.app/> |
| Transport Management System | source `tms` |
| Small Business Manager | source `small-business-manager` + public APK releases <https://github.com/mehedihasansajal7-ctrl/small-business-manager-downloads/releases/latest> |
| Sales ERP | source `sales-erp` |

The three **SFUWT systems** (`sfuwt-welfare`, `sfuwt-dashboard`, `welfare-dashboard`) and
`zakat-platform` stay **private**: their source contains a live ERP data-warehouse credential and the
live apps' default staff passwords, and they are the employer's / trust's systems — so a public link
would be both a security and an IP problem. Those cards end with an honest note instead.

1. Corporate Zakat Management & Assurance Platform — Next.js / Prisma / PostgreSQL *(private)*
2. SFUWT Welfare Application Portal — Flask / SQLite *(private; live, staff sign-in)*
3. SFUWT Control Tower & Field Visit Tracker — Node.js / MSSQL *(private; live, staff sign-in)*
4. Family Finance — Android (Kotlin / Jetpack Compose / Firebase) + installable web PWA **(public)**
5. Transport Management System (TMS) — Next.js 16 / Prisma / PostgreSQL **(public)**
6. Small Business Manager — with a Farming module — TypeScript npm-workspaces monorepo **(public)**
7. Integrated Sales, Order, Inventory & Delivery ERP — Next.js 16 / React 19 / Prisma /
   PostgreSQL 17 / Tailwind 4 **(public)**. Source lives in `D:\sales-erp`.

> Before any of the four were published the git **history** was checked for secrets, and two were
> cleaned: `family-finance-app` had its real `app/google-services.json` (API key + project id) purged
> from all history and replaced by a sanitised `app/google-services.example.json`;
> `small-business-manager` had a dev-only `.local-smoke-data/.session_secret` purged. Pre-purge git
> bundles were kept in `%TEMP%\opencode\*-pre-purge.bundle`.

## Rebuilding the offline single-file build

`Mehedi-Hasan-Sajal-Portfolio.html` is a generated artifact. After any edit to `index.html`
(especially if you add **new Tailwind classes or new icons**) rebuild it:

1. **Embed the font** — fetch `https://fonts.googleapis.com/css2?family=Inter:wght@400..800&display=swap`
   with a Chrome User-Agent, keep the **`latin`** `@font-face` only (it covers every non-ASCII char
   used here; `latin-ext` covers none), download its `.woff2` and inline it as
   `src:url(data:font/woff2;base64,…)` — replacing the three Google-Fonts `<link>` tags.
2. **Bake the icons** — for every `<i data-lucide="NAME" class="CLASSES"></i>`, fetch
   `https://unpkg.com/lucide-static@latest/icons/NAME.svg` and replace the tag with an inline
   `<svg class="CLASSES" …>`. The theme toggle becomes **two** SVGs (moon `block dark:hidden`,
   sun `hidden dark:block`) and the theme JS loses its `lucide.createIcons()` calls.
3. **Inline Tailwind** — load the intermediate file in a browser with the Play CDN still present,
   read the injected `<style>` whose text starts with `*,`, and save it. (This is why a *new*
   Tailwind class needs a rebuild: the CDN only generates the classes it sees.)
4. **Finalise** — replace `<script src="https://cdn.tailwindcss.com">` with that CSS inside a
   `<style>` at the end of `<head>`; delete the Tailwind/lucide `<script>` tags and the
   `tailwind.config` block (it needs the CDN global); then base64-inline
   `src="mehedi-hasan-sajal.jpeg"` and both `href="Mehedi-Hasan-Sajal-CV.pdf"`.
5. **Verify** — the page must report `performance.getEntriesByType('resource')` with **0** external
   requests, `document.fonts.check('16px Inter') === true`, the photo loading, the dark-mode toggle
   working and the CV downloading as `Mehedi-Hasan-Sajal-CV.pdf`.

⚠️ Do all file reads/writes in **Python with `encoding="utf-8"`**. PowerShell's `Get-Content` /
`Out-File` (and `git show | Out-File`) decode bytes with the console code page and will corrupt
`—`, `·`, `→` into mojibake.

## Local preview

Open `index.html` directly in a browser, or serve the folder:

```bash
python -m http.server 8791
# → http://127.0.0.1:8791/index.html
```
