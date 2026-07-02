file_path = '/Users/gregmontoya/AntiGravity Workspaces/Paul_Project_1/CSL-Resale-Advantage/resale-advantage-v3/csl-investor-exit-advantage-v3.html'
with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Change the text color of the program name eyebrow (.hero-eyebrow) from white (#fff) to brand steel blue (var(--accent))
# so it stands out cleanly against the dark hero background.
html = html.replace(
    '    color: #fff; \n    font-size: 0.95rem;',
    '    color: var(--accent); \n    font-size: 0.95rem;'
)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Eyebrow text color changed to brand blue!")
