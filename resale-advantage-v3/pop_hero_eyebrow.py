file_path = '/Users/gregmontoya/AntiGravity Workspaces/Paul_Project_1/CSL-Resale-Advantage/resale-advantage-v3/csl-investor-exit-advantage-v3.html'
with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update the HTML of the eyebrow to wrap the word "PROGRAM" in a span
old_eyebrow_html = '<div class="hero-eyebrow">CSL RESALE ADVANTAGE PROGRAM</div>'
new_eyebrow_html = '<div class="hero-eyebrow">CSL RESALE ADVANTAGE <span>PROGRAM</span></div>'

html = html.replace(old_eyebrow_html, new_eyebrow_html)

# 2. Update CSS for .hero-eyebrow:
# - Increase border-left width to 5px (bolder visual anchor line)
# - Set font-weight to 800 (extra bold)
# - Scale font-size slightly to 1.05rem
# - Increase letter-spacing to 0.15em for that modern premium spaced look
# - Style nested span with var(--accent) (brand blue) to make "PROGRAM" pop!

old_css = """  .hero-eyebrow { 
    display: inline-block; 
    align-self: flex-start; 
    border-left: 4px solid var(--accent); 
    color: var(--accent); 
    font-size: 1rem; 
    font-weight: 700; 
    text-transform: uppercase; 
    letter-spacing: 0.12em; 
    padding: 2px 0 2px 16px; 
    margin-bottom: 20px; 
    background: none;
  }"""

# Note: In revert_eyebrow_color.py, we reverted "color: var(--accent);" back to "color: #fff;"
# Let's verify the exact CSS in the file currently (it has color: #fff;)
old_css_white = """  .hero-eyebrow { 
    display: inline-block; 
    align-self: flex-start; 
    border-left: 4px solid var(--accent); 
    color: #fff; 
    font-size: 1rem; 
    font-weight: 700; 
    text-transform: uppercase; 
    letter-spacing: 0.12em; 
    padding: 2px 0 2px 16px; 
    margin-bottom: 20px; 
    background: none;
  }"""

new_css = """  .hero-eyebrow { 
    display: inline-block; 
    align-self: flex-start; 
    border-left: 5px solid var(--accent); 
    color: #fff; 
    font-size: 1.05rem; 
    font-weight: 800; 
    text-transform: uppercase; 
    letter-spacing: 0.15em; 
    padding: 2px 0 2px 16px; 
    margin-bottom: 20px; 
    background: none;
  }
  .hero-eyebrow span {
    color: var(--accent);
  }"""

# Try replacing both variations to be safe
html = html.replace(old_css_white, new_css)
html = html.replace(old_css, new_css)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Hero eyebrow updated to stand out with color-accented 'PROGRAM', bolder font, and wider accent line!")
