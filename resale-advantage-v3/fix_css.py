with open("webflow_embeds/01_css.txt", "r") as f:
    css_content = f.read()

links = """<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;700;900&family=Cormorant+Garamond:wght@600;700&family=Bebas+Neue&family=Inter:wght@400;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://use.typekit.net/sjt3vdj.css">
"""

with open("webflow_embeds/01_css.txt", "w") as f:
    f.write(links + css_content)
