file_path = '/Users/gregmontoya/AntiGravity Workspaces/Paul_Project_1/CSL-Resale-Advantage/resale-advantage-v3/csl-investor-exit-advantage-v3.html'
with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Remove the ghost call button in the hero CTA
html = html.replace(
    '<a class="btn-ghost" href="tel:9492441090">or call 949-244-1090</a>',
    ''
)

# 2. Update .hero-optional CSS to make it stand out more (higher color opacity, slightly larger, medium font weight)
old_optional = '.hero-optional { color: rgba(255,255,255,.5); font-size: .85rem; line-height: 1.4; text-align: center; max-width: none; width: 100%; margin-top: 40px; }'
new_optional = '.hero-optional { color: rgba(255, 255, 255, 0.85); font-size: 0.95rem; line-height: 1.5; text-align: center; max-width: none; width: 100%; margin-top: 40px; font-weight: 500; }'

html = html.replace(old_optional, new_optional)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("CTA adjusted and disclosure updated to stand out.")
