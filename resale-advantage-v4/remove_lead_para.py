file_path = '/Users/gregmontoya/AntiGravity Workspaces/Paul_Project_1/CSL-Resale-Advantage/resale-advantage-v3/csl-investor-exit-advantage-v3.html'
with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Remove the lead paragraph line (<p class="hero-lead-para">...</p>) to tighten the visual flow
old_para = """        <p class="hero-lead-para">We pre-negotiated an exclusive exit program with Innovate Realty and Honest Escrow to help CSL borrowers maximize their profit on the sale side of their projects:</p>"""

html = html.replace(old_para + "\n", "")
html = html.replace(old_para, "")

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Second line (lead paragraph) removed from hero section!")
