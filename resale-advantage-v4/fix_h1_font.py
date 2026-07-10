file_path = '/Users/gregmontoya/AntiGravity Workspaces/Paul_Project_1/CSL-Resale-Advantage/resale-advantage-v3/csl-investor-exit-advantage-v3.html'
with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Restore Google Font import with Oswald and Inter
html = html.replace(
    '<link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;500;700&family=Cormorant+Garamond:wght@600;700&family=display=swap" rel="stylesheet">',
    '<link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;500;700&family=Cormorant+Garamond:wght@600;700&family=Oswald:wght@700&family=Inter:wght@400;700&display=swap" rel="stylesheet">'
)

# 2. Re-add Arteria Std Compress local font face
arteria_font_face = """<style>
  @font-face {
    font-family: 'Arteria Std Compress';
    src: local('Arteria Std Compress');
    font-display: swap;
  }"""
html = html.replace("<style>", arteria_font_face)

# 3. Update H1 font sizing and family to match the giant condensed look
html = html.replace(
    '.hero h1 { font-family: \'Roboto\', sans-serif; font-size: 3.1rem; font-weight: 700; line-height: 1.1; color: #fff; margin: 0; letter-spacing: -.01em; max-width: 680px; }',
    '.hero h1 { font-family: \'Arteria Std Compress\', \'Oswald\', sans-serif; font-size: 101px; font-weight: 700; text-transform: uppercase; line-height: 90.9px; color: #fff; margin: 0; letter-spacing: normal; }'
)

# Make sure media queries don't override it to something too small, or keep them balanced:
# html = html.replace(".hero h1 { font-size: 48px; line-height: 52px; }", ".hero h1 { font-size: 64px; line-height: 64px; }")
# Currently in stylesheet:
# @media(max-width:1100px){ ... .hero h1 { font-size: 48px; line-height: 52px; } ... }
# Let's keep a condensed responsive override:
html = html.replace(
    '.hero h1 { font-size: 48px; line-height: 52px; }',
    '.hero h1 { font-family: \'Arteria Std Compress\', \'Oswald\', sans-serif; font-size: 64px; line-height: 64px; }'
)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("H1 font restored to Arteria Std Compress / Oswald at 101px.")
