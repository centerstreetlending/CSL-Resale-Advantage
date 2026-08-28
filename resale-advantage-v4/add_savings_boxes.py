file_path = '/Users/gregmontoya/AntiGravity Workspaces/Paul_Project_1/CSL-Resale-Advantage/resale-advantage-v3/csl-investor-exit-advantage-v3.html'
with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Add CSS for .hero-savings and .save
boxes_css = """  .hero-savings { display: flex; gap: 14px; flex-wrap: wrap; margin: 22px 0 26px; }
  .save { background: rgba(255,255,255,.07); border: 1px solid rgba(255,255,255,.16); border-radius: 12px; padding: 12px 18px; min-width: 140px; }
  .save strong { display: block; font-size: 1.7rem; font-weight: 800; color: #F2BD63; line-height: 1; }
  .save span { display: block; font-size: .68rem; color: rgba(255,255,255,.72); text-transform: uppercase; letter-spacing: .04em; margin-top: 5px; }"""

# We'll inject this inside the style tag. Let's find a good hook.
html = html.replace(
    '.hero-right { width: 340px; flex-shrink: 0; padding: 26px 22px; background: rgba(255, 255, 255, 0.06); border: 1px solid rgba(255,255,255,.16); border-radius: 18px; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 24px; }',
    '.hero-right { width: 340px; flex-shrink: 0; padding: 26px 22px; background: rgba(255, 255, 255, 0.06); border: 1px solid rgba(255,255,255,.16); border-radius: 18px; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 24px; }\n' + boxes_css
)

# 2. Replace the HTML bullets list with the horizontal savings boxes
old_list = """        <ul class="bullets">
          <li>1% exclusive listing fee</li>
          <li>Seller escrow as low as $500</li>
          <li>20k buyer views in 21 days</li>
        </ul>"""

new_boxes = """        <div class="hero-savings">
          <div class="save"><strong>1%</strong><span>Exclusive listing fee</span></div>
          <div class="save"><strong>$500</strong><span>Seller escrow, as low as</span></div>
          <div class="save"><strong>20K</strong><span>Buyer views in 21 days</span></div>
        </div>"""

html = html.replace(old_list, new_boxes)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Horizontal savings boxes restored!")
