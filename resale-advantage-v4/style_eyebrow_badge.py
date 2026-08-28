file_path = '/Users/gregmontoya/AntiGravity Workspaces/Paul_Project_1/CSL-Resale-Advantage/resale-advantage-v3/csl-investor-exit-advantage-v3.html'
with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Replace the plain text eyebrow styling with a clean, high-contrast solid program badge.
# This makes the program name stand out immediately without looking like the old clunky box.

old_eyebrow = '.hero-eyebrow { color: var(--accent); font-size: 16px; font-weight: 700; text-transform: uppercase; letter-spacing: 2.4px; margin-bottom: 12px; }'
new_eyebrow = """.hero-eyebrow { 
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

html = html.replace(old_eyebrow, new_eyebrow)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Eyebrow styled as a clean solid badge!")
