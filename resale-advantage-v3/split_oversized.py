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
    if len(current_chunk) + len(addition) > 9000:
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

parts = re.split(r"(<div class=\"offer-bar\"|<header|<section|<footer)", html_content)
sections = []
for i in range(1, len(parts), 2):
    sections.append(parts[i] + parts[i+1])

html_chunks = []
current_html = ""

def add_chunk(chunk):
    global current_html
    if len(current_html) + len(chunk) > 9000:
        if current_html.strip():
            html_chunks.append(current_html)
        current_html = chunk
    else:
        current_html += chunk

for s in sections:
    if len(s) > 9500:
        if 'class="soft"' in s and 'class="benefit"' in s:
            # Split benefits section
            b_parts = s.split('<div class="benefit">')
            if len(b_parts) > 4:
                chunk1 = b_parts[0] + '<div class="benefit">' + '<div class="benefit">'.join(b_parts[1:5]) + '</div></div></section>'
                chunk2 = '<section class="soft" style="padding-top:0"><div class="wrap"><div class="grid-2"><div class="benefit">' + '<div class="benefit">'.join(b_parts[5:])
                add_chunk(chunk1)
                add_chunk(chunk2)
            else:
                add_chunk(s)
        elif '<footer' in s:
            # Footer is ~10090 bytes. Minify it to get it under 9500.
            minified = re.sub(r"\s+", " ", s)
            add_chunk(minified)
        else:
            add_chunk(s)
    else:
        add_chunk(s)

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

