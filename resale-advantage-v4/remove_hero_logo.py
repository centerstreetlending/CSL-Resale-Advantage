file_path = '/Users/gregmontoya/AntiGravity Workspaces/Paul_Project_1/CSL-Resale-Advantage/resale-advantage-v3/csl-investor-exit-advantage-v3.html'
with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Remove the corporate logo image from the hero-left-top section
old_hero_top = """    <div class="hero-left">
      <div class="hero-left-top">
        <img src="logo1.svg" alt="Center Street Lending" style="height: 36px; width: auto; display: block; margin-bottom: 16px;">
        <div class="hero-eyebrow">CSL RESALE ADVANTAGE PROGRAM</div>"""

new_hero_top = """    <div class="hero-left">
      <div class="hero-left-top">
        <div class="hero-eyebrow">CSL RESALE ADVANTAGE PROGRAM</div>"""

html = html.replace(old_hero_top, new_hero_top)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Corporate logo removed from the hero space!")
