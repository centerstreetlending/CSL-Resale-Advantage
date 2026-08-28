file_path = '/Users/gregmontoya/AntiGravity Workspaces/Paul_Project_1/CSL-Resale-Advantage/resale-advantage-v3/csl-investor-exit-advantage-v3.html'
with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

# We will add margin-top: -50px to .hero-right to visually shift the ticker card slightly higher than absolute vertical center.
# We also want to reset it on mobile/tablet media queries so it doesn't get messed up when stacked vertically.

# 1. Update .hero-right styles
html = html.replace(
    '.hero-right { width: 340px; flex-shrink: 0; padding: 26px 22px; background: rgba(255, 255, 255, 0.06); border: 1px solid rgba(255,255,255,.16); border-radius: 18px; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 24px; }',
    '.hero-right { width: 340px; flex-shrink: 0; padding: 26px 22px; background: rgba(255, 255, 255, 0.06); border: 1px solid rgba(255,255,255,.16); border-radius: 18px; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 24px; margin-top: -60px; }'
)

# 2. Reset margin-top to 0 in media query for max-width: 1100px so it aligns correctly when stacked
html = html.replace(
    '.hero-right { width: 100%; max-width: 572px; padding: 40px 24px; }',
    '.hero-right { width: 100%; max-width: 572px; padding: 40px 24px; margin-top: 0; }'
)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Ticker card shifted higher!")
