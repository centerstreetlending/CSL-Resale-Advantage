import re

with open('csl-investor-exit-advantage-v3.html', 'r') as f:
    text = f.read()

# 1. Standardize section padding
text = re.sub(r'section\{padding:56px 0\}', r'section{padding:80px 0}', text)
text = re.sub(r'\.who-its-for-v2 \{ background: #fff; padding: 90px;', r'.who-its-for-v2 { background: #fff; padding: 80px 0;', text)

# 2. Standardize Eyebrow spacing
text = re.sub(r'\.tl-eyebrow \{\s*font-size: var\(--text-small\); \/\* Standardized to 13\.6px \(~14px\) \*\/\s*font-weight: 700;\s*letter-spacing: 0\.15em; \/\* Standardized \*\/\s*text-transform: uppercase;\s*color: var\(--accent\);\s*text-align: center;\s*margin: 0 0 6px;\s*\}', 
              r'.tl-eyebrow {\n    font-size: var(--text-small);\n    font-weight: 700;\n    letter-spacing: 0.15em;\n    text-transform: uppercase;\n    color: var(--accent);\n    text-align: center;\n    margin: 0 0 12px;\n  }', text)

text = re.sub(r'\.who-eyebrow \{ color: var\(--accent\); font-size: var\(--text-micro\); font-weight: 700; text-transform: uppercase; letter-spacing: 2\.4px; margin: 0; line-height: 20px; \}',
              r'.who-eyebrow { color: var(--accent); font-size: var(--text-micro); font-weight: 700; text-transform: uppercase; letter-spacing: 2.4px; margin: 0 0 12px 0; line-height: 20px; }', text)

text = re.sub(r'\.trust-eyebrow \{\s*font-size: var\(--text-small\); \/\* Standardized to 13\.6px \(~14px\) \*\/\s*font-weight: 700;\s*letter-spacing: 0\.15em; \/\* Standardized \*\/\s*text-transform: uppercase;\s*color: #4683B3; \/\* Brand steel blue \*\/\s*\}',
              r'.trust-eyebrow {\n    font-size: var(--text-small);\n    font-weight: 700;\n    letter-spacing: 0.15em;\n    text-transform: uppercase;\n    color: #4683B3;\n    margin: 0 0 12px 0;\n  }', text)

# 3. Standardize Heading spacing
# .timeline-title
text = re.sub(r'\.timeline-title \{\s*font-size: var\(--text-h2\);\s*font-weight: 700;\s*color: var\(--navy\);\s*text-align: center;\s*margin-bottom: 48px;\s*letter-spacing: -0\.01em;\s*line-height: 1\.25;\s*margin-top: 8px;\s*\}',
              r'.timeline-title {\n    font-size: var(--text-h2);\n    font-weight: 700;\n    color: var(--navy);\n    text-align: center;\n    margin: 0 0 40px 0;\n    letter-spacing: -0.01em;\n    line-height: 1.25;\n  }', text)

# .trust-heading
# Wait, trust-heading has no CSS! Let me check if it does.
# Let's save and then grep for trust-heading to be sure.

with open('csl-investor-exit-advantage-v3.html', 'w') as f:
    f.write(text)
print("Done fixing paddings and eyebrows")
