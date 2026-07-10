import re
import urllib.parse

with open("resale-advantage-v3/csl-investor-exit-advantage-v3.html", "r", encoding="utf-8") as f:
    html = f.read()

base_url = "https://centerstreetlending.github.io/CSL-Resale-Advantage/resale-advantage-v3/"

# 1. Replace all local image src with absolute URLs
def replace_img_src(match):
    src = match.group(1)
    if not src.startswith("http") and not src.startswith("//"):
        # URL encode spaces and special characters for the CDN URL
        safe_src = urllib.parse.quote(src)
        return f'src="{base_url}{safe_src}"'
    return match.group(0)

html = re.sub(r'src="([^"]+)"', replace_img_src, html)

# 2. Extract Head Code
head_match = re.search(r'<head>(.*?)</head>', html, re.DOTALL)
head_code = head_match.group(1) if head_match else ""
head_code = re.sub(r'<meta.*?>', '', head_code)
head_code = re.sub(r'<title>.*?</title>', '', head_code)

with open("resale-advantage-v3/webflow-head-code.html", "w", encoding="utf-8") as out:
    out.write("<!-- PASTE THIS INTO WEBFLOW: Page Settings → Custom Code → Head Tag -->\n" + head_code.strip())

# 3. Extract Body Code
body_match = re.search(r'<body>(.*?)</body>', html, re.DOTALL)
body_content = body_match.group(1).strip() if body_match else ""

# Extract JS at the bottom
script_match = re.search(r'(<script>.*?</script>\s*<script>.*?</script>)$', body_content, re.DOTALL)
if script_match:
    js_code = script_match.group(1)
    body_content = body_content.replace(js_code, '').strip()
else:
    js_code = ""

# 4. Safely chunk the body content based on top-level elements to ensure tags aren't broken
# Split by tags that we know are at the root level of the body
split_regex = r'(?=<header|<div class="offer-bar"|<div class="hero"|<div class="color-bar"|<section|<footer)'
chunks = re.split(split_regex, body_content)
chunks = [c.strip() for c in chunks if c.strip()]

# Now we have perfectly encapsulated HTML chunks (none are cut in half).
# We want exactly 13 chunks (the user has 13 embeds).
# If we have more than 13 chunks, we merge the smallest adjacent chunks until we have exactly 13.
while len(chunks) > 13:
    # Find the adjacent pair with the smallest combined length
    min_len = float('inf')
    merge_index = 0
    for i in range(len(chunks) - 1):
        combined_len = len(chunks[i]) + len(chunks[i+1])
        if combined_len < min_len:
            min_len = combined_len
            merge_index = i
            
    # Merge them
    merged = chunks[merge_index] + "\n\n" + chunks[merge_index+1]
    chunks = chunks[:merge_index] + [merged] + chunks[merge_index+2:]

# If we have less than 13 chunks (unlikely), append empty chunks
while len(chunks) < 13:
    chunks.append("<!-- Empty Embed -->")

with open("resale-advantage-v3/webflow-body-blocks.html", "w", encoding="utf-8") as out:
    out.write("<!-- ============================================================\n")
    out.write(f"     WEBFLOW BODY BLOCKS (Exactly 13 Embeds)\n")
    out.write("     All image URLs have been converted to absolute CDN URLs!\n")
    out.write("     Each block contains perfectly complete HTML tags.\n")
    out.write("============================================================ -->\n\n")
    
    for i, block in enumerate(chunks):
        out.write(f"<!-- ═══════════════════════════════════════════════\n")
        out.write(f"     BLOCK {i+1} ({len(block)} chars)\n")
        out.write(f"     → Add ONE Embed element in Webflow, paste below\n")
        out.write(f"═══════════════════════════════════════════════ -->\n\n")
        out.write(block + "\n\n")
        
    out.write(f"<!-- ═══════════════════════════════════════════════\n")
    out.write(f"     JS — PASTE INTO: Page Settings → Custom Code → Before </body>\n")
    out.write(f"═══════════════════════════════════════════════ -->\n\n")
    out.write(js_code + "\n")

print(f"Done! Created exactly {len(chunks)} safe HTML embeds with absolute Image URLs.")
