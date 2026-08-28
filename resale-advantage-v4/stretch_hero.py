file_path = '/Users/gregmontoya/AntiGravity Workspaces/Paul_Project_1/CSL-Resale-Advantage/resale-advantage-v3/csl-investor-exit-advantage-v3.html'
with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Stretch the hero row max-width to 1200px to give it more breathing room
html = html.replace(
    '.hero-main-row { display: flex; align-items: flex-start; justify-content: space-between; width: 100%; max-width: 1080px; gap: 44px; margin: 0 auto; }',
    '.hero-main-row { display: flex; align-items: flex-start; justify-content: space-between; width: 100%; max-width: 1200px; gap: 44px; margin: 0 auto; }'
)

# 2. Stretch the hero-left max-width to 800px
html = html.replace(
    '.hero-left { flex: 1; max-width: 680px; display: flex; flex-direction: column; gap: 28px; }',
    '.hero-left { flex: 1; max-width: 800px; display: flex; flex-direction: column; gap: 28px; }'
)

# 3. Slightly adjust the H1 styling to prevent line wrapping (adding font-size: 92px to ensure Oswald fits if local Arteria is missing, and keep it massive)
html = html.replace(
    '.hero h1 { font-family: \'Arteria Std Compress\', \'Oswald\', sans-serif; font-size: 101px; font-weight: 700; text-transform: uppercase; line-height: 90.9px; color: #fff; margin: 0; letter-spacing: normal; }',
    '.hero h1 { font-family: \'Arteria Std Compress\', \'Oswald\', sans-serif; font-size: 92px; font-weight: 700; text-transform: uppercase; line-height: 86px; color: #fff; margin: 0; letter-spacing: -0.01em; }'
)

# 4. Wrap the H1 content in spans to prevent wrapping of the individual lines
html = html.replace(
    '<h1>WE MADE IT <span class="hl">EASIER & CHEAPER</span><br>TO EXIT YOUR INVESTMENT.</h1>',
    '<h1><span style="display: inline-block; white-space: nowrap;">WE MADE IT <span class="hl">EASIER & CHEAPER</span></span><br><span style="display: inline-block; white-space: nowrap;">TO EXIT YOUR INVESTMENT.</span></h1>'
)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Hero stretched and H1 wrapping fixed.")
