file_path = '/Users/gregmontoya/AntiGravity Workspaces/Paul_Project_1/CSL-Resale-Advantage/resale-advantage-v3/csl-investor-exit-advantage-v3.html'
with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Replace the offer bar CSS with the dark-slate background, gold text b tag styling
old_css = """  .offer-bar { background: var(--accent); color: #fff; text-align: center; padding: 10px 16px; font-size: 16px; display: flex; align-items: center; justify-content: center; gap: 10px; font-family: 'Roboto', sans-serif; }
  .offer-bar span { font-weight: 400; }
  .offer-bar a { font-weight: 700; color: #fff; text-decoration: underline; cursor: pointer; }"""

new_css = """  .offer-bar { background: var(--navy-deep); color: #fff; text-align: center; padding: 9px 16px; font-size: .8rem; letter-spacing: .05em; font-family: 'Roboto', sans-serif; }
  .offer-bar b { color: #F2BD63; font-weight: 700; text-transform: uppercase; }"""

html = html.replace(old_css, new_css)

# 2. Replace the HTML content of the offer bar
old_html = """<div class="offer-bar">
  <span>EXCLUSIVE OFFER: Pre-negotiated savings available exclusively for CSL investors and borrowers.</span>
  <a href="#optin">Request Info &gt;</a>
</div>"""

new_html = """<div class="offer-bar"><b>EXCLUSIVE OFFER</b> &mdash; pre-negotiated for CSL borrowers</div>"""

html = html.replace(old_html, new_html)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Top offer bar updated successfully!")
