file_path = '/Users/gregmontoya/AntiGravity Workspaces/Paul_Project_1/CSL-Resale-Advantage/resale-advantage-v3/csl-investor-exit-advantage-v3.html'
with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update the CSS for .program-title:
# - Increase size to 1.6rem
# - Add text-transform: uppercase
# - Tune letter-spacing to -0.01em for clean presentation
old_styles = """  .program-title { 
    display: inline-block; 
    font-size: 1.45rem; 
    font-weight: 700; 
    color: var(--navy); 
    letter-spacing: -0.019em; 
  }"""

new_styles = """  .program-title { 
    display: inline-block; 
    font-size: 1.6rem; 
    font-weight: 800; 
    color: var(--navy); 
    letter-spacing: -0.01em; 
    text-transform: uppercase;
  }"""

html = html.replace(old_styles, new_styles)

# 2. Update the HTML to capitalized words
old_html = '<span class="program-title">CSL Resale Advantage <span>Program</span></span>'
new_html = '<span class="program-title">CSL Resale Advantage <span>Program</span></span>' # text-transform will handle it, but let's change text casing as well for cleanliness
html = html.replace(old_html, '<span class="program-title">CSL RESALE ADVANTAGE <span>PROGRAM</span></span>')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Header program title capitalized and resized larger!")
