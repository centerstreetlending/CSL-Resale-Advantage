import os

artifact_path = "/Users/gregmontoya/.gemini/antigravity/brain/295d0129-bb41-44c9-867b-90ef4c424554/webflow_code_to_copy.md"
embeds_dir = "webflow_embeds"

files = sorted(os.listdir(embeds_dir))

md_content = "# Webflow Copy/Paste Guide\n\nHere is the exact code you need to copy into Webflow. I have provided the Head code, the HTML body blocks, and the final Javascript snippet.\n\n"

md_content += "## Head Code\nGo to your Webflow **Page Settings** (the gear icon next to your page name), scroll down to **Custom Code**, and paste this into the **Head tag** section:\n\n```html\n"
for f in files:
    if f.endswith("_css.txt"):
        with open(os.path.join(embeds_dir, f), "r") as fh:
            md_content += fh.read() + "\n"
md_content += "```\n\n"

block_num = 1
for f in files:
    if f.endswith("_html.txt"):
        with open(os.path.join(embeds_dir, f), "r") as fh:
            md_content += f"## HTML Embed Block {block_num}\n"
            md_content += "Create a new **Embed** element in the Webflow designer and paste this code:\n\n```html\n"
            md_content += fh.read() + "\n```\n\n"
            block_num += 1

js_blocks = [f for f in files if f.endswith("_script.txt")]
if js_blocks:
    md_content += "## Before </body> Code\n"
    md_content += "Go back to your Webflow **Page Settings**, scroll to the bottom of the **Custom Code** section, and paste this into the **Before </body> tag** section:\n\n```html\n"
    for f in js_blocks:
        with open(os.path.join(embeds_dir, f), "r") as fh:
            md_content += fh.read() + "\n"
    md_content += "```\n"

with open(artifact_path, "w") as f:
    f.write(md_content)
    
print("Artifact updated successfully!")
