with open("csl-investor-exit-advantage-v3.html", "r") as f:
    content = f.read()

import re

# Split by top-level tags/sections
sections = []

# CSS
css_match = re.search(r'<style>.*?</style>', content, re.DOTALL)
if css_match:
    css = css_match.group(0)
    print("Total CSS size:", len(css))
    # We will need to chunk CSS into 10k chunks
    lines = css.split('\n')
    chunk = ""
    chunk_idx = 1
    for line in lines:
        if len(chunk) + len(line) > 9000:
            print(f"CSS Chunk {chunk_idx}: {len(chunk)}")
            chunk = "<style>\n" + line + "\n"
            chunk_idx += 1
        else:
            chunk += line + "\n"
    if chunk:
        print(f"CSS Chunk {chunk_idx}: {len(chunk)}")

# HTML body
body_match = re.search(r'</style>\n*(.*)\n*<script>', content, re.DOTALL)
if body_match:
    body = body_match.group(1)
    print("Total Body HTML size:", len(body))
    # chunk body HTML by top-level <section> or <header> or <nav>
    # Actually, we can just split by <!-- COMMENTS -->
    parts = re.split(r'(<!--.*?-->)', body)
    chunk = ""
    chunk_idx = 1
    for part in parts:
        if len(chunk) + len(part) > 9000:
            print(f"HTML Chunk {chunk_idx}: {len(chunk)}")
            chunk = part
            chunk_idx += 1
        else:
            chunk += part
    if chunk:
        print(f"HTML Chunk {chunk_idx}: {len(chunk)}")

# Script
script_match = re.search(r'<script>.*?</script>', content, re.DOTALL)
if script_match:
    script = script_match.group(0)
    print("Script size:", len(script))

