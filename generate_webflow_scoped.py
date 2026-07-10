import re
import os

with open("resale-advantage-v3/csl-investor-exit-advantage-v3.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. Extract head code (styles and links)
head_match = re.search(r'<head>(.*?)</head>', html, re.DOTALL)
head_content = head_match.group(1) if head_match else ""

# Remove meta tags and title
head_code = re.sub(r'<meta.*?>', '', head_content)
head_code = re.sub(r'<title>.*?</title>', '', head_code)

# Extract CSS from head code
style_match = re.search(r'<style>(.*?)</style>', head_code, re.DOTALL)
if style_match:
    css = style_match.group(1)
    
    # Prefix selectors to scope to .csl-landing-page
    # First, handle the global reset
    css = css.replace('*{margin:0;padding:0;box-sizing:border-box}', '.csl-landing-page * {box-sizing:border-box;}')
    
    # Replace body with the wrapper class
    css = re.sub(r'\bbody\s*\{', '.csl-landing-page {', css)
    
    # Remove header, footer, and offer-bar styles
    css = re.sub(r'header(\.scrolled)?\s*\{.*?\}', '', css, flags=re.DOTALL)
    css = re.sub(r'header \.wrap\s*\{.*?\}', '', css, flags=re.DOTALL)
    css = re.sub(r'header a\.phone.*?\{.*?\}', '', css, flags=re.DOTALL)
    css = re.sub(r'header img\s*\{.*?\}', '', css, flags=re.DOTALL)
    css = re.sub(r'\.nav-left\s*\{.*?\}', '', css, flags=re.DOTALL)
    css = re.sub(r'footer\s*\{.*?\}', '', css, flags=re.DOTALL)
    css = re.sub(r'footer \.wrap\s*\{.*?\}', '', css, flags=re.DOTALL)
    css = re.sub(r'footer \.wordmark\s*\{.*?\}', '', css, flags=re.DOTALL)
    css = re.sub(r'footer \.licenses\s*\{.*?\}', '', css, flags=re.DOTALL)
    css = re.sub(r'\.offer-bar\s*\{.*?\}', '', css, flags=re.DOTALL)
    css = re.sub(r'\.offer-bar:hover\s*\{.*?\}', '', css, flags=re.DOTALL)
    css = re.sub(r'\.offer-bar a\s*\{.*?\}', '', css, flags=re.DOTALL)
    css = re.sub(r'\.offer-bar:hover \.offer-pulse\s*\{.*?\}', '', css, flags=re.DOTALL)
    css = re.sub(r'\.offer-bar b\s*\{.*?\}', '', css, flags=re.DOTALL)
    css = re.sub(r'\.offer-pulse\s*\{.*?\}', '', css, flags=re.DOTALL)
    css = re.sub(r'@keyframes offer-glow\s*\{.*?\}\s*\}\s*\}', '', css, flags=re.DOTALL) # roughly
    
    # Scope typography and generic tags
    css = css.replace('h1,h2,h3{', '.csl-landing-page h1, .csl-landing-page h2, .csl-landing-page h3 {')
    css = css.replace('h2{', '.csl-landing-page h2 {')
    css = css.replace('section{', '.csl-landing-page section {')
    
    # Prefix some major classes just in case they clash (though Webflow usually doesn't have these exact names)
    # Actually, a simpler way to ensure no clash is to wrap all our HTML in a div, and just rely on the specific classes.
    # Webflow doesn't use classes like .hero, .trustbar natively for global nav.
    
    head_code = head_code.replace(style_match.group(1), css)

with open("resale-advantage-v3/webflow-head-code.html", "w", encoding="utf-8") as out:
    out.write("<!-- PASTE THIS INTO WEBFLOW: Page Settings → Custom Code → Head Tag -->\n" + head_code.strip())

# 2. Extract body code
body_match = re.search(r'<body>(.*?)</body>', html, re.DOTALL)
body_content = body_match.group(1).strip() if body_match else ""

# Extract the JS script blocks at the end
script_match = re.search(r'(<script>.*?</script>\s*<script>.*?</script>)$', body_content, re.DOTALL)
if script_match:
    js_code = script_match.group(1)
    body_content = body_content.replace(js_code, '').strip()
else:
    js_code = ""

# REMOVE offer-bar, header, and footer from the HTML
body_content = re.sub(r'<div class="offer-bar">.*?</div>', '', body_content, flags=re.DOTALL)
body_content = re.sub(r'<header.*?>.*?</header>', '', body_content, flags=re.DOTALL)
body_content = re.sub(r'<footer.*?>.*?</footer>', '', body_content, flags=re.DOTALL)

# Remove the JS event listener for sticky header since header is gone
js_code = re.sub(r'// --- Sticky Header Scroll Transition ---.*?\}\);', '', js_code, flags=re.DOTALL)

# Wrap the remaining content in a sandboxing div
body_content = f'<div class="csl-landing-page">\n{body_content.strip()}\n</div>'

# Split body content into blocks
import re
# We'll split on sections to keep chunks < 9000
chunks = re.split(r'(?=<section)', body_content)
chunks = [c.strip() for c in chunks if c.strip()]

blocks = []
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

print(f"Done! Created {len(blocks)} embeds. Scoped CSS and removed header/footer.")
