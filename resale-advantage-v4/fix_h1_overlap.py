file_path = '/Users/gregmontoya/AntiGravity Workspaces/Paul_Project_1/CSL-Resale-Advantage/resale-advantage-v3/csl-investor-exit-advantage-v3.html'
with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Swap Oswald for Bebas Neue in Google Fonts to get a tall, highly condensed font fallback
html = html.replace(
    'family=Oswald:wght@700&family=Inter:wght@400;700&display=swap',
    'family=Bebas+Neue&family=Inter:wght@400;700&display=swap'
)

# 2. Update H1 style to use Bebas Neue and adjust size to 76px (which fits perfectly on a single line in Bebas Neue fallback)
html = html.replace(
    '.hero h1 { font-family: \'Arteria Std Compress\', \'Oswald\', sans-serif; font-size: 92px; font-weight: 700; text-transform: uppercase; line-height: 86px; color: #fff; margin: 0; letter-spacing: -0.01em; }',
    '.hero h1 { font-family: \'Arteria Std Compress\', \'Bebas Neue\', sans-serif; font-size: 76px; font-weight: 400; text-transform: uppercase; line-height: 76px; color: #fff; margin: 0; letter-spacing: 0.03em; }'
)

# 3. Add flex-shrink: 0 to hero-right to protect the right-side card from squeezing
html = html.replace(
    '.hero-right { width: 340px; padding: 26px 22px; background: rgba(255, 255, 255, 0.06); border: 1px solid rgba(255,255,255,.16); border-radius: 18px; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 24px; }',
    '.hero-right { width: 340px; flex-shrink: 0; padding: 26px 22px; background: rgba(255, 255, 255, 0.06); border: 1px solid rgba(255,255,255,.16); border-radius: 18px; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 24px; }'
)

# 4. Make sure responsiveness works nicely for Bebas Neue
html = html.replace(
    '.hero h1 { font-family: \'Arteria Std Compress\', \'Oswald\', sans-serif; font-size: 64px; line-height: 64px; }',
    '.hero h1 { font-family: \'Arteria Std Compress\', \'Bebas Neue\', sans-serif; font-size: 52px; line-height: 52px; }'
)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Overlap fixed using Bebas Neue fallback and sizing updates.")
