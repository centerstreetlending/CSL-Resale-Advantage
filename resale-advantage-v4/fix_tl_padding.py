import re

with open('csl-investor-exit-advantage-v3.html', 'r') as f:
    text = f.read()

# Fix .tl padding
text = re.sub(r'\.tl \{\s*margin-top: 0;\s*padding: 64px 0 48px;\s*text-align: center;\s*\}',
              r'.tl {\n    margin-top: 0;\n    padding: 0;\n    text-align: center;\n  }', text)

# Just in case the format is slightly different
text = re.sub(r'padding: 64px 0 48px;', r'padding: 0;', text)

# Also let's check trust-copy top padding
text = re.sub(r'\.trust-copy \{\s*color: #fff;\s*padding-top: 10px; \/\* Slight top offset to balance with image borders \*\/\s*\}',
              r'.trust-copy {\n    color: #fff;\n    padding-top: 0;\n  }', text)

with open('csl-investor-exit-advantage-v3.html', 'w') as f:
    f.write(text)
print("Done fixing tl padding")
