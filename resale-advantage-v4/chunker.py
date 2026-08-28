import re
import os

with open("csl-investor-exit-advantage-v4.html", "r") as f:
    html = f.read()

# 1. Extract CSS safely
css_match = re.search(r'<style>(.*?)</style>', html, re.DOTALL)
if css_match:
    css_content = css_match.group(1)
else:
    css_content = ""

# Strip the font-face block from css
css_content = re.sub(r'^\s*@font-face\s*\{\s*font-family:\s*\'Arteria Std Compress\';\s*src:\s*local\(\'Arteria Std Compress\'\);\s*font-display:\s*swap;\s*\}', '', css_content, flags=re.MULTILINE)
css_content = css_content.replace("'Arteria Std Compress', 'Bebas Neue', sans-serif", "'Bebas Neue', 'Roboto', sans-serif")

css_chunks = []
current_chunk = "<style>\n@import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;700;900&family=Cormorant+Garamond:wght@600;700&family=Bebas+Neue&family=Inter:wght@400;700&display=swap');\n@import url('https://use.typekit.net/sjt3vdj.css');\n"

bracket_count = 0
start = 0
for i, char in enumerate(css_content):
    if char == '{':
        bracket_count += 1
    elif char == '}':
        bracket_count -= 1
        if bracket_count == 0:
            rule = css_content[start:i+1]
            if len(current_chunk) + len(rule) > 9500:
                current_chunk += "</style>"
                css_chunks.append(current_chunk)
                current_chunk = "<style>\n" + rule
            else:
                current_chunk += rule
            start = i+1

if current_chunk != "<style>\n" and current_chunk != "<style>\n</style>":
    current_chunk += css_content[start:]
    current_chunk += "\n</style>"
    css_chunks.append(current_chunk)


# 2. Extract HTML Body safely
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')
body = soup.find("body")
html_chunks = []
current_html = ""

for child in body.children:
    if child.name in ["style", "script", "link"]:
        continue
    
    addition = str(child)
    if not addition.strip():
        continue
        
    if len(current_html) + len(addition) > 9500:
        if current_html:
            html_chunks.append(current_html)
        current_html = addition
    else:
        current_html += addition

if current_html:
    html_chunks.append(current_html)

# Extract Script
script_match = re.search(r'(<script>.*?</script>)', html, re.DOTALL)
script_content = script_match.group(1) if script_match else ""

# Save all chunks
os.system("rm -f webflow_embeds/*.txt")
idx = 1
for chunk in css_chunks:
    with open(f"webflow_embeds/{idx:02d}_css.txt", "w") as f:
        f.write(chunk)
    idx += 1

for chunk in html_chunks:
    with open(f"webflow_embeds/{idx:02d}_html.txt", "w") as f:
        f.write(chunk)
    idx += 1

if script_content:
    with open(f"webflow_embeds/{idx:02d}_script.txt", "w") as f:
        f.write(script_content)

print(f"Generated {idx-1} safe chunks!")
