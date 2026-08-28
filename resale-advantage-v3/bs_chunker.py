from bs4 import BeautifulSoup
import os
import re

with open("csl-investor-exit-advantage-v3.html", "r") as f:
    html = f.read()

# Replace fonts
html = re.sub(r'^\s*@font-face\s*\{\s*font-family:\s*\'Arteria Std Compress\';\s*src:\s*local\(\'Arteria Std Compress\'\);\s*font-display:\s*swap;\s*\}', '', html, flags=re.MULTILINE)
html = html.replace("'Arteria Std Compress', 'Bebas Neue', sans-serif", "'Bebas Neue', 'Roboto', sans-serif")

soup = BeautifulSoup(html, 'html.parser')

# Extract CSS and Script
styles = soup.find_all("style")
scripts = soup.find_all("script")

css_content = ""
for style in styles:
    css_content += str(style)

script_content = ""
for script in scripts:
    script_content += str(script)

# Chunk CSS safely
css_chunks = []
current_chunk = "<style>\n@import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;700;900&family=Cormorant+Garamond:wght@600;700&family=Bebas+Neue&family=Inter:wght@400;700&display=swap');\n@import url('https://use.typekit.net/sjt3vdj.css');\n"

blocks = css_content.replace("<style>", "").replace("</style>", "").split('}')
for i, block in enumerate(blocks):
    if not block.strip():
        continue
    addition = block + '}\n'
    if len(current_chunk) + len(addition) > 9500:
        current_chunk += "</style>"
        css_chunks.append(current_chunk)
        current_chunk = "<style>\n" + addition
    else:
        current_chunk += addition

if current_chunk != "<style>\n":
    current_chunk += "</style>"
    css_chunks.append(current_chunk)

# Chunk HTML Body safely
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

# Clean and write
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

print(f"Generated {idx-1} perfectly DOM-safe chunks!")
