import os
import re

with open("csl-investor-exit-advantage-v3.html", "r") as f:
    html = f.read()

html = re.sub(r'^\s*@font-face\s*\{\s*font-family:\s*\'Arteria Std Compress\';\s*src:\s*local\(\'Arteria Std Compress\'\);\s*font-display:\s*swap;\s*\}', '', html, flags=re.MULTILINE)
html = html.replace("'Arteria Std Compress', 'Bebas Neue', sans-serif", "'Bebas Neue', 'Roboto', sans-serif")

css_match = re.search(r'<style>(.*?)</style>', html, re.DOTALL)
css_content = css_match.group(1) if css_match else ""

chunks = []
current_chunk = "<style>\n@import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;700;900&family=Cormorant+Garamond:wght@600;700&family=Bebas+Neue&family=Inter:wght@400;700&display=swap');\n@import url('https://use.typekit.net/sjt3vdj.css');\n"
brace_count = 0
in_comment = False
i = 0

while i < len(css_content):
    if css_content[i:i+2] == '/*' and not in_comment:
        in_comment = True
        current_chunk += '/*'
        i += 2
        continue
    elif css_content[i:i+2] == '*/' and in_comment:
        in_comment = False
        current_chunk += '*/'
        i += 2
        continue
        
    if not in_comment:
        if css_content[i] == '{':
            brace_count += 1
        elif css_content[i] == '}':
            brace_count -= 1
            
    current_chunk += css_content[i]
    
    if brace_count == 0 and not in_comment and css_content[i] == '}':
        # Root level end! Can chunk if getting large
        if len(current_chunk) > 8500:
            current_chunk += "\n</style>"
            chunks.append(current_chunk)
            current_chunk = "<style>\n"
            
    i += 1

if current_chunk.strip() != "<style>\n":
    current_chunk += "\n</style>"
    chunks.append(current_chunk)

# Write CSS chunks over the old ones
idx = 1
for chunk in chunks:
    with open(f"webflow_embeds/{idx:02d}_css.txt", "w") as f:
        f.write(chunk)
    idx += 1

print(f"Generated {idx-1} perfect CSS chunks!")
