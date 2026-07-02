file_path = '/Users/gregmontoya/AntiGravity Workspaces/Paul_Project_1/CSL-Resale-Advantage/resale-advantage-v3/csl-investor-exit-advantage-v3.html'
with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update .program-title CSS:
# - Increase font-size to 1.3rem (a little bit bigger)
# - Add color override for nested spans to color "Program" in brand blue (var(--accent))
old_title_css = """  .program-title { 
    display: none; 
    font-size: 1.15rem; 
    font-weight: 700; 
    color: var(--navy); 
    letter-spacing: -0.01em; 
    opacity: 0;
    transform: translateY(-5px);
    transition: opacity 0.3s ease, transform 0.3s ease;
  }"""

new_title_css = """  .program-title { 
    display: none; 
    font-size: 1.3rem; 
    font-weight: 700; 
    color: var(--navy); 
    letter-spacing: -0.019em; 
    opacity: 0;
    transform: translateY(-5px);
    transition: opacity 0.3s ease, transform 0.3s ease;
  }
  .program-title span {
    color: var(--accent);
  }"""

html = html.replace(old_title_css, new_title_css)

# 2. Update the HTML to wrap the word "Program" in a span
old_title_html = '<span class="program-title">CSL Resale Advantage Program</span>'
new_title_html = '<span class="program-title">CSL Resale Advantage <span>Program</span></span>'

html = html.replace(old_title_html, new_title_html)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Sticky title styled bigger with 'Program' in blue!")
