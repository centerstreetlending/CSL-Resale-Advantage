file_path = '/Users/gregmontoya/AntiGravity Workspaces/Paul_Project_1/CSL-Resale-Advantage/resale-advantage-v3/csl-investor-exit-advantage-v3.html'
with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Modify the .save CSS styles to keep the frosted glass visual style, but scale the sizing back down to original levels.
old_styles = """  .save { 
    background: rgba(255, 255, 255, 0.08); 
    border: 1px solid rgba(255, 255, 255, 0.18); 
    border-radius: 16px; 
    padding: 18px 22px; 
    min-width: 150px; 
    flex: 1; 
    box-shadow: 0 12px 24px rgba(0, 0, 0, 0.25);
    backdrop-filter: blur(8px);
    -webkit-backdrop-filter: blur(8px);
  }
  .save strong { 
    display: block; 
    font-size: 2.2rem; 
    font-weight: 800; 
    color: var(--accent); 
    line-height: 1.0; 
    margin-bottom: 6px; 
    letter-spacing: -0.02em;
  }
  .save span { 
    display: block; 
    font-size: 0.75rem; 
    color: rgba(255, 255, 255, 0.82); 
    text-transform: uppercase; 
    letter-spacing: 0.06em; 
    line-height: 1.3;
  }"""

new_styles = """  .save { 
    background: rgba(255, 255, 255, 0.08); 
    border: 1px solid rgba(255, 255, 255, 0.18); 
    border-radius: 12px; 
    padding: 12px 18px; 
    min-width: 140px; 
    flex: 1; 
    box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
    backdrop-filter: blur(8px);
    -webkit-backdrop-filter: blur(8px);
  }
  .save strong { 
    display: block; 
    font-size: 1.7rem; 
    font-weight: 800; 
    color: var(--accent); 
    line-height: 1.0; 
    margin-bottom: 4px; 
    letter-spacing: -0.01em;
  }
  .save span { 
    display: block; 
    font-size: 0.68rem; 
    color: rgba(255, 255, 255, 0.82); 
    text-transform: uppercase; 
    letter-spacing: 0.04em; 
    line-height: 1.3;
  }"""

html = html.replace(old_styles, new_styles)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Horizontal savings boxes resized down to original scale.")
