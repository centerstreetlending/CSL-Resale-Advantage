file_path = '/Users/gregmontoya/AntiGravity Workspaces/Paul_Project_1/CSL-Resale-Advantage/resale-advantage-v3/csl-investor-exit-advantage-v3.html'
with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Add CSS for .hero-intro-text
intro_css = """  .hero-intro-text {
    font-size: 0.72rem;
    font-weight: 700;
    color: rgba(255, 255, 255, 0.6);
    text-transform: uppercase;
    letter-spacing: 0.15em;
    display: block;
    margin-bottom: 8px;
  }"""

html = html.replace(
    '.hero-right { width: 340px; flex-shrink: 0; padding: 26px 22px; background: rgba(255, 255, 255, 0.06); border: 1px solid rgba(255,255,255,.16); border-radius: 18px; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 24px; margin-top: -130px; }',
    '.hero-right { width: 340px; flex-shrink: 0; padding: 26px 22px; background: rgba(255, 255, 255, 0.06); border: 1px solid rgba(255,255,255,.16); border-radius: 18px; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 24px; margin-top: -130px; }\n' + intro_css
)

# 2. Add the HTML text line above the eyebrow badge
html = html.replace(
    '<div class="hero-eyebrow">CSL Resale Advantage Program</div>',
    '<span class="hero-intro-text">Introducing the</span>\n        <div class="hero-eyebrow">CSL Resale Advantage Program</div>'
)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Introducing text added above the program badge!")
