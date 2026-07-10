import glob

files = glob.glob("webflow_embeds/*_css.txt")
for f in files:
    with open(f, "r") as file:
        content = file.read()
    
    # Remove all animation rules
    import re
    content = re.sub(r'animation:[^;\}]+[;\}]', '}', content) # wait, replace with } if it ended with }
    # Let's do a safer string replace
    content = re.sub(r'animation\s*:\s*fadeUp[^;\}]*[;]?', '', content)
    content = re.sub(r'animation-delay\s*:[^;\}]*[;]?', '', content)
    content = re.sub(r'@keyframes\s+fadeUp\s*\{[^}]+\}\s*\}', '', content)
    content = re.sub(r'opacity\s*:\s*0[;]?', 'opacity: 1;', content)
    
    with open(f, "w") as file:
        file.write(content)

