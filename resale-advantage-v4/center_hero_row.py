file_path = '/Users/gregmontoya/AntiGravity Workspaces/Paul_Project_1/CSL-Resale-Advantage/resale-advantage-v3/csl-investor-exit-advantage-v3.html'
with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Change align-items from flex-start to center for the hero container row
html = html.replace(
    '.hero-main-row { display: flex; align-items: flex-start; justify-content: space-between; width: 100%; max-width: 1200px; gap: 44px; margin: 0 auto; }',
    '.hero-main-row { display: flex; align-items: center; justify-content: space-between; width: 100%; max-width: 1200px; gap: 44px; margin: 0 auto; }'
)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Hero content centered top to bottom!")
