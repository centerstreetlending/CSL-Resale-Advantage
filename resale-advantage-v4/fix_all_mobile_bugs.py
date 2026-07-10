file_path = '/Users/gregmontoya/AntiGravity Workspaces/Paul_Project_1/CSL-Resale-Advantage/resale-advantage-v3/csl-investor-exit-advantage-v3.html'
with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Correct the eyebrow text color to brand steel blue (var(--accent))
html = html.replace(
    '  .hero-eyebrow { \n    display: inline-block; \n    align-self: flex-start; \n    border-left: 4px solid var(--accent); \n    color: #fff; ',
    '  .hero-eyebrow { \n    display: inline-block; \n    align-self: flex-start; \n    border-left: 4px solid var(--accent); \n    color: var(--accent); '
)

# 2. Add H1 wrapper override and savings boxes vertical stacking in the max-width: 640px media query
old_640_query = """  @media(max-width:640px){
    .offer-bar { 
      font-size: 0.78rem; 
      padding: 10px 16px; 
      line-height: 1.4;
      flex-wrap: wrap;
      justify-content: center;
      gap: 6px 8px;
    }
    .offer-pulse {
      flex-shrink: 0;
    }
    header { padding: 12px 0; height: auto !important; }
    header .wrap { padding: 0 16px; }
    header a.phone { font-size: 0.85rem; font-weight: 700; }
    header a.wordmark img { height: 26px !important; }
    .hero-cta { flex-direction: column; gap: 16px; align-items: stretch; width: 100%; }
    .hero-cta .btn { justify-content: center; width: 100%; }
    .stat-card .num { font-size: 48px; line-height: 48px; }
  }"""

new_640_query = """  @media(max-width:640px){
    .offer-bar { 
      font-size: 0.78rem; 
      padding: 10px 16px; 
      line-height: 1.4;
      flex-wrap: wrap;
      justify-content: center;
      gap: 6px 8px;
    }
    .offer-pulse {
      flex-shrink: 0;
    }
    header { padding: 12px 0; height: auto !important; }
    header .wrap { padding: 0 16px; }
    header a.phone { font-size: 0.85rem; font-weight: 700; }
    header a.wordmark img { height: 26px !important; }
    
    /* Mobile H1 Overlap & Sizing fixes */
    .hero h1 { font-size: 40px !important; line-height: 44px !important; }
    .hero h1 span { white-space: normal !important; display: inline !important; }
    
    /* Mobile Savings Boxes Stacking */
    .hero-savings { flex-direction: column; gap: 12px; margin: 20px 0; }
    .save { max-width: none; width: 100%; }
    
    .hero-cta { flex-direction: column; gap: 16px; align-items: stretch; width: 100%; }
    .hero-cta .btn { justify-content: center; width: 100%; }
    .stat-card .num { font-size: 48px; line-height: 48px; }
  }"""

html = html.replace(old_640_query, new_640_query)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Mobile H1 clipping, savings boxes stacking, and blue eyebrow fixed!")
