file_path = '/Users/gregmontoya/AntiGravity Workspaces/Paul_Project_1/CSL-Resale-Advantage/resale-advantage-v3/csl-investor-exit-advantage-v3.html'
with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update the top bar CSS:
# - Increase font-size to .92rem (~15px)
# - Add vertical padding slightly (11px)
# - Add styling for a subtle pulsing brand-blue alert dot next to the text
# - Add Keyframes animation for the pulse

old_css = """  .offer-bar { background: var(--navy-deep); color: #fff; text-align: center; padding: 9px 16px; font-size: .8rem; letter-spacing: .05em; font-family: 'Roboto', sans-serif; }
  .offer-bar b { color: var(--accent); font-weight: 700; text-transform: uppercase; }"""

new_css = """  .offer-bar { 
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
  }
  .offer-bar b { color: var(--accent); font-weight: 700; text-transform: uppercase; }
  .offer-pulse {
    display: inline-block;
    width: 8px;
    height: 8px;
    background-color: var(--accent);
    border-radius: 50%;
    box-shadow: 0 0 0 0 rgba(70, 131, 179, 0.7);
    animation: offer-glow 2s infinite;
  }
  @keyframes offer-glow {
    0% {
      transform: scale(0.95);
      box-shadow: 0 0 0 0 rgba(70, 131, 179, 0.7);
    }
    70% {
      transform: scale(1);
      box-shadow: 0 0 0 6px rgba(70, 131, 179, 0);
    }
    100% {
      transform: scale(0.95);
      box-shadow: 0 0 0 0 rgba(70, 131, 179, 0);
    }
  }"""

html = html.replace(old_css, new_css)

# 2. Add the pulsing dot element into the top bar HTML
old_html = """<div class="offer-bar"><b>EXCLUSIVE OFFER</b> &mdash; pre-negotiated for CSL borrowers</div>"""
new_html = """<div class="offer-bar"><span class="offer-pulse"></span><b>EXCLUSIVE OFFER</b> &mdash; pre-negotiated for CSL borrowers</div>"""

html = html.replace(old_html, new_html)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Top bar polished with larger font and animated pulse dot!")
