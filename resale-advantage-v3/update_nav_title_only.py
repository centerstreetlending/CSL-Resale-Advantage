file_path = '/Users/gregmontoya/AntiGravity Workspaces/Paul_Project_1/CSL-Resale-Advantage/resale-advantage-v3/csl-investor-exit-advantage-v3.html'
with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Restore the large program title CSS style (.program-title) and remove the unused .nav-left flex direction overrides
old_nav_css = """  .nav-left { display: flex; align-items: center; }"""

new_nav_css = """  .nav-left { display: flex; align-items: center; }
  .program-title { 
    display: inline-block; 
    font-size: 1.6rem; 
    font-weight: 800; 
    color: var(--navy); 
    letter-spacing: -0.01em; 
    text-transform: uppercase;
  }
  .program-title span {
    color: var(--accent);
  }"""

html = html.replace(old_nav_css, new_nav_css)

# 2. Update Header HTML: Remove the Center Street Lending logo image, place the large capitalized program title
old_header_html = """<header id="sticky-header">
  <div class="wrap">
    <div class="nav-left">
      <a class="wordmark" href="https://www.centerstreetlending.com/"><img src="logo1.svg" alt="Center Street Lending" style="height: 36px; width: auto; display: block;"></a>
    </div>
    <a class="phone" href="tel:5555555555">(555) 555-5555</a>
  </div>
</header>"""

new_header_html = """<header id="sticky-header">
  <div class="wrap">
    <div class="nav-left">
      <span class="program-title">CSL RESALE ADVANTAGE <span>PROGRAM</span></span>
    </div>
    <a class="phone" href="tel:5555555555">(555) 555-5555</a>
  </div>
</header>"""

html = html.replace(old_header_html, new_header_html)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Corporate logo removed from header; large program title restored successfully!")
