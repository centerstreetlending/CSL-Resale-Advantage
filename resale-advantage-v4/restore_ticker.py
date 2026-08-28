file_path = '/Users/gregmontoya/AntiGravity Workspaces/Paul_Project_1/CSL-Resale-Advantage/resale-advantage-v3/csl-investor-exit-advantage-v3.html'
with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Add CSS for ticker labels, numbers, and subtext
ticker_css = """  .tk-label { display: block; font-size: .7rem; text-transform: uppercase; letter-spacing: .09em; color: rgba(255,255,255,.7); text-align: center; }
  .tk-num { display: block; font-size: 3.8rem; font-weight: 800; color: #fff; line-height: 1.05; margin: 8px 0 4px; text-align: center; font-family: 'Roboto', sans-serif; }
  .tk-sub { font-size: .84rem; color: rgba(255,255,255,.82); line-height: 1.4; text-align: center; }"""

html = html.replace(
    '.hero-right { width: 340px; flex-shrink: 0; padding: 26px 22px; background: rgba(255, 255, 255, 0.06); border: 1px solid rgba(255,255,255,.16); border-radius: 18px; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 24px; }',
    '.hero-right { width: 340px; flex-shrink: 0; padding: 26px 22px; background: rgba(255, 255, 255, 0.06); border: 1px solid rgba(255,255,255,.16); border-radius: 18px; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 24px; }\n' + ticker_css
)

# 2. Replace the HTML inside hero-right with the V2 ticker structure
old_hero_right = """    <div class="hero-right">
      <div class="stat-card">
        <div class="num">100+</div>
        <div class="sub">CSL Borrowers selling Properties through CSL Resale Advantage Program</div>
      </div>
      <div class="stat-card">
        <div class="num">$2.4M+</div>
        <div class="sub">Estimated Total Exit Cost Savings with CSL Resale Advantage Program</div>
      </div>
    </div>"""

new_hero_right = """    <div class="hero-right">
      <span class="tk-label">Borrowers using the program</span>
      <span class="tk-num" id="deal-ticker" data-target="100">0</span>
      <span class="tk-sub">homes sold through CSL Resale Advantage</span>
    </div>"""

html = html.replace(old_hero_right, new_hero_right)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("V2 ticker successfully restored in V3!")
