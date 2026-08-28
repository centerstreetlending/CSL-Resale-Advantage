import re

with open('csl-investor-exit-advantage-v3.html', 'r') as f:
    text = f.read()

# Make timeline-title margin-bottom match trust-heading (20px)
text = re.sub(r'\.timeline-title \{\s*font-size: var\(--text-h2\);\s*font-weight: 700;\s*color: var\(--navy\);\s*text-align: center;\s*margin: 0 0 40px 0;\s*letter-spacing: -0\.01em;\s*line-height: 1\.25;\s*\}',
              r'.timeline-title {\n    font-size: var(--text-h2);\n    font-weight: 700;\n    color: var(--navy);\n    text-align: center;\n    margin: 0 0 24px 0;\n    letter-spacing: -0.01em;\n    line-height: 1.25;\n  }', text)

# Make trust-heading margin-bottom 24px (middle ground between 20 and 32)
text = re.sub(r'margin: 0 0 20px;', r'margin: 0 0 24px;', text)

# Ensure who-left-top gap is 24px (already is, let's verify)
# .who-left-top { display: flex; flex-direction: column; gap: 24px; }

with open('csl-investor-exit-advantage-v3.html', 'w') as f:
    f.write(text)
print("Done fixing heading margins")
