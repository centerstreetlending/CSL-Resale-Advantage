file_path = '/Users/gregmontoya/AntiGravity Workspaces/Paul_Project_1/CSL-Resale-Advantage/resale-advantage-v3/csl-investor-exit-advantage-v3.html'
with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Replace the lowercase text with capitalized text as requested
old_tag = "<b>EXCLUSIVE OFFER</b> &mdash; pre-negotiated for CSL borrowers"
new_tag = "<b>EXCLUSIVE OFFER</b> &mdash; PRE-NEGOTIATED FOR CSL BORROWERS"

html = html.replace(old_tag, new_tag)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Tag text capitalized successfully!")
