file_path = '/Users/gregmontoya/AntiGravity Workspaces/Paul_Project_1/CSL-Resale-Advantage/resale-advantage-v3/csl-investor-exit-advantage-v3.html'
with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Replace the em-dash (&mdash; or —) with the ellipsis (...) as requested
html = html.replace(
    'You found it, improved it, and rehabbed it &mdash; now list it at <strong>1%</strong> and close for less.',
    'You found it, improved it, and rehabbed it... now list it at <strong>1%</strong> and close for less.'
)
html = html.replace(
    'You found it, improved it, and rehabbed it — now list it at <strong>1%</strong> and close for less.',
    'You found it, improved it, and rehabbed it... now list it at <strong>1%</strong> and close for less.'
)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Lead copy updated with ellipsis.")
