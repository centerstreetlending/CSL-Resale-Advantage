file_path = '/Users/gregmontoya/AntiGravity Workspaces/Paul_Project_1/CSL-Resale-Advantage/resale-advantage-v3/csl-investor-exit-advantage-v3.html'
with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Enhance the .offer-bar CSS to ensure it has a proper z-index and box-shadow,
# preventing it from getting layered behind the hero or blending in with the dark hero image.
old_css = """  .offer-bar { 
    background: var(--navy-deep); 
    color: #fff; 
    text-align: center; 
    padding: 11px 16px; 
    font-size: 0.92rem; 
    letter-spacing: 0.05em; 
    font-family: 'Roboto', sans-serif; 
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 8px;
    border-bottom: 1px solid rgba(255, 255, 255, 0.05);
  }"""

new_css = """  .offer-bar { 
    background: var(--navy-deep); 
    color: #fff; 
    text-align: center; 
    padding: 12px 16px; 
    font-size: 0.92rem; 
    letter-spacing: 0.05em; 
    font-family: 'Roboto', sans-serif; 
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 8px;
    border-bottom: 1px solid rgba(255, 255, 255, 0.08);
    position: relative;
    z-index: 999;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
  }"""

html = html.replace(old_css, new_css)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Offer bar CSS visibility and layering enhanced!")
