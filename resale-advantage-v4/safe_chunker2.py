import re
import os

with open("csl-investor-exit-advantage-v3.html", "r") as f:
    html = f.read()

# Replace fonts
html = re.sub(r'^\s*@font-face\s*\{\s*font-family:\s*\'Arteria Std Compress\';\s*src:\s*local\(\'Arteria Std Compress\'\);\s*font-display:\s*swap;\s*\}', '', html, flags=re.MULTILINE)
html = html.replace("'Arteria Std Compress', 'Bebas Neue', sans-serif", "'Bebas Neue', 'Roboto', sans-serif")

# Extract CSS
css_match = re.search(r'<style>(.*?)</style>', html, re.DOTALL)
css_content = css_match.group(1) if css_match else ""

css_chunks = []
current_chunk = "<style>\n@import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;700;900&family=Cormorant+Garamond:wght@600;700&family=Bebas+Neue&family=Inter:wght@400;700&display=swap');\n@import url('https://use.typekit.net/sjt3vdj.css');\n"

blocks = css_content.split('}')
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

# Extract HTML Body
body_match = re.search(r'<body>(.*?)</body>', html, re.DOTALL)
html_content = body_match.group(1) if body_match else ""

sections = re.split(r'(<div class="offer-bar">|<header id="sticky-header">|<!-- HERO -->|<!-- WHO THIS IS FOR -->|<section class="trust-section">|<section class="timeline-section">|<section id="innolaunch"|<section id="faq"|<section id="honest-escrow-v2"|<section class="exit-cta-v2">|<section class="disclaimer-v2">|<footer>)', html_content)

html_chunks = []
current_html = sections[0]

for i in range(1, len(sections), 2):
    tag = sections[i]
    content = sections[i+1]
    
    addition = tag + content
    
    # If adding this section exceeds limit, push current_html to chunks and start fresh
    if len(current_html) + len(addition) > 9500:
        if current_html.strip():
            html_chunks.append(current_html)
        current_html = addition
    else:
        current_html += addition

if current_html.strip():
    html_chunks.append(current_html)

# Extract Script
script_match = re.search(r'(<script>.*?</script>)', html, re.DOTALL)
script_content = script_match.group(1) if script_match else ""

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

print("Generated chunks!")
