file_path = '/Users/gregmontoya/AntiGravity Workspaces/Paul_Project_1/CSL-Resale-Advantage/resale-advantage-v3/csl-investor-exit-advantage-v3.html'
with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Replace the phone link to remove the word "Call "
html = html.replace(
    '<a class="phone" href="tel:5555555555">Call (555) 555-5555</a>',
    '<a class="phone" href="tel:5555555555">(555) 555-5555</a>'
)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Call text removed from header phone link!")
