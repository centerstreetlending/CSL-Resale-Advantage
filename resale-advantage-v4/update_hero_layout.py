file_path = '/Users/gregmontoya/AntiGravity Workspaces/Paul_Project_1/CSL-Resale-Advantage/resale-advantage-v3/csl-investor-exit-advantage-v3.html'
with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update .hero-eyebrow CSS to remove the box/background
old_eyebrow_css = '.hero-eyebrow { display: inline-block; background: rgba(255,255,255,.12); border: 1px solid rgba(255,255,255,.25); border-radius: 999px; padding: 5px 16px; font-size: .8rem; font-weight: 600; letter-spacing: .08em; text-transform: uppercase; margin-bottom: 4px; color: var(--accent); }'
new_eyebrow_css = '.hero-eyebrow { color: var(--accent); font-size: 16px; font-weight: 700; text-transform: uppercase; letter-spacing: 2.4px; margin-bottom: 12px; }'

html = html.replace(old_eyebrow_css, new_eyebrow_css)

# 2. Update .hero-optional CSS to be centered and span across the page
old_optional_css = '.hero-optional { color: rgba(255,255,255,.5); font-size: .68rem; line-height: 1.4; text-align: left; max-width: 620px; margin-top: 14px; }'
new_optional_css = '.hero-optional { color: rgba(255,255,255,.5); font-size: .85rem; line-height: 1.4; text-align: center; max-width: none; width: 100%; margin-top: 40px; }'

html = html.replace(old_optional_css, new_optional_css)

# 3. Add list styles for .bullets
old_bullets_css = '.hero p.bullets { font-size: 1.15rem; font-weight: 700; line-height: 1.6; color: #fff; margin: 0; }'
new_bullets_css = """ul.bullets { font-size: 1.15rem; font-weight: 700; line-height: 1.6; color: #fff; margin: 0; padding-left: 20px; list-style-type: disc; }
ul.bullets li { margin-bottom: 8px; }"""

html = html.replace(old_bullets_css, new_bullets_css)

# 4. Reconstruct Hero HTML structure
# We need to find the hero section and restructure it.
# Current structure of hero:
# <div class="hero">
#   <div class="wrap hero-main-row">
#     <div class="hero-left">
#       <div class="hero-left-top">
#         <div class="hero-eyebrow">Pre-negotiated exclusively for CSL borrowers</div>
#         <h1>We made it <span class="hl">easier & cheaper</span><br>to exit your investment.</h1>
#         <h2>CSL Resale Advantage Program</h2>
#         <p class="lead">You found it, improved it, and rehabbed it &mdash; now list it at <strong>1%</strong> and close for less. We pre-negotiated an exclusive deal with <strong>Innovate Realty</strong> and <strong>Honest Escrow</strong>, just for CSL borrowers.</p>
#         <p class="bullets">1% exclusive listing fee<br>Seller escrow as low as $500<br>20k buyer views in 21 days</p>
#       </div>
#       <div class="hero-cta">
#         <a class="btn" href="#optin">Request Information <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M12 4l-1.41 1.41L16.17 11H4v2h12.17l-5.58 5.59L12 20l8-8-8-8z" fill="currentColor"/></svg></a>
#         <a class="btn-ghost" href="tel:9492441090">or call 949-244-1090</a>
#       </div>
#       <div class="hero-optional">Entirely optional &mdash; you're always free to choose your own broker, escrow company, and other providers. Currently limited to California Only.</div>
#     </div>
#     ...

# We will replace it with a structure where:
# - Eyebrow is standard text (no box)
# - Title is uppercase
# - Bullets are <ul> <li>
# - hero-optional is placed below wrap hero-main-row, wrapped in <div class="wrap">

# Target left column block:
old_left_col = """    <div class="hero-left">
      <div class="hero-left-top">
        <div class="hero-eyebrow">Pre-negotiated exclusively for CSL borrowers</div>
        <h1>We made it <span class="hl">easier & cheaper</span><br>to exit your investment.</h1>
        <h2>CSL Resale Advantage Program</h2>
        <p class="lead">You found it, improved it, and rehabbed it &mdash; now list it at <strong>1%</strong> and close for less. We pre-negotiated an exclusive deal with <strong>Innovate Realty</strong> and <strong>Honest Escrow</strong>, just for CSL borrowers.</p>
        <p class="bullets">1% exclusive listing fee<br>Seller escrow as low as $500<br>20k buyer views in 21 days</p>
      </div>
      <div class="hero-cta">
        <a class="btn" href="#optin">Request Information <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M12 4l-1.41 1.41L16.17 11H4v2h12.17l-5.58 5.59L12 20l8-8-8-8z" fill="currentColor"/></svg></a>
        <a class="btn-ghost" href="tel:9492441090">or call 949-244-1090</a>
      </div>
      <div class="hero-optional">Entirely optional &mdash; you're always free to choose your own broker, escrow company, and other providers. Currently limited to California Only.</div>
    </div>"""

new_left_col = """    <div class="hero-left">
      <div class="hero-left-top">
        <div class="hero-eyebrow">Pre-negotiated exclusively for CSL borrowers</div>
        <h1>WE MADE IT <span class="hl">EASIER & CHEAPER</span><br>TO EXIT YOUR INVESTMENT.</h1>
        <h2>CSL Resale Advantage Program</h2>
        <p class="lead">You found it, improved it, and rehabbed it &mdash; now list it at <strong>1%</strong> and close for less. We pre-negotiated an exclusive deal with <strong>Innovate Realty</strong> and <strong>Honest Escrow</strong>, just for CSL borrowers.</p>
        <ul class="bullets">
          <li>1% exclusive listing fee</li>
          <li>Seller escrow as low as $500</li>
          <li>20k buyer views in 21 days</li>
        </ul>
      </div>
      <div class="hero-cta">
        <a class="btn" href="#optin">Request Information <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M12 4l-1.41 1.41L16.17 11H4v2h12.17l-5.58 5.59L12 20l8-8-8-8z" fill="currentColor"/></svg></a>
        <a class="btn-ghost" href="tel:9492441090">or call 949-244-1090</a>
      </div>
    </div>"""

html = html.replace(old_left_col, new_left_col)

# Now target the bottom of the hero block to properly position hero-optional:
old_bottom = """    <div class="hero-right">
      <div class="stat-card">
        <div class="num">100+</div>
        <div class="sub">CSL Borrowers selling Properties through CSL Resale Advantage Program</div>
      </div>
      <div class="stat-card">
        <div class="num">$2.4M+</div>
        <div class="sub">Estimated Total Exit Cost Savings with CSL Resale Advantage Program</div>
      </div>
    </div>
    </div>
  </div>
</div>"""

new_bottom = """    <div class="hero-right">
      <div class="stat-card">
        <div class="num">100+</div>
        <div class="sub">CSL Borrowers selling Properties through CSL Resale Advantage Program</div>
      </div>
      <div class="stat-card">
        <div class="num">$2.4M+</div>
        <div class="sub">Estimated Total Exit Cost Savings with CSL Resale Advantage Program</div>
      </div>
    </div>
  </div>
  <div class="wrap">
    <div class="hero-optional">Entirely optional &mdash; you're always free to choose your own broker, escrow company, and other providers. Currently limited to California Only.</div>
  </div>
</div>"""

html = html.replace(old_bottom, new_bottom)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Hero layout updated with bullets, uppercase title, standard eyebrow, and centered full-width optional text.")
