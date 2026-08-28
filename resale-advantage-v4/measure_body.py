import re

with open("csl-investor-exit-advantage-v4.html", "r") as f:
    html = f.read()

# Remove style tags
html_no_style = re.sub(r'<style>.*?</style>', '', html, flags=re.DOTALL)
# Remove script tags
html_no_script = re.sub(r'<script.*?</script>', '', html_no_style, flags=re.DOTALL)

# Extract body
body_match = re.search(r'<body>(.*?)</body>', html_no_script, flags=re.DOTALL)
if body_match:
    body = body_match.group(1).strip()
    print(f"Body size (no CSS/JS): {len(body)} characters")
else:
    print("Could not find body tag")
