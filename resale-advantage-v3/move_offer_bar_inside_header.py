file_path = '/Users/gregmontoya/AntiGravity Workspaces/Paul_Project_1/CSL-Resale-Advantage/resale-advantage-v3/csl-investor-exit-advantage-v3.html'
with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Remove the standalone offer-bar from below the header
html = html.replace(
    '</header>\n<div class="offer-bar">PRE-NEGOTIATED FOR CSL BORROWERS</div>',
    '</header>'
)

# 2. Place it INSIDE the header element, right at the bottom (before </header>)
# This guarantees it renders inside the sticky wrapper and cannot be covered or hidden.
old_header_structure = """<header id="sticky-header">
  <div class="wrap">
    <div class="nav-left">
      <a class="wordmark" href="https://www.centerstreetlending.com/"><img src="logo1.svg" alt="Center Street Lending" style="height: 36px; width: auto; display: block;"></a>
    </div>
    <a class="phone" href="tel:5555555555">(555) 555-5555</a>
  </div>
</header>"""

new_header_structure = """<header id="sticky-header">
  <div class="wrap">
    <div class="nav-left">
      <a class="wordmark" href="https://www.centerstreetlending.com/"><img src="logo1.svg" alt="Center Street Lending" style="height: 36px; width: auto; display: block;"></a>
    </div>
    <a class="phone" href="tel:5555555555">(555) 555-5555</a>
  </div>
  <div class="offer-bar">PRE-NEGOTIATED FOR CSL BORROWERS</div>
</header>"""

html = html.replace(old_header_structure, new_header_structure)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Offer bar successfully moved inside the sticky header element!")
