file_path = '/Users/gregmontoya/AntiGravity Workspaces/Paul_Project_1/CSL-Resale-Advantage/resale-advantage-v3/csl-investor-exit-advantage-v3.html'
with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update CSS for .hero-subheading:
# - Remove text-transform: uppercase
# - Revert letter-spacing to -0.01em (standard look)
# - Keep font-weight: 800 and the vertical blue accent line
old_subheading_css = """  .hero-subheading {
    display: inline-block;
    align-self: flex-start;
    border-left: 5px solid var(--accent);
    color: #fff;
    font-size: 1.25rem;
    font-weight: 800;
    text-transform: uppercase;
    letter-spacing: 0.15em;
    padding: 2px 0 2px 16px;
    margin: 28px 0 20px 0;
    font-family: 'Roboto', sans-serif;
    line-height: 1.0;
  }
  .hero-subheading span {
    color: var(--accent);
  }"""

new_subheading_css = """  .hero-subheading {
    display: inline-block;
    align-self: flex-start;
    border-left: 5px solid var(--accent);
    color: #fff;
    font-size: 1.35rem;
    font-weight: 700;
    letter-spacing: -0.01em;
    padding: 2px 0 2px 16px;
    margin: 28px 0 20px 0;
    font-family: 'Roboto', sans-serif;
    line-height: 1.0;
  }"""

html = html.replace(old_subheading_css, new_subheading_css)

# 2. Update HTML: Revert "CSL RESALE ADVANTAGE PROGRAM" back to title-case "The CSL Resale Advantage"
old_subheading_html = '<h2 class="hero-subheading">CSL RESALE ADVANTAGE <span>PROGRAM</span></h2>'
new_subheading_html = '<h2 class="hero-subheading">The CSL Resale Advantage</h2>'

html = html.replace(old_subheading_html, new_subheading_html)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Subheading reverted back to 'The CSL Resale Advantage' in Title Case with the vertical blue line!")
