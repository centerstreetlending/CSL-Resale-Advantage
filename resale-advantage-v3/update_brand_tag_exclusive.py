file_path = '/Users/gregmontoya/AntiGravity Workspaces/Paul_Project_1/CSL-Resale-Advantage/resale-advantage-v3/csl-investor-exit-advantage-v3.html'
with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update the CSS to add classes for the brand tag and mobile responsive rules
brand_tag_styles = """  /* Hero Brand Tag Styles */
  .hero-brand-row {
    display: flex;
    align-items: center;
    gap: 14px;
    margin-bottom: 24px;
  }
  .brand-divider {
    color: rgba(255, 255, 255, 0.4);
    font-size: 1.15rem;
    font-weight: 300;
  }
  .brand-text {
    color: rgba(255, 255, 255, 0.85);
    font-size: 1.15rem;
    font-weight: 300;
    font-family: 'Roboto', sans-serif;
    letter-spacing: 0.02em;
  }
  .brand-text b {
    color: var(--accent);
    font-weight: 700;
    text-transform: uppercase;
  }"""

# Insert brand_tag_styles into the CSS stylesheet (we can put it before the media queries)
html = html.replace(
    "  header.scrolled {\n    padding: 10px 0;\n    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);\n  }",
    "  header.scrolled {\n    padding: 10px 0;\n    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);\n  }\n\n" + brand_tag_styles
)

# Add mobile responsive override in the max-width: 640px query
html = html.replace(
    "    /* Mobile Savings Boxes Stacking */",
    """    /* Mobile Brand Tag stacking */
    .hero-brand-row { flex-direction: column; align-items: flex-start; gap: 8px; margin-bottom: 16px; }
    .brand-divider { display: none; }
    .brand-text { font-size: 0.95rem !important; }
    
    /* Mobile Savings Boxes Stacking */"""
)

# 2. Replace the HTML inside the hero-left-top with the new markup
old_markup = """        <div class="hero-brand-row" style="display: flex; align-items: center; gap: 14px; margin-bottom: 24px;">
          <img src="logo1.svg" alt="Center Street Lending" style="height: 32px; width: auto; display: block;">
          <span style="color: rgba(255, 255, 255, 0.8); font-size: 1.15rem; font-weight: 300; font-family: 'Roboto', sans-serif; letter-spacing: 0.02em;">| &nbsp; Borrower Offer</span>
        </div>"""

new_markup = """        <div class="hero-brand-row">
          <img src="logo1.svg" alt="Center Street Lending" style="height: 32px; width: auto; display: block;">
          <span class="brand-divider">|</span>
          <span class="brand-text"><b>EXCLUSIVE OFFER</b> &mdash; pre-negotiated for CSL borrowers</span>
        </div>"""

html = html.replace(old_markup, new_markup)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Hero brand row updated to show CSL Logo | EXCLUSIVE OFFER!")
