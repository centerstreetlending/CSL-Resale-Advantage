file_path = '/Users/gregmontoya/AntiGravity Workspaces/Paul_Project_1/CSL-Resale-Advantage/resale-advantage-v3/csl-investor-exit-advantage-v3.html'
with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Restore the program title style in CSS and remove the temporary wordmark override
old_css = """  /* Wordmark Logos Styles */
  .wordmark { 
    font-weight: 800; 
    color: var(--navy); 
    font-size: 1.05rem; 
    letter-spacing: .04em; 
    text-decoration: none; 
  }
  .wordmark span { 
    color: var(--accent); 
  }
  
  .hero-wordmark { 
    display: block; 
    font-weight: 800; 
    color: #fff !important; 
    font-size: 1.15rem; 
    letter-spacing: .04em; 
    text-decoration: none; 
    margin-bottom: 8px;
  }
  .hero-wordmark span { 
    color: var(--accent); 
  }
  
  header.scrolled {
    padding: 10px 0;
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
  }"""

new_css = """  .nav-left { display: flex; align-items: center; }
  .program-title { 
    display: inline-block; 
    font-size: 1.3rem; 
    font-weight: 700; 
    color: var(--navy); 
    letter-spacing: -0.019em; 
  }
  .program-title span {
    color: var(--accent);
  }
  
  header.scrolled {
    padding: 10px 0;
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
  }"""

html = html.replace(old_css, new_css)

# Re-add mobile styling overrides for header logo image
html = html.replace(
    "@media(max-width:640px){\n    .offer-bar {",
    "@media(max-width:640px){\n    header a.wordmark img { height: 26px !important; }\n    .offer-bar {"
)
html = html.replace(
    "@media(max-width:380px){\n    header a.phone {",
    "@media(max-width:380px){\n    header a.wordmark img { height: 22px !important; }\n    header a.phone {"
)

# 2. Revert Header HTML to display "CSL Resale Advantage Program"
old_header_html = """<header id="sticky-header">
  <div class="wrap">
    <div class="nav-left">
      <a class="wordmark" href="https://www.centerstreetlending.com/">CENTER STREET <span>LENDING</span></a>
    </div>
    <a class="phone" href="tel:5555555555">(555) 555-5555</a>
  </div>
</header>"""

new_header_html = """<header id="sticky-header">
  <div class="wrap">
    <div class="nav-left">
      <span class="program-title">CSL Resale Advantage <span>Program</span></span>
    </div>
    <a class="phone" href="tel:5555555555">(555) 555-5555</a>
  </div>
</header>"""

html = html.replace(old_header_html, new_header_html)

# 3. Revert Hero HTML to display the SVG logo image
old_hero_top = """    <div class="hero-left">
      <div class="hero-left-top">
        <a class="wordmark hero-wordmark" href="https://www.centerstreetlending.com/">CENTER STREET <span>LENDING</span></a>
        <div class="hero-eyebrow">CSL Resale Advantage Program</div>"""

new_hero_top = """    <div class="hero-left">
      <div class="hero-left-top">
        <img src="logo1.svg" alt="Center Street Lending" style="height: 36px; width: auto; display: block; margin-bottom: 8px;">
        <div class="hero-eyebrow">CSL Resale Advantage Program</div>"""

html = html.replace(old_hero_top, new_hero_top)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Reverted back to previous version successfully!")
