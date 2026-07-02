file_path = '/Users/gregmontoya/AntiGravity Workspaces/Paul_Project_1/CSL-Resale-Advantage/resale-advantage-v3/csl-investor-exit-advantage-v3.html'
with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Replace the plain text in the offer bar with the original styled EXCLUSIVE OFFER and pulsing dot,
# followed by the capitalized PRE-NEGOTIATED FOR CSL BORROWERS text.
old_bar = '<div class="offer-bar">PRE-NEGOTIATED FOR CSL BORROWERS</div>'
new_bar = '<div class="offer-bar"><span style="display: inline-flex; align-items: center; gap: 6px; white-space: nowrap;"><span class="offer-pulse"></span><b>EXCLUSIVE OFFER</b></span> &mdash; PRE-NEGOTIATED FOR CSL BORROWERS</div>'

html = html.replace(old_bar, new_bar)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Exclusive Offer text and pulsing dot restored to the front of the top bar!")
