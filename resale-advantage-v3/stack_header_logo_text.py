file_path = '/Users/gregmontoya/AntiGravity Workspaces/Paul_Project_1/CSL-Resale-Advantage/resale-advantage-v3/csl-investor-exit-advantage-v3.html'
with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update CSS styles:
# - Remove the old .program-title styles
# - Add .program-title-sub styling (small, uppercase, stacked spacing, bold, with span color for blue)
old_styles = """  .nav-left { display: flex; align-items: center; }
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

new_styles = """  .nav-left { display: flex; flex-direction: column; align-items: flex-start; gap: 5px; }
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

html = html.replace(old_styles, new_styles)

# Add responsive sizing for the stacked text under media queries (640px query)
html = html.replace(
    "    header a.wordmark img { height: 26px !important; }",
    "    header a.wordmark img { height: 22px !important; }\n    .program-title-sub { font-size: 0.65rem; }"
)

# 2. Update Header HTML: Stack the CSL logo image (logo1.svg) and the program title subtext vertically inside nav-left
old_header_html = """<header id="sticky-header">
  <div class="wrap">
    <div class="nav-left">
      <span class="program-title">CSL RESALE ADVANTAGE <span>PROGRAM</span></span>
    </div>
    <a class="phone" href="tel:5555555555">(555) 555-5555</a>
  </div>
</header>"""

new_header_html = """<header id="sticky-header">
  <div class="wrap">
    <div class="nav-left">
      <a class="wordmark" href="https://www.centerstreetlending.com/"><img src="logo1.svg" alt="Center Street Lending" style="height: 26px; width: auto; display: block;"></a>
      <span class="program-title-sub">CSL RESALE ADVANTAGE <span>PROGRAM</span></span>
    </div>
    <a class="phone" href="tel:5555555555">(555) 555-5555</a>
  </div>
</header>"""

html = html.replace(old_header_html, new_header_html)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("CSL Corporate logo image and CSL RESALE ADVANTAGE PROGRAM subtext stacked vertically in header!")
