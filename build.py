"""
Build the self-contained, offline single-file portfolio.

    python build.py

Reads  index.html  (the editable source)
Writes Mehedi-Hasan-Sajal-Portfolio.html  (served by GitHub Pages as index.html)

What it does
  1. embeds the Inter variable font (latin subset) as base64 @font-face
  2. bakes every <i data-lucide="x"> into an inline <svg> (fetched from lucide-static)
  3. inlines assets/tailwind.css and drops the Tailwind / Lucide CDN <script> tags
  4. embeds the photo and the CV as base64 data URIs

If you add NEW Tailwind utility classes to index.html you must regenerate
assets/tailwind.css first (render build-tmp in a browser with the Play CDN and copy
the injected <style> whose text starts with "*, "), otherwise those classes have no CSS.
"""
import base64, pathlib, re, urllib.request

ROOT = pathlib.Path(__file__).parent
UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/124.0.0.0 Safari/537.36"}

html = (ROOT / "index.html").read_text(encoding="utf-8")
tw = (ROOT / "assets" / "tailwind.css").read_text(encoding="utf-8").strip()

# 1) Inter (latin, variable 400-800)
gcss = urllib.request.urlopen(urllib.request.Request(
    "https://fonts.googleapis.com/css2?family=Inter:wght@400..800&display=swap", headers=UA), timeout=40).read().decode("utf-8")
blk = re.search(r"/\*\s*latin\s*\*/\s*(@font-face\s*\{.*?\})", gcss, re.S).group(1)
wurl = re.search(r"url\((https://[^)]+\.woff2)\)", blk).group(1)
rng = re.search(r"unicode-range:\s*([^;]+);", blk).group(1).strip()
woff2 = urllib.request.urlopen(urllib.request.Request(wurl, headers=UA), timeout=60).read()
font_face = ("  <style>\n    /* Inter variable (400-800, latin) embedded - works with no network */\n"
             "    @font-face{font-family:'Inter';font-style:normal;font-weight:400 800;font-display:swap;"
             "src:url(data:font/woff2;base64," + base64.b64encode(woff2).decode("ascii") +
             ")format('woff2');unicode-range:" + rng + "}\n  </style>")
old_font = ('  <link rel="preconnect" href="https://fonts.googleapis.com">\n'
            '  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
            '  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">')
assert old_font in html, "font <link> block not found in index.html"
html = html.replace(old_font, font_face)

# 2) drop the CDNs and inline the CSS
html = re.sub(r'\s*<script src="https://cdn\.tailwindcss\.com"></script>', "", html)
html = re.sub(r'\s*<script src="https://unpkg\.com/lucide@latest/dist/umd/lucide\.js"></script>', "", html)
html = re.sub(r'\s*<script>\s*tailwind\.config = \{.*?\}\s*</script>', "", html, flags=re.S)
assert "</head>" in html
html = html.replace("</head>", "  <style>\n/* Tailwind CSS (generated at build time, inlined) */\n" + tw + "\n  </style>\n</head>", 1)

# 3) bake the icons
cache = {}
def svg_for(name):
    if name not in cache:
        s = urllib.request.urlopen(urllib.request.Request(
            "https://unpkg.com/lucide-static@latest/icons/%s.svg" % name, headers=UA), timeout=30).read().decode("utf-8")
        s = re.sub(r"<!--.*?-->", "", s, flags=re.S)
        cache[name] = re.sub(r"\s+", " ", re.search(r"<svg[^>]*>(.*)</svg>", s, re.S).group(1)).strip()
    return cache[name]

def to_svg(name, classes):
    return ('<svg class="%s" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" '
            'fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" '
            'aria-hidden="true">%s</svg>') % (classes, svg_for(name))

theme_pair = to_svg("moon", "w-4 h-4 block dark:hidden") + to_svg("sun", "w-4 h-4 hidden dark:block")
html = html.replace('<i data-lucide="moon" class="w-4 h-4 theme-icon"></i>', theme_pair)
icon_re = re.compile(r'<i data-lucide="([a-z0-9-]+)" class="([^"]*)"></i>')
html, n = icon_re.subn(lambda m: to_svg(m.group(1), m.group(2)), html)
html = html.replace("    // ---- Icons ----\n    lucide.createIcons();\n",
                    "    /* Icons are baked into the markup - no runtime library needed */\n")
html = html.replace("""    function applyTheme(dark) {
      root.classList.toggle('dark', dark);
      document.querySelectorAll('.theme-icon').forEach(el => {
        el.setAttribute('data-lucide', dark ? 'sun' : 'moon');
      });
      lucide.createIcons();
    }""", """    function applyTheme(dark) {
      root.classList.toggle('dark', dark);
    }""")

# 4) embed the photo + CV
jpeg = (ROOT / "mehedi-hasan-sajal.jpeg").read_bytes()
pdf = (ROOT / "Mehedi-Hasan-Sajal-CV.pdf").read_bytes()
html = html.replace('src="mehedi-hasan-sajal.jpeg"', 'src="data:image/jpeg;base64,' + base64.b64encode(jpeg).decode("ascii") + '"')
html = html.replace('href="Mehedi-Hasan-Sajal-CV.pdf"', 'href="data:application/pdf;base64,' + base64.b64encode(pdf).decode("ascii") + '"')

out = ROOT / "Mehedi-Hasan-Sajal-Portfolio.html"
out.write_text(html, encoding="utf-8")
print("icons baked        :", n, "| leftover <i>:", len(re.findall(r'<i data-lucide', html)))
print("output             :", out.name, out.stat().st_size, "bytes")
print("external script/link:", len(re.findall(r'<script[^>]*\bsrc=', html)), "/", len(re.findall(r'<link[^>]*\bhref="https?', html)))
