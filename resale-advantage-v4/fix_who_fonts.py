import re

with open('csl-investor-exit-advantage-v3.html', 'r') as f:
    text = f.read()

replacements = [
    (r'\.who-left h2 \{ font-size: 32px;', r'.who-left h2 { font-size: var(--text-h2);'),
    (r'\.who-intro \{ font-size: 20px;', r'.who-intro { font-size: var(--text-lead);'),
    (r'\.who-item h3 \{ font-size: 24px;', r'.who-item h3 { font-size: var(--text-h3);'),
    (r'\.who-item p \{ font-size: 20px;', r'.who-item p { font-size: var(--text-body);'),
]

for old, new in replacements:
    text = re.sub(old, new, text)

with open('csl-investor-exit-advantage-v3.html', 'w') as f:
    f.write(text)
