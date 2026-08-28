file_path = '/Users/gregmontoya/AntiGravity Workspaces/Paul_Project_1/CSL-Resale-Advantage/resale-advantage-v3/csl-investor-exit-advantage-v3.html'
with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Remove flex: 1; from .save to prevent them from stretching to fill the wide container
old_styles = """  .save { 
    background: rgba(255, 255, 255, 0.08); 
    border: 1px solid rgba(255, 255, 255, 0.18); 
    border-radius: 12px; 
    padding: 12px 18px; 
    min-width: 140px; 
    flex: 1; 
    box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
    backdrop-filter: blur(8px);
    -webkit-backdrop-filter: blur(8px);
  }"""

new_styles = """  .save { 
    background: rgba(255, 255, 255, 0.08); 
    border: 1px solid rgba(255, 255, 255, 0.18); 
    border-radius: 12px; 
    padding: 12px 18px; 
    min-width: 140px; 
    box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
    backdrop-filter: blur(8px);
    -webkit-backdrop-filter: blur(8px);
  }"""

html = html.replace(old_styles, new_styles)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Savings boxes stretching disabled.")
