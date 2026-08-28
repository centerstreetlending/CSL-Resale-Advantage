import os
import re

with open("csl-investor-exit-advantage-v3.html", "r") as f:
    content = f.read()

os.makedirs("webflow_embeds", exist_ok=True)

# 1. Chunk CSS
css_match = re.search(r'<style>(.*?)</style>', content, re.DOTALL)
css_content = css_match.group(1)
css_lines = css_content.split('\n')

css_chunks = []
current_chunk = "<style>\n"
for line in css_lines:
    if len(current_chunk) + len(line) > 9000:
        current_chunk += "</style>\n"
        css_chunks.append(current_chunk)
        current_chunk = "<style>\n" + line + "\n"
    else:
        current_chunk += line + "\n"
if current_chunk != "<style>\n":
    current_chunk += "</style>\n"
    css_chunks.append(current_chunk)

# 2. Chunk HTML Body
body_match = re.search(r'</style>\n*(.*?)\n*<script>', content, re.DOTALL)
body_html = body_match.group(1)

# We will split by major section boundaries to ensure valid HTML.
# The boundaries are top-level tags: <nav>, <section>, <footer>.
# Let's find all these top-level tags.
# We can use a simple regex that matches <nav..., <section..., <footer... and their corresponding closing tags.
# Since we don't have nested <section> tags, this is safe.

html_chunks = []
current_chunk = ""

# Split by the comments that precede the sections
parts = re.split(r'(<!--.*?-->)', body_html)
# Group comments with the following text
blocks = []
current_block = ""
for part in parts:
    if part.startswith("<!--"):
        if current_block.strip():
            blocks.append(current_block)
        current_block = part + "\n"
    else:
        current_block += part
if current_block.strip():
    blocks.append(current_block)

for block in blocks:
    if len(current_chunk) + len(block) > 9000:
        if current_chunk.strip():
            html_chunks.append(current_chunk.strip())
        current_chunk = block
    else:
        current_chunk += block
if current_chunk.strip():
    html_chunks.append(current_chunk.strip())

# 3. Chunk Script
script_match = re.search(r'<script>(.*?)</script>', content, re.DOTALL)
script_content = script_match.group(1)
script_lines = script_content.split('\n')

script_chunks = []
current_chunk = "<script>\n"
for line in script_lines:
    if len(current_chunk) + len(line) > 9000:
        current_chunk += "</script>\n"
        script_chunks.append(current_chunk)
        current_chunk = "<script>\n" + line + "\n"
    else:
        current_chunk += line + "\n"
if current_chunk != "<script>\n":
    current_chunk += "</script>\n"
    script_chunks.append(current_chunk)

# Write all to files
idx = 1

for chunk in css_chunks:
    with open(f"webflow_embeds/{idx:02d}_css.txt", "w") as f:
        f.write(chunk)
    idx += 1

for chunk in html_chunks:
    with open(f"webflow_embeds/{idx:02d}_html.txt", "w") as f:
        f.write(chunk)
    idx += 1

for chunk in script_chunks:
    with open(f"webflow_embeds/{idx:02d}_script.txt", "w") as f:
        f.write(chunk)
    idx += 1

print(f"Generated {idx-1} files in 'webflow_embeds' directory.")
