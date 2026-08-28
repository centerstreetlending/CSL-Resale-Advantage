file_path = '/Users/gregmontoya/AntiGravity Workspaces/Paul_Project_1/CSL-Resale-Advantage/resale-advantage-v3/csl-investor-exit-advantage-v3.html'
with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Make the badge (eyebrow) a little bigger
old_badge = """.hero-eyebrow { 
    display: inline-block; 
    background: var(--accent); 
    color: #fff; 
    font-size: 0.8rem; 
    font-weight: 700; 
    text-transform: uppercase; 
    letter-spacing: 0.12em; 
    padding: 6px 14px; 
    border-radius: 4px; 
    margin-bottom: 20px; 
  }"""

new_badge = """.hero-eyebrow { 
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

html = html.replace(old_badge, new_badge)

# 2. Make the savings boxes "a little bigger" but limit their max-width to 185px (flex: 1)
# so they fill the horizontal space cleanly without getting stretched like wide rectangles.
old_save = """  .save { 
    background: rgba(255, 255, 255, 0.08); 
    border: 1px solid rgba(255, 255, 255, 0.18); 
    border-radius: 12px; 
    padding: 12px 18px; 
    min-width: 140px; 
    box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
    backdrop-filter: blur(8px);
    -webkit-backdrop-filter: blur(8px);
  }"""

new_save = """  .save { 
    background: rgba(255, 255, 255, 0.08); 
    border: 1px solid rgba(255, 255, 255, 0.18); 
    border-radius: 12px; 
    padding: 14px 20px; 
    min-width: 130px; 
    max-width: 185px; 
    flex: 1; 
    box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
    backdrop-filter: blur(8px);
    -webkit-backdrop-filter: blur(8px);
  }"""

html = html.replace(old_save, new_save)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Badge and savings boxes resized successfully!")
