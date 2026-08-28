file_path = '/Users/gregmontoya/AntiGravity Workspaces/Paul_Project_1/CSL-Resale-Advantage/resale-advantage-v3/csl-investor-exit-advantage-v3.html'
with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Revert the eyebrow text color from brand blue (var(--accent)) back to white (#fff) as per the mockup design
html = html.replace(
    '  .hero-eyebrow { \n    display: inline-block; \n    align-self: flex-start; \n    border-left: 4px solid var(--accent); \n    color: var(--accent); ',
    '  .hero-eyebrow { \n    display: inline-block; \n    align-self: flex-start; \n    border-left: 4px solid var(--accent); \n    color: #fff; '
)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Eyebrow text color reverted to white successfully!")
