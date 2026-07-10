file_path = '/Users/gregmontoya/AntiGravity Workspaces/Paul_Project_1/CSL-Resale-Advantage/resale-advantage-v3/csl-investor-exit-advantage-v3.html'
with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Revert Navigation Header CSS to normal (no vertical stacking)
old_css = """  .nav-left { display: flex; flex-direction: column; align-items: flex-start; gap: 5px; }
  .program-title-sub { 
    font-size: 0.72rem; 
    font-weight: 800; 
    color: var(--navy); 
    letter-spacing: 0.05em; 
    text-transform: uppercase;
    line-height: 1.0;
  }
  .program-title-sub span {
    color: var(--accent);
  }"""

new_css = """  .nav-left { display: flex; align-items: center; }"""

html = html.replace(old_css, new_css)

# Remove mobile stacked font override
html = html.replace("\\n    .program-title-sub { font-size: 0.65rem; }", "")

# 2. Revert Header HTML to just show the logo image (logo1.svg) and phone link
old_header_html = """<header id="sticky-header">
  <div class="wrap">
    <div class="nav-left">
      <a class="wordmark" href="https://www.centerstreetlending.com/"><img src="logo1.svg" alt="Center Street Lending" style="height: 26px; width: auto; display: block;"></a>
      <span class="program-title-sub">CSL RESALE ADVANTAGE <span>PROGRAM</span></span>
    </div>
    <a class="phone" href="tel:5555555555">(555) 555-5555</a>
  </div>
</header>"""

new_header_html = """<header id="sticky-header">
  <div class="wrap">
    <div class="nav-left">
      <a class="wordmark" href="https://www.centerstreetlending.com/"><img src="logo1.svg" alt="Center Street Lending" style="height: 36px; width: auto; display: block;"></a>
    </div>
    <a class="phone" href="tel:5555555555">(555) 555-5555</a>
  </div>
</header>"""

html = html.replace(old_header_html, new_header_html)

# Also ensure standard mobile logo size override matches:
html = html.replace(
    "header a.wordmark img { height: 22px !important; }",
    "header a.wordmark img { height: 26px !important; }"
)

# 3. Update Hero Left Top HTML:
# - Logo brand tag row sits at the very top.
# - Below the brand tag row, inject the eyebrow element (with vertical blue line) containing capitalized "CSL RESALE ADVANTAGE PROGRAM" in white text.
# - Headline sits below the eyebrow.
old_hero_top = """    <div class="hero-left">
      <div class="hero-left-top">
        <div class="hero-brand-row">
          <img src="logo1.svg" alt="Center Street Lending" style="height: 32px; width: auto; display: block;">
          <span class="brand-divider">|</span>
          <span class="brand-text">PRE-NEGOTIATED FOR CSL BORROWERS</span>
        </div>
        <h1><span style="display: inline-block; white-space: nowrap;">WE MADE IT <span class="hl">EASIER & CHEAPER</span></span><br><span style="display: inline-block; white-space: nowrap;">TO EXIT YOUR INVESTMENT.</span></h1>"""

new_hero_top = """    <div class="hero-left">
      <div class="hero-left-top">
        <div class="hero-brand-row">
          <img src="logo1.svg" alt="Center Street Lending" style="height: 32px; width: auto; display: block;">
          <span class="brand-divider">|</span>
          <span class="brand-text">PRE-NEGOTIATED FOR CSL BORROWERS</span>
        </div>
        <div class="hero-eyebrow">CSL RESALE ADVANTAGE PROGRAM</div>
        <h1><span style="display: inline-block; white-space: nowrap;">WE MADE IT <span class="hl">EASIER & CHEAPER</span></span><br><span style="display: inline-block; white-space: nowrap;">TO EXIT YOUR INVESTMENT.</span></h1>"""

html = html.replace(old_hero_top, new_hero_top)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Branding corrected: Nav logo is clean, CSL RESALE ADVANTAGE PROGRAM sits under brand logo in hero, above H1!")
