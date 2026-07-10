import re

with open('csl-investor-exit-advantage-v3.html', 'r') as f:
    text = f.read()

text = re.sub(r'\.who-eyebrow \{ color: var\(--accent\); font-size: 16px;', r'.who-eyebrow { color: var(--accent); font-size: var(--text-micro);', text)

with open('csl-investor-exit-advantage-v3.html', 'w') as f:
    f.write(text)
