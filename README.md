# Mehedi Hasan Sajal — Portfolio

Personal portfolio site (single-file, dependency-free) for **Mehedi Hasan Sajal** —
Sales Operations & MIS professional and builder of business automation systems.

- `index.html` — the whole site (Tailwind CDN + Lucide icons, light/dark theme,
  scroll-reveal, responsive nav). No build step.
- `mehedi-hasan-sajal.jpeg` — professional headshot (hero).
- `Mehedi-Hasan-Sajal-CV.pdf` — downloadable CV used by the "Download CV" buttons.
- `Mehedi-Hasan-Sajal-Portfolio.html` — **single-file shareable build**: the photo and the CV are
  embedded as base64 data URIs, so this ONE file can be sent via WhatsApp / email and shows the
  photo + downloads the CV with no companion files. It only needs internet for the Tailwind /
  Lucide / Google-Fonts CDNs. Regenerate after editing `index.html` by re-running the embed step
  (base64-inline `src="mehedi-hasan-sajal.jpeg"` and both `href="Mehedi-Hasan-Sajal-CV.pdf"`).

## Featured projects

1. Corporate Zakat Management & Assurance Platform — Next.js / Prisma / PostgreSQL
2. SFUWT Welfare Application Portal — Flask / SQLite → https://sfuwt-welfare.opsh.io/
3. SFUWT Control Tower & Field Visit Tracker — Node.js / MSSQL → https://sfuwt-dashboard.opsh.io/
4. Family Finance — Android (Kotlin / Jetpack Compose / Firebase)
5. Transport Management System (TMS) — Next.js 16 / Prisma / PostgreSQL

## Local preview

Open `index.html` directly in a browser, or serve the folder:

```bash
python -m http.server 8791
# → http://127.0.0.1:8791/index.html
```
