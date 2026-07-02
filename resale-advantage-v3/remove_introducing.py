file_path = '/Users/gregmontoya/AntiGravity Workspaces/Paul_Project_1/CSL-Resale-Advantage/resale-advantage-v3/csl-investor-exit-advantage-v3.html'
with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Remove the "Introducing" eyebrow element completely
html = html.replace(
    '        <div class="hero-eyebrow">Introducing</div>\n',
    ''
)
html = html.replace(
    '        <div class="hero-eyebrow">Introducing</div>',
    ''
)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Introducing eyebrow removed!")
