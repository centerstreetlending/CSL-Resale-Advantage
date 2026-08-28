file_path = '/Users/gregmontoya/AntiGravity Workspaces/Paul_Project_1/CSL-Resale-Advantage/resale-advantage-v3/csl-investor-exit-advantage-v3.html'
with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Change the .offer-bar b color from gold (#F2BD63) to white (#fff) as requested to remove the yellow text.
html = html.replace(
    '  .offer-bar b { color: #F2BD63; font-weight: 700; text-transform: uppercase; }',
    '  .offer-bar b { color: #fff; font-weight: 700; text-transform: uppercase; }'
)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Yellow text removed from top offer bar!")
