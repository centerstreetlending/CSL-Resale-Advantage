file_path = '/Users/gregmontoya/AntiGravity Workspaces/Paul_Project_1/CSL-Resale-Advantage/resale-advantage-v3/csl-investor-exit-advantage-v3.html'
with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Change the .offer-bar b color from white (#fff) to brand steel blue (var(--accent))
# so the "EXCLUSIVE OFFER" text in the top announcement bar stands out in your brand blue.
html = html.replace(
    '  .offer-bar b { color: #fff; font-weight: 700; text-transform: uppercase; }',
    '  .offer-bar b { color: var(--accent); font-weight: 700; text-transform: uppercase; }'
)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Top bar EXCLUSIVE OFFER color changed to brand blue!")
