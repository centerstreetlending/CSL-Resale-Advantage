import re

with open("resale-advantage-v3/csl-investor-exit-advantage-v3.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. Extract head code (styles and links) UNSCOPED
head_match = re.search(r'<head>(.*?)</head>', html, re.DOTALL)
head_content = head_match.group(1) if head_match else ""

# Remove meta tags and title, keep only links and styles
head_code = re.sub(r'<meta.*?>', '', head_content)
head_code = re.sub(r'<title>.*?</title>', '', head_code)

with open("resale-advantage-v3/webflow-head-code.html", "w", encoding="utf-8") as out:
    out.write("<!-- PASTE THIS INTO WEBFLOW: Page Settings → Custom Code → Head Tag -->\n" + head_code.strip())

# 2. Extract FULL body code (INCLUDING header and footer)
body_match = re.search(r'<body>(.*?)</body>', html, re.DOTALL)
body_content = body_match.group(1).strip() if body_match else ""

# Extract the JS script blocks at the end
script_match = re.search(r'(<script>.*?</script>\s*<script>.*?</script>)$', body_content, re.DOTALL)
if script_match:
    js_code = script_match.group(1)
    body_content = body_content.replace(js_code, '').strip()
else:
    js_code = ""

# Split body content into EXACTLY 13 blocks
def split_into_13(text):
    n = 13
    chunk_size = len(text) // n
    chunks = []
    start = 0
    for i in range(n - 1):
        target = start + chunk_size
        # Find next newline or safe tag boundary
        match = re.search(r'\n|<', text[target:])
        if match:
            split_point = target + match.start()
        else:
            split_point = target
        chunks.append(text[start:split_point].strip())
        start = split_point
    chunks.append(text[start:].strip())
    return chunks

blocks = split_into_13(body_content)
    
with open("resale-advantage-v3/webflow-body-blocks.html", "w", encoding="utf-8") as out:
    out.write("<!-- ============================================================\n")
    out.write(f"     WEBFLOW BODY BLOCKS ({len(blocks)} Embeds)\n")
    out.write("     Each block = one Embed element in Webflow.\n")
    out.write("     Also paste the JS block below into:\n")
    out.write("     Page Settings → Custom Code → Before </body> tag\n")
    out.write("============================================================ -->\n\n")
    
    for i, block in enumerate(blocks):
        out.write(f"<!-- ═══════════════════════════════════════════════\n")
        out.write(f"     BLOCK {i+1} ({len(block)} chars)\n")
        out.write(f"     → Add ONE Embed element in Webflow, paste below\n")
        out.write(f"═══════════════════════════════════════════════ -->\n\n")
        out.write(block + "\n\n")
        
    out.write(f"<!-- ═══════════════════════════════════════════════\n")
    out.write(f"     JS — PASTE INTO: Page Settings → Custom Code → Before </body>\n")
    out.write(f"═══════════════════════════════════════════════ -->\n\n")
    out.write(js_code + "\n")

print(f"Done! Created {len(blocks)} embeds with FULL unscoped HTML including header and footer.")
