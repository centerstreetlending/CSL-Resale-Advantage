file_path = '/Users/gregmontoya/AntiGravity Workspaces/Paul_Project_1/CSL-Resale-Advantage/resale-advantage-v3/csl-investor-exit-advantage-v3.html'
with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Change the margin-top from -60px to -130px to push the ticker card significantly higher
html = html.replace(
    'margin-top: -60px;',
    'margin-top: -130px;'
)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Ticker card shifted significantly higher!")
