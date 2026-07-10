file_path = '/Users/gregmontoya/AntiGravity Workspaces/Paul_Project_1/CSL-Resale-Advantage/resale-advantage-v3/csl-investor-exit-advantage-v3.html'
with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Swap the order: Eyebrow goes first, Logo goes below it, then the H1 headline.
# Also change the eyebrow text to "Introducing" as requested.

old_top = """      <div class="hero-left-top">
        <img src="logo1.svg" alt="Center Street Lending" style="height: 36px; width: auto; display: block; margin-bottom: 8px;">
        <div class="hero-eyebrow">CSL Resale Advantage Program</div>"""

new_top = """      <div class="hero-left-top">
        <div class="hero-eyebrow">Introducing</div>
        <img src="logo1.svg" alt="Center Street Lending" style="height: 36px; width: auto; display: block; margin-bottom: 12px;">"""

html = html.replace(old_top, new_top)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Eyebrow text changed to Introducing and logo moved below it successfully!")
