file_path = '/Users/gregmontoya/AntiGravity Workspaces/Paul_Project_1/CSL-Resale-Advantage/resale-advantage-v3/csl-investor-exit-advantage-v3.html'
with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Restore the tk- CSS classes for styling the animated ticker
ticker_styles = """  .tk-label { 
    display: block; 
    font-size: 0.8rem; 
    font-weight: 700;
    text-transform: uppercase; 
    letter-spacing: 0.15em; 
    color: rgba(255, 255, 255, 0.85); 
    text-align: center; 
  }
  .tk-num { 
    display: block; 
    font-size: 5rem; 
    font-weight: 800; 
    color: #fff; 
    line-height: 1.0; 
    margin: 12px 0; 
    text-align: center; 
    font-family: 'Roboto', sans-serif; 
    letter-spacing: -0.03em;
    text-shadow: 0 0 20px rgba(255, 255, 255, 0.15);
  }
  .tk-sub { 
    font-size: 0.95rem; 
    color: rgba(255, 255, 255, 0.9); 
    line-height: 1.5; 
    text-align: center;
    font-weight: 400;
  }"""

# Remove the double stat card CSS styles
html = html.replace(
    """  .stat-card { 
    display: flex; 
    flex-direction: column; 
    align-items: center; 
    gap: 6px; 
    width: 100%;
  }
  .stat-card:not(:last-child) {
    border-bottom: 1px solid rgba(255, 255, 255, 0.12);
    padding-bottom: 24px;
    margin-bottom: 12px;
  }
  .stat-num { 
    display: block; 
    font-size: 3.8rem; 
    font-weight: 800; 
    color: #fff; 
    line-height: 1.05; 
    text-align: center; 
    font-family: 'Roboto', sans-serif; 
    letter-spacing: -0.02em;
    text-shadow: 0 0 20px rgba(255, 255, 255, 0.1);
  }
  .stat-sub { 
    font-size: 0.88rem; 
    color: rgba(255, 255, 255, 0.82); 
    line-height: 1.4; 
    text-align: center;
    font-weight: 400;
  }""",
    ticker_styles
)

# 2. Re-insert the ticker HTML back into the hero-right container
old_double_stats = """    <div class="hero-right">
      <div class="stat-card">
        <span class="stat-num">100+</span>
        <span class="stat-sub">CSL Borrowers selling Properties through CSL Resale Advantage Program</span>
      </div>
      <div class="stat-card">
        <span class="stat-num">$2.4M+</span>
        <span class="stat-sub">Estimated Total Exit Cost Savings with CSL Resale Advantage Program</span>
      </div>
    </div>"""

new_ticker_html = """    <div class="hero-right">
      <span class="tk-label">Borrowers using the program</span>
      <span class="tk-num" id="deal-ticker" data-target="100">0</span>
      <span class="tk-sub">homes sold through CSL Resale Advantage</span>
    </div>"""

html = html.replace(old_double_stats, new_ticker_html)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Ticker restored successfully on the right-hand side!")
