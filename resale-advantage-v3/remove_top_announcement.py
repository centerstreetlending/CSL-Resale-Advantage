file_path = '/Users/gregmontoya/AntiGravity Workspaces/Paul_Project_1/CSL-Resale-Advantage/resale-advantage-v3/csl-investor-exit-advantage-v3.html'
with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Remove the top black announcement bar (.offer-bar) completely from the HTML
old_offer_bar = """<div class="offer-bar"><span style="display: inline-flex; align-items: center; gap: 6px; white-space: nowrap;"><span class="offer-pulse"></span><b>EXCLUSIVE OFFER</b></span> &mdash; pre-negotiated for CSL borrowers</div>\n\n"""

# Try both formatted and unformatted variations to guarantee match
html = html.replace(old_offer_bar, "")
html = html.replace("""<div class="offer-bar"><span style="display: inline-flex; align-items: center; gap: 6px; white-space: nowrap;"><span class="offer-pulse"></span><b>EXCLUSIVE OFFER</b></span> &mdash; pre-negotiated for CSL borrowers</div>""", "")

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Top announcement bar removed successfully!")
