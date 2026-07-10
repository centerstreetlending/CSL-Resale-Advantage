file_path = '/Users/gregmontoya/AntiGravity Workspaces/Paul_Project_1/CSL-Resale-Advantage/resale-advantage-v3/csl-investor-exit-advantage-v3.html'
with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Add align-self: flex-start; to .hero-eyebrow to prevent it from stretching to 100% width
# inside the flexbox column container (.hero-left-top). This will shrink-wrap the blue badge
# to the exact width of the program name text.

old_badge = """.hero-eyebrow { 
    display: inline-block; 
    background: var(--accent); 
    color: #fff; 
    font-size: 0.95rem; 
    font-weight: 700; 
    text-transform: uppercase; 
    letter-spacing: 0.12em; 
    padding: 8px 18px; 
    border-radius: 4px; 
    margin-bottom: 20px; 
  }"""

new_badge = """.hero-eyebrow { 
    display: inline-block; 
    align-self: flex-start; 
    background: var(--accent); 
    color: #fff; 
    font-size: 0.95rem; 
    font-weight: 700; 
    text-transform: uppercase; 
    letter-spacing: 0.12em; 
    padding: 8px 18px; 
    border-radius: 4px; 
    margin-bottom: 20px; 
  }"""

html = html.replace(old_badge, new_badge)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Eyebrow badge stretch fixed!")
