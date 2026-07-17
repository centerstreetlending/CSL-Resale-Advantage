import os

artifact_path = "/Users/gregmontoya/.gemini/antigravity/brain/295d0129-bb41-44c9-867b-90ef4c424554/webflow_code_to_copy.md"
embeds_dir = "webflow_embeds"

files = sorted(os.listdir(embeds_dir))

html_files = [f for f in files if f.endswith("_html.txt")]
num_embeds = len(html_files)

md_content = f"# Your {num_embeds} Webflow Embeds\n\nHere is the exact code you need to copy into Webflow. The blocks are perfectly split so no HTML tags are broken!\n\n"

# Add Head CSS
md_content += "## 1. Head Code\nGo to your Webflow **Page Settings** (the gear icon next to your page name), scroll down to **Custom Code**, and paste this into the **Head tag** section:\n\n```html\n"
md_content += "<!-- PASTE THIS INTO WEBFLOW: Page Settings → Custom Code → Head Tag -->\n"
md_content += "<link rel=\"preconnect\" href=\"https://fonts.googleapis.com\">\n"
md_content += "<link rel=\"preconnect\" href=\"https://fonts.gstatic.com\" crossorigin>\n"
md_content += "<link href=\"https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;700;900&family=Cormorant+Garamond:wght@600;700&family=Bebas+Neue&family=Inter:wght@400;700&display=swap\" rel=\"stylesheet\">\n"
md_content += "<link rel=\"stylesheet\" href=\"https://use.typekit.net/sjt3vdj.css\">\n"
md_content += "<style>\n"

for f in files:
    if f.endswith("_css.txt"):
        with open(os.path.join(embeds_dir, f), "r") as fh:
            content = fh.read().replace("<style>", "").replace("</style>", "").strip()
            # remove duplicate imports
            content = content.replace("@import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;700;900&family=Cormorant+Garamond:wght@600;700&family=Bebas+Neue&family=Inter:wght@400;700&display=swap');", "")
            content = content.replace("@import url('https://use.typekit.net/sjt3vdj.css');", "")
            md_content += content + "\n"
md_content += "</style>\n```\n\n"

# Add Body HTML Blocks
md_content += f"## 2. The {num_embeds} Body Embeds\n"
md_content += f"Below are the {num_embeds} blocks of code. Go down your list of Code Embeds on the Webflow canvas and paste one block into each embed, sequentially.\n\n"
md_content += "```html\n"
md_content += f"<!-- ============================================================\n"
md_content += f"     WEBFLOW BODY BLOCKS (Exactly {num_embeds} Embeds)\n"
md_content += f"============================================================ -->\n\n"

import re

block_num = 1
for f in html_files:
    with open(os.path.join(embeds_dir, f), "r") as fh:
        content = fh.read().strip()
        
        # Convert all relative src to absolute github pages URLs
        content = re.sub(
            r'src="([^"]+?\.(?:svg|png|jpg|jpeg))"',
            r'src="https://centerstreetlending.github.io/CSL-Resale-Advantage/resale-advantage-v4/\1"',
            content
        )
        
        md_content += f"<!-- ═══════════════════════════════════════════════\n"
        md_content += f"     BLOCK {block_num} ({len(content)} chars)\n"
        md_content += f"     → Add ONE Embed element in Webflow, paste below\n"
        md_content += f"═══════════════════════════════════════════════ -->\n\n"
        md_content += content + "\n\n"
        block_num += 1
md_content += "```\n\n"

# Add JS Blocks
js_blocks = [f for f in files if f.endswith("_script.txt")]
if js_blocks:
    md_content += "## 3. Before </body> Code\n"
    md_content += "Go back to your Webflow **Page Settings**, scroll to the bottom of the **Custom Code** section, and paste this into the **Before </body> tag** section:\n\n```html\n"
    for f in js_blocks:
        with open(os.path.join(embeds_dir, f), "r") as fh:
            md_content += fh.read() + "\n"
    md_content += "```\n"

with open(artifact_path, "w") as f:
    f.write(md_content)
    
print("Artifact updated successfully!")
