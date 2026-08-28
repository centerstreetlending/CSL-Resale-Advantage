import os
import re

desktop_folder = os.path.expanduser("~/Desktop/Webflow_Embeds_Separate")
os.makedirs(desktop_folder, exist_ok=True)

# 1. Write Head Code
with open("resale-advantage-v3/webflow-head-code.html", "r", encoding="utf-8") as f:
    head_code = f.read()

# Remove the PASTE THIS INTO WEBFLOW comment to make it cleaner
head_code = re.sub(r'<!-- PASTE THIS.*?-->\n?', '', head_code).strip()

with open(os.path.join(desktop_folder, "00_Head_Code.txt"), "w", encoding="utf-8") as f:
    f.write(head_code)

# 2. Extract and write Body Blocks
with open("resale-advantage-v3/webflow-body-blocks.html", "r", encoding="utf-8") as f:
    body_content = f.read()

# The blocks are separated by the big comment lines
# We can find all blocks using a regex that looks for the block comment and captures the content until the next block comment or JS comment
pattern = r'<!-- ═══════════════════════════════════════════════\n     BLOCK (\d+).*?\n═══════════════════════════════════════════════ -->\n(.*?)(?=(?:<!-- ═══════════════════════════════════════════════\n     BLOCK|<!-- ═══════════════════════════════════════════════\n     JS))'

blocks = re.findall(pattern, body_content, re.DOTALL)

for i, (block_num, content) in enumerate(blocks):
    filename = f"Embed_{int(block_num):02d}.txt"
    with open(os.path.join(desktop_folder, filename), "w", encoding="utf-8") as f:
        f.write(content.strip())

# 3. Extract JS
js_pattern = r'<!-- ═══════════════════════════════════════════════\n     JS — PASTE INTO: Page Settings → Custom Code → Before </body>\n═══════════════════════════════════════════════ -->\n(.*)'
js_match = re.search(js_pattern, body_content, re.DOTALL)
if js_match:
    with open(os.path.join(desktop_folder, "14_Javascript_Before_Body_End.txt"), "w", encoding="utf-8") as f:
        f.write(js_match.group(1).strip())

print(f"Created {len(blocks)} embed text files + head and js files!")
