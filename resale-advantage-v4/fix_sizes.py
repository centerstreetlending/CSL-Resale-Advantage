import re

file_path = '/Users/gregmontoya/AntiGravity Workspaces/Paul_Project_1/CSL-Resale-Advantage/resale-advantage-v3/csl-investor-exit-advantage-v3.html'
with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update hero h1
html = html.replace("font-size: 101px; font-weight: 700; text-transform: uppercase; line-height: 90.9px;", 
                    "font-size: 56px; font-weight: 700; line-height: 62px;")
html = html.replace("font-size: 64px; line-height: 64px;", "font-size: 48px; line-height: 52px;")

# 2. Update stat-card num
html = html.replace("font-size: 127px; font-weight: 700; text-transform: uppercase; line-height: 114.3px;", 
                    "font-size: 64px; font-weight: 700; line-height: 64px;")
html = html.replace("font-size: 80px; line-height: 80px;", "font-size: 48px; line-height: 48px;")

# 3. Update optin section (it doesn't have a 101px header, it has normal `h2`)
# Wait, I noticed #optin h2 might be using standard h2 styles (1.7rem) since we removed Arteria.

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Font sizes updated.")
