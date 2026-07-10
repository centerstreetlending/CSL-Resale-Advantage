file_path = '/Users/gregmontoya/AntiGravity Workspaces/Paul_Project_1/CSL-Resale-Advantage/resale-advantage-v3/csl-investor-exit-advantage-v3.html'
with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update .save CSS to increase min-width and max-width slightly to accommodate the text on a single line
# 2. Add white-space: nowrap; to .save span to prevent wrapping

old_save = """  .save { 
    background: rgba(255, 255, 255, 0.08); 
    border: 1px solid rgba(255, 255, 255, 0.18); 
    border-radius: 12px; 
    padding: 14px 20px; 
    min-width: 130px; 
    max-width: 185px; 
    flex: 1; 
    box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
    backdrop-filter: blur(8px);
    -webkit-backdrop-filter: blur(8px);
  }"""

new_save = """  .save { 
    background: rgba(255, 255, 255, 0.08); 
    border: 1px solid rgba(255, 255, 255, 0.18); 
    border-radius: 12px; 
    padding: 14px 20px; 
    min-width: 155px; 
    max-width: 195px; 
    flex: 1; 
    box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
    backdrop-filter: blur(8px);
    -webkit-backdrop-filter: blur(8px);
  }"""

html = html.replace(old_save, new_save)

old_span = """  .save span { 
    display: block; 
    font-size: 0.68rem; 
    color: rgba(255, 255, 255, 0.82); 
    text-transform: uppercase; 
    letter-spacing: 0.04em; 
    line-height: 1.3;
  }"""

new_span = """  .save span { 
    display: block; 
    font-size: 0.68rem; 
    color: rgba(255, 255, 255, 0.82); 
    text-transform: uppercase; 
    letter-spacing: 0.04em; 
    line-height: 1.3;
    white-space: nowrap;
  }"""

html = html.replace(old_span, new_span)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Savings text wrapping fixed.")
