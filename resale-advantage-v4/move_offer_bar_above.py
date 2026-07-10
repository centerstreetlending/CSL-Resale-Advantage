file_path = '/Users/gregmontoya/AntiGravity Workspaces/Paul_Project_1/CSL-Resale-Advantage/resale-advantage-v3/csl-investor-exit-advantage-v3.html'
with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Remove the offer-bar from below the header
html = html.replace(
    '</header>\n<div class="offer-bar">PRE-NEGOTIATED FOR CSL BORROWERS</div>',
    '</header>'
)

# 2. Place the offer-bar ABOVE the header (very top of the page)
target_header = '<header id="sticky-header">'
replacement_markup = """<div class="offer-bar">PRE-NEGOTIATED FOR CSL BORROWERS</div>

<header id="sticky-header">"""

html = html.replace(target_header, replacement_markup)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Offer bar successfully moved back above the navigation header!")
