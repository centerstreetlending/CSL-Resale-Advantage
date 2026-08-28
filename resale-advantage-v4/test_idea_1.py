file_path = '/Users/gregmontoya/AntiGravity Workspaces/Paul_Project_1/CSL-Resale-Advantage/resale-advantage-v3/csl-investor-exit-advantage-v3.html'
with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update CSS for .hero-eyebrow to use Idea 1 (Left Border Accent Line, no background box)
old_css = """.hero-eyebrow { 
    display: inline-block; 
    align-self: flex-start; 
    background: var(--accent); 
    color: #fff; 
    font-size: 0.95rem; 
    font-weight: 700; 
    text-transform: uppercase; 
    letter-spacing: 0.12em; 
    padding: 8px 18px; 
    border-radius: 4px; 
    margin-bottom: 20px; 
  }"""

new_css = """.hero-eyebrow { 
    display: inline-block; 
    align-self: flex-start; 
    border-left: 4px solid var(--accent); 
    color: #fff; 
    font-size: 1rem; 
    font-weight: 700; 
    text-transform: uppercase; 
    letter-spacing: 0.12em; 
    padding: 2px 0 2px 16px; 
    margin-bottom: 20px; 
    background: none;
  }"""

html = html.replace(old_css, new_css)

# 2. Remove the "Introducing the" text in HTML to make it super clean
html = html.replace(
    '<span class="hero-intro-text">Introducing the</span>\n        <div class="hero-eyebrow">CSL Resale Advantage Program</div>',
    '<div class="hero-eyebrow">CSL Resale Advantage Program</div>'
)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Idea 1 applied successfully.")
