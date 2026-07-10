file_path = '/Users/gregmontoya/AntiGravity Workspaces/Paul_Project_1/CSL-Resale-Advantage/resale-advantage-v3/csl-investor-exit-advantage-v3.html'
with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update CSS for .offer-bar:
# - Add a subtle, premium dark gradient background (metallic sheen) to draw the eye
# - Set cursor: pointer and add transition rules for smooth hover effects
# - Add hover styles: slightly lighten the background and scale the pulsing dot to make it feel highly interactive
old_css = """  .offer-bar { 
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
    border-bottom: none;
    margin: 0;
  }"""

new_css = """  .offer-bar { 
    background: linear-gradient(90deg, #171f26 0%, #24303b 50%, #171f26 100%); 
    color: #fff; 
    text-align: center; 
    padding: 12px 16px; 
    font-size: 0.92rem; 
    letter-spacing: 0.06em; 
    font-family: 'Roboto', sans-serif; 
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 8px;
    border-bottom: 1px solid rgba(255, 255, 255, 0.03);
    margin: 0;
    cursor: pointer;
    transition: background 0.3s ease, border-color 0.3s ease;
  }
  .offer-bar:hover {
    background: linear-gradient(90deg, #1b252e 0%, #2b3a47 50%, #1b252e 100%);
    border-bottom-color: rgba(70, 131, 179, 0.2);
  }
  .offer-bar a {
    color: inherit;
    text-decoration: none;
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 8px;
    width: 100%;
  }
  .offer-bar:hover .offer-pulse {
    transform: scale(1.2);
  }"""

html = html.replace(old_css, new_css)

# 2. Update HTML: Wrap the content inside the offer-bar div in a clean anchor tag pointing to #optin
old_html = """<div class="offer-bar"><span style="display: inline-flex; align-items: center; gap: 6px; white-space: nowrap;"><span class="offer-pulse"></span><b>EXCLUSIVE OFFER</b></span> &mdash; PRE-NEGOTIATED FOR CSL BORROWERS</div>"""

new_html = """<div class="offer-bar"><a href="#optin"><span style="display: inline-flex; align-items: center; gap: 6px; white-space: nowrap;"><span class="offer-pulse"></span><b>EXCLUSIVE OFFER</b></span> &mdash; PRE-NEGOTIATED FOR CSL BORROWERS</a></div>"""

html = html.replace(old_html, new_html)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Top offer bar polished with premium gradient, hover states, and opt-in link!")
