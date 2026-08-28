file_path = '/Users/gregmontoya/AntiGravity Workspaces/Paul_Project_1/CSL-Resale-Advantage/resale-advantage-v3/csl-investor-exit-advantage-v3.html'
with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Change the font-size of the sticky header title (.program-title) from 1.3rem to 1.45rem to make it stand out more.
old_styles = """  .program-title { 
    display: inline-block; 
    font-size: 1.3rem; 
    font-weight: 700; 
    color: var(--navy); 
    letter-spacing: -0.019em; 
  }"""

new_styles = """  .program-title { 
    display: inline-block; 
    font-size: 1.45rem; 
    font-weight: 700; 
    color: var(--navy); 
    letter-spacing: -0.019em; 
  }"""

html = html.replace(old_styles, new_styles)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Sticky header program title resized larger!")
