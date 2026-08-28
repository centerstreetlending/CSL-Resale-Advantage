file_path = '/Users/gregmontoya/AntiGravity Workspaces/Paul_Project_1/CSL-Resale-Advantage/resale-advantage-v3/csl-investor-exit-advantage-v3.html'
with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update header styles
html = html.replace(
    'header a.phone { color: var(--navy); font-size: 18px; font-weight: 500; text-decoration: none; }',
    'header a.phone { color: var(--navy); font-size: .95rem; font-weight: 600; text-decoration: none; }'
)

# 2. Update hero padding to match V2 exactly
html = html.replace(
    'background-blend-mode: multiply, normal, normal; padding: 72px 24px;',
    'background-blend-mode: multiply, normal, normal; padding: 72px 0 60px;'
)

# 3. Update hero left layout spacing and font sizes
html = html.replace(
    '.hero-left { flex: 1; max-width: 850px; display: flex; flex-direction: column; gap: 48px; }',
    '.hero-left { flex: 1; max-width: 680px; display: flex; flex-direction: column; gap: 28px; }'
)
html = html.replace(
    '.hero-left-top { display: flex; flex-direction: column; gap: 24px; }',
    '.hero-left-top { display: flex; flex-direction: column; gap: 16px; }'
)
html = html.replace(
    '.hero-eyebrow { color: var(--accent); font-size: 16px; font-weight: 700; text-transform: uppercase; letter-spacing: 2.4px; }',
    '.hero-eyebrow { display: inline-block; background: rgba(255,255,255,.12); border: 1px solid rgba(255,255,255,.25); border-radius: 999px; padding: 5px 16px; font-size: .8rem; font-weight: 600; letter-spacing: .08em; text-transform: uppercase; margin-bottom: 4px; color: var(--accent); }'
)
html = html.replace(
    '.hero h1 { font-family: \'Roboto\', sans-serif; font-size: 56px; font-weight: 700; line-height: 62px; color: #fff; margin: 0; letter-spacing: normal; }',
    '.hero h1 { font-family: \'Roboto\', sans-serif; font-size: 3.1rem; font-weight: 700; line-height: 1.1; color: #fff; margin: 0; letter-spacing: -.01em; max-width: 680px; }'
)
html = html.replace(
    '.hero h2 { color: #fff; font-size: 32px; font-weight: 700; line-height: 38.4px; margin: 0; }',
    '.hero h2 { color: #fff; font-size: 1.7rem; font-weight: 700; line-height: 1.2; margin: 0; }'
)
html = html.replace(
    '.hero p.lead { font-size: 20px; font-weight: 400; line-height: 30px; color: #fff; margin: 0; max-width: none; }',
    '.hero p.lead { font-size: 1.15rem; font-weight: 400; line-height: 1.6; color: rgba(255,255,255,.85); margin: 0; max-width: 620px; }'
)
html = html.replace(
    '.hero p.bullets { font-size: 20px; font-weight: 700; line-height: 36px; color: #fff; margin: 0; }',
    '.hero p.bullets { font-size: 1.15rem; font-weight: 700; line-height: 1.6; color: #fff; margin: 0; }'
)

# 4. Update hero CTAs and buttons
html = html.replace(
    '.hero-cta { display: flex; align-items: center; gap: 48px; }',
    '.hero-cta { display: flex; align-items: center; gap: 16px; }'
)
html = html.replace(
    '.hero-cta .btn { font-size: 18px; font-weight: 500; padding: 12px 24px; border-radius: 0; outline: 1px solid var(--accent); display: inline-flex; align-items: center; gap: 12px; }',
    '.hero-cta .btn { font-size: 1rem; font-weight: 600; padding: 14px 32px; border-radius: 6px; display: inline-flex; align-items: center; gap: 12px; }'
)
html = html.replace(
    '.hero-cta .btn-ghost { color: #fff; font-size: 18px; font-weight: 500; text-decoration: underline; padding: 0; }',
    '.hero-cta .btn-ghost { color: rgba(255,255,255,.92); font-size: 1rem; font-weight: 600; text-decoration: underline; padding: 0; }'
)

# 5. Update hero right card sizes
html = html.replace(
    '.hero-right { width: 572px; padding: 64px 32px; background: rgba(255, 255, 255, 0.20); border-radius: 12px; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 64px; }',
    '.hero-right { width: 340px; padding: 26px 22px; background: rgba(255, 255, 255, 0.06); border: 1px solid rgba(255,255,255,.16); border-radius: 18px; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 24px; }'
)
html = html.replace(
    '.stat-card .num { font-family: \'Roboto\', sans-serif; font-size: 64px; font-weight: 700; text-transform: uppercase; line-height: 64px; color: #fff; }',
    '.stat-card .num { font-family: \'Roboto\', sans-serif; font-size: 3.8rem; font-weight: 800; line-height: 1.05; color: #fff; }'
)
html = html.replace(
    '.stat-card .sub { color: #fff; font-size: 20px; font-weight: 700; line-height: 24px; text-align: center; max-width: 400px; }',
    '.stat-card .sub { color: rgba(255,255,255,.82); font-size: .84rem; font-weight: 400; line-height: 1.4; text-align: center; max-width: 400px; }'
)

# 6. Update hero optional text alignment
html = html.replace(
    '.hero-optional { color: #fff; font-size: 16px; font-style: italic; font-weight: 400; line-height: 24px; text-align: center; max-width: none; margin: 0; }',
    '.hero-optional { color: rgba(255,255,255,.5); font-size: .68rem; line-height: 1.4; text-align: left; max-width: 620px; margin-top: 14px; }'
)

# 7. Add wrap class to hero-main-row in HTML to align it perfectly with header
html = html.replace(
    '<div class="hero-main-row">',
    '<div class="wrap hero-main-row">'
)

# 8. Place the hero-optional element INSIDE the hero-left block so it left-aligns properly and behaves like V2
html = html.replace(
    '  </div>\n  \n  <div class="hero-optional">Entirely optional &mdash; you\'re always free to choose your own broker, escrow company, and other providers. Currently limited to California Only.</div>\n</div>',
    '      <div class="hero-optional">Entirely optional &mdash; you\'re always free to choose your own broker, escrow company, and other providers. Currently limited to California Only.</div>\n    </div>\n  </div>\n</div>'
)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Formatting fixed!")
