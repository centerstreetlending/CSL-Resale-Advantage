import re

with open('csl-investor-exit-advantage-v3.html', 'r') as f:
    content = f.read()

# Replace general tags
content = re.sub(r'h2\{font-size:[^;]+;', r'h2{font-size:var(--text-h2);', content)
content = re.sub(r'\.btn\{[^}]*font-size:[^;]+;', lambda m: m.group(0).replace(re.search(r'font-size:[^;]+;', m.group(0)).group(0), 'font-size:var(--text-body);'), content)

# I will just write a script to replace specific patterns.
