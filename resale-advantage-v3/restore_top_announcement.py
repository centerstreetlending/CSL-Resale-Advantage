file_path = '/Users/gregmontoya/AntiGravity Workspaces/Paul_Project_1/CSL-Resale-Advantage/resale-advantage-v3/csl-investor-exit-advantage-v3.html'
with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Insert the top announcement bar HTML right back above the header tag
target_header = '<header id="sticky-header">'
replacement_markup = """<div class="offer-bar"><span style="display: inline-flex; align-items: center; gap: 6px; white-space: nowrap;"><span class="offer-pulse"></span><b>EXCLUSIVE OFFER</b></span> &mdash; pre-negotiated for CSL borrowers</div>

<header id="sticky-header">"""

html = html.replace(target_header, replacement_markup)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Top announcement bar restored successfully!")
