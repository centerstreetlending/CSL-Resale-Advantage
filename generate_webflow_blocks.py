import re

with open("resale-advantage-v3/csl-investor-exit-advantage-v3.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. Extract head code (styles and links)
head_match = re.search(r'<head>(.*?)</head>', html, re.DOTALL)
if head_match:
    head_content = head_match.group(1)
    # Remove meta tags and title, keep only links and styles
    head_code = re.sub(r'<meta.*?>', '', head_content)
    head_code = re.sub(r'<title>.*?</title>', '', head_code)
    # Write to webflow-head-code.html
    with open("resale-advantage-v3/webflow-head-code.html", "w", encoding="utf-8") as out:
        out.write("<!-- PASTE THIS INTO WEBFLOW: Page Settings → Custom Code → Head Tag -->\n" + head_code.strip())

# 2. Extract body code
body_match = re.search(r'<body>(.*?)</body>', html, re.DOTALL)
if body_match:
    body_content = body_match.group(1).strip()
    
    # Extract the JS script block at the end
    script_match = re.search(r'(<script>.*?</script>\s*<script>.*?</script>)$', body_content, re.DOTALL)
    if script_match:
        js_code = script_match.group(1)
        body_content = body_content.replace(js_code, '').strip()
    else:
        # Fallback to single script block
        script_match = re.search(r'(<script>.*?</script>)$', body_content, re.DOTALL)
        if script_match:
            js_code = script_match.group(1)
            body_content = body_content.replace(js_code, '').strip()
        else:
            js_code = ""

    # Split body content into blocks based on major tags (<section>, <header>, <div class="hero">)
    blocks = []
    
    # We will use beautifulsoup to accurately find top level elements
    # But since we might not have beautifulsoup, we can just split by <section>, <header>, <footer>
    import xml.etree.ElementTree as ET
    
    # Let's just do a simple greedy split
    chunks = re.split(r'(?=<header>|<section|<footer|<div class="offer-bar"|<div class="hero"|<div class="color-bar")', body_content)
    
    # Filter empty chunks
    chunks = [c.strip() for c in chunks if c.strip()]
    
    # Combine chunks so they are < 9000 chars
    current_block = ""
    for chunk in chunks:
        if len(current_block) + len(chunk) < 8500:
            current_block += "\n" + chunk
        else:
            blocks.append(current_block.strip())
            current_block = chunk
    if current_block:
        blocks.append(current_block.strip())
        
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

print(f"Done! Created {len(blocks)} embeds.")
