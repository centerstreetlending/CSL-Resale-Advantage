with open("webflow_embeds/01_css.txt", "r") as f:
    content = f.read()

# Remove the HTML link tags
import re
content = re.sub(r'<link.*?>\n?', '', content)

# Insert the @import tags inside the <style> tag
import_statement = """@import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;700;900&family=Cormorant+Garamond:wght@600;700&family=Bebas+Neue&family=Inter:wght@400;700&display=swap');
@import url('https://use.typekit.net/sjt3vdj.css');
"""

content = content.replace("<style>\n", f"<style>\n{import_statement}\n")

with open("webflow_embeds/01_css.txt", "w") as f:
    f.write(content)
