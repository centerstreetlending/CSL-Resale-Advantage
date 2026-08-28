file_path = '/Users/gregmontoya/AntiGravity Workspaces/Paul_Project_1/CSL-Resale-Advantage/resale-advantage-v3/csl-investor-exit-advantage-v3.html'
with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Replace the eyebrow text with "CSL Resale Advantage Program"
html = html.replace(
    '<div class="hero-eyebrow">Pre-negotiated exclusively for CSL borrowers</div>',
    '<div class="hero-eyebrow">CSL Resale Advantage Program</div>'
)

# 2. Remove the duplicate H2 header "CSL Resale Advantage Program" from under the H1 to avoid redundancy
html = html.replace(
    '        <h2>CSL Resale Advantage Program</h2>',
    ''
)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Eyebrow updated and redundant H2 removed!")
