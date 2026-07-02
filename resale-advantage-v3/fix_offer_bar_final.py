file_path = '/Users/gregmontoya/AntiGravity Workspaces/Paul_Project_1/CSL-Resale-Advantage/resale-advantage-v3/csl-investor-exit-advantage-v3.html'
with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Move .offer-bar OUTSIDE the header (place it below </header> in the HTML)
# This will make it not sticky (only the white header remains sticky)
old_header = """<header id="sticky-header">
  <div class="wrap">
    <div class="nav-left">
      <a class="wordmark" href="https://www.centerstreetlending.com/"><img src="logo1.svg" alt="Center Street Lending" style="height: 36px; width: auto; display: block;"></a>
    </div>
    <a class="phone" href="tel:5555555555">(555) 555-5555</a>
  </div>
  <div class="offer-bar">PRE-NEGOTIATED FOR CSL BORROWERS</div>
</header>"""

new_header = """<header id="sticky-header">
  <div class="wrap">
    <div class="nav-left">
      <a class="wordmark" href="https://www.centerstreetlending.com/"><img src="logo1.svg" alt="Center Street Lending" style="height: 36px; width: auto; display: block;"></a>
    </div>
    <a class="phone" href="tel:5555555555">(555) 555-5555</a>
  </div>
</header>
<div class="offer-bar">PRE-NEGOTIATED FOR CSL BORROWERS</div>"""

html = html.replace(old_header, new_header)

# 2. Update CSS for .offer-bar to remove the box-shadow (which was creating the visual gap/gray space)
# and ensure margins are locked to 0 to prevent any default browser margins from creating white space.
old_css = """  .offer-bar { 
    background: var(--navy-deep); 
    color: #fff; 
    text-align: center; 
    padding: 12px 16px; 
    font-size: 0.92rem; 
    letter-spacing: 0.05em; 
    font-family: 'Roboto', sans-serif; 
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 8px;
    border-bottom: 1px solid rgba(255, 255, 255, 0.08);
    position: relative;
    z-index: 999;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
  }"""

new_css = """  .offer-bar { 
    background: var(--navy-deep); 
    color: #fff; 
    text-align: center; 
    padding: 12px 16px; 
    font-size: 0.92rem; 
    letter-spacing: 0.05em; 
    font-family: 'Roboto', sans-serif; 
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 8px;
    border-bottom: none;
    margin: 0;
  }"""

html = html.replace(old_css, new_css)

# Also ensure header and hero margins/paddings are tight to prevent spacing:
# header margin: 0; hero margin-top: 0;
html = html.replace(
    "  header { \n    background: #fff; ",
    "  header { \n    background: #fff; \n    margin: 0; "
)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Offer bar moved outside header, box-shadow removed, and margins locked to 0!")
