file_path = '/Users/gregmontoya/AntiGravity Workspaces/Paul_Project_1/CSL-Resale-Advantage/resale-advantage-v3/csl-investor-exit-advantage-v3.html'
with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Change the .save strong text color from gold (#F2BD63) to CSL brand steel blue (var(--accent))
html = html.replace(
    '.save strong { display: block; font-size: 1.7rem; font-weight: 800; color: #F2BD63; line-height: 1; }',
    '.save strong { display: block; font-size: 1.7rem; font-weight: 800; color: var(--accent); line-height: 1; }'
)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Savings boxes font color updated to brand blue.")
