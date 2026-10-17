# Mehedi Hasan Sajal — Portfolio

Personal portfolio site (single-file, dependency-free) for **Mehedi Hasan Sajal** —
Sales Operations & MIS professional and builder of business automation systems.

- `index.html` — the whole site (Tailwind CDN + Lucide icons, light/dark theme,
  scroll-reveal, responsive nav). No build step.
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

Five are **internal / private systems** (the live apps are behind staff sign-in and the GitHub
repos are private, so linking them would be a dead end). Two are **publicly reachable** and are the
only clickable project links on the page.

1. Corporate Zakat Management & Assurance Platform — Next.js / Prisma / PostgreSQL
2. SFUWT Welfare Application Portal — Flask / SQLite *(live, staff sign-in required)*
3. SFUWT Control Tower & Field Visit Tracker — Node.js / MSSQL *(live, staff sign-in required)*
4. **Family Finance** — Android (Kotlin / Jetpack Compose / Firebase) + an installable web PWA →
   <https://family-finance-98333.web.app/> *(live; sign in with a family ID)*
5. Transport Management System (TMS) — Next.js 16 / Prisma / PostgreSQL
6. **Small Business Manager — with a Farming module** — TypeScript npm-workspaces monorepo
   (`packages/domain` pure logic · Node + `node:sqlite` API · React/Vite PWA · Expo Android ·
   Supabase/PostgreSQL port); offline-first double-entry accounting + farming costing.
   Public Android APK releases:
   <https://github.com/mehedihasansajal7-ctrl/small-business-manager-downloads/releases/latest>
7. Integrated Sales, Order, Inventory & Delivery ERP — Next.js 16 / React 19 / Prisma /
   PostgreSQL 17 / Tailwind 4 (bulk-commodity trading; role-based, rules enforced in code *and* by
   DB CHECK constraints + append-only audit trigger). Source lives in `D:\sales-erp`.

> Everything else that works for a visitor is the GitHub **profile**
> (`github.com/mehedihasansajal7-ctrl`) — individual repo links 404 because those repos are private.

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
