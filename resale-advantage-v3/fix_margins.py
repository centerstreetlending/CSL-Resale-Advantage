import re

file_path = '/Users/gregmontoya/AntiGravity Workspaces/Paul_Project_1/CSL-Resale-Advantage/resale-advantage-v3/csl-investor-exit-advantage-v3.html'
with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update header padding
html = html.replace('header { background: #fff; padding: 17px 90px; height: 72px; border: none; }', 
                    'header { background: #fff; padding: 16px 0; height: 72px; border: none; }')

# 2. Update header wrap max-width and padding
html = html.replace('header .wrap { max-width: 1588px; display: flex; align-items: center; justify-content: space-between; margin: 0 auto; padding: 0; }', 
                    'header .wrap { max-width: 1080px; display: flex; align-items: center; justify-content: space-between; margin: 0 auto; padding: 0 24px; }')

# 3. Update hero padding 
html = html.replace("background-blend-mode: multiply, normal, normal; padding: 90px;", 
                    "background-blend-mode: multiply, normal, normal; padding: 72px 24px;")

# 4. Update hero main row max-width
html = html.replace(".hero-main-row { display: flex; align-items: flex-start; justify-content: space-between; width: 100%; max-width: 1588px; gap: 48px; }", 
                    ".hero-main-row { display: flex; align-items: flex-start; justify-content: space-between; width: 100%; max-width: 1080px; gap: 44px; margin: 0 auto; }")

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Margins updated successfully.")
