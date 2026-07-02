import re

with open('csl-investor-exit-advantage-v3.html', 'r') as f:
    text = f.read()

# Fix section-title margin
text = re.sub(r'\.section-title \{ color: var\(--navy-darkest, #2C3842\); font-size: var\(--text-h2\); font-weight: 700; line-height: 40px; margin-bottom: 12px; \}',
              r'.section-title { color: var(--navy-darkest, #2C3842); font-size: var(--text-h2); font-weight: 700; line-height: 40px; margin-bottom: 24px; }', text)

with open('csl-investor-exit-advantage-v3.html', 'w') as f:
    f.write(text)
print("Done fixing section-title")
