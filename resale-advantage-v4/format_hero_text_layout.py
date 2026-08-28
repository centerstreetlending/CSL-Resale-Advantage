file_path = '/Users/gregmontoya/AntiGravity Workspaces/Paul_Project_1/CSL-Resale-Advantage/resale-advantage-v3/csl-investor-exit-advantage-v3.html'
with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Add CSS styles for the new text layout (Subheading, Bullets, Note, and Rating row)
layout_styles = """  /* Hero Text Layout Styles (BiggerPockets theme) */
  .hero-subheading {
    font-size: 1.4rem;
    font-weight: 700;
    color: #fff;
    margin: 24px 0 10px;
    font-family: 'Roboto', sans-serif;
    letter-spacing: -0.01em;
  }
  .hero-lead-para {
    font-size: 1.08rem;
    line-height: 1.6;
    color: rgba(255, 255, 255, 0.85);
    margin-bottom: 16px;
    font-family: 'Roboto', sans-serif;
  }
  .hero-bullets {
    list-style: none;
    padding: 0;
    margin: 0 0 20px 0;
    display: flex;
    flex-direction: column;
    gap: 12px;
  }
  .hero-bullets li {
    position: relative;
    padding-left: 20px;
    font-size: 1.02rem;
    line-height: 1.5;
    color: rgba(255, 255, 255, 0.85);
    font-family: 'Roboto', sans-serif;
  }
  .hero-bullets li::before {
    content: "•";
    color: var(--accent);
    font-weight: bold;
    font-size: 1.4rem;
    position: absolute;
    left: 0;
    top: -2px;
  }
  .hero-bullets li strong {
    color: #fff;
    font-weight: 700;
  }
  .hero-note {
    font-size: 0.9rem;
    line-height: 1.5;
    color: rgba(255, 255, 255, 0.6);
    margin: 20px 0;
    font-family: 'Roboto', sans-serif;
  }
  .hero-note strong {
    color: rgba(255, 255, 255, 0.8);
    font-weight: 700;
  }
  .hero-rating-row {
    display: flex;
    align-items: center;
    gap: 8px;
    margin-top: 18px;
    font-family: 'Roboto', sans-serif;
    font-size: 0.95rem;
  }
  .rating-label {
    font-weight: 700;
    color: #fff;
  }
  .rating-stars {
    color: #00b67a;
    font-size: 1.15rem;
    letter-spacing: 2px;
  }
  .rating-text {
    color: rgba(255, 255, 255, 0.7);
  }"""

# Insert layout_styles into CSS stylesheet
html = html.replace(
    "  header.scrolled {\n    padding: 10px 0;\n    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);\n  }",
    "  header.scrolled {\n    padding: 10px 0;\n    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);\n  }\n\n" + layout_styles
)

# Remove unused savings boxes styles from stylesheet
html = html.replace(
    """  .hero-savings { display: flex; gap: 14px; flex-wrap: wrap; margin: 22px 0 26px; }
  .save { 
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
    white-space: nowrap;
  }""",
    ""
)

# Remove old mobile savings stacking from stylesheet
html = html.replace(
    """    /* Mobile Savings Boxes Stacking */
    .hero-savings { flex-direction: column; gap: 12px; margin: 20px 0; }
    .save { max-width: none; width: 100%; }""",
    ""
)

# 2. Update HTML of hero-left
old_hero_left = """      <div class="hero-left">
      <div class="hero-left-top">
        <div class="hero-eyebrow">CSL RESALE ADVANTAGE PROGRAM</div>
        <h1><span style="display: inline-block; white-space: nowrap;">WE MADE IT <span class="hl">EASIER & CHEAPER</span></span><br><span style="display: inline-block; white-space: nowrap;">TO EXIT YOUR INVESTMENT.</span></h1>

        <p class="lead">You found it, improved it, and rehabbed it... now list it at <strong>1%</strong> and close for less. We pre-negotiated an exclusive deal with <strong>Innovate Realty</strong> and <strong>Honest Escrow</strong>, just for CSL borrowers.</p>
        <div class="hero-savings">
          <div class="save"><strong>1%</strong><span>Exclusive listing fee</span></div>
          <div class="save"><strong>$500</strong><span>Seller escrow, as low as</span></div>
          <div class="save"><strong>20K</strong><span>Buyer views in 21 days</span></div>
        </div>
      </div>
      <div class="hero-cta">
        <a class="btn" href="#optin">Request Information <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M12 4l-1.41 1.41L16.17 11H4v2h12.17l-5.58 5.59L12 20l8-8-8-8z" fill="currentColor"/></svg></a>
      </div>
      <div class="hero-optional">Entirely optional &mdash; you're always free to choose your own broker, escrow company, and other providers.</div>
    </div>"""

# Reconstruct using the new hierarchy: Eyebrow, H1, H2, Paragraph, Bullets, Note, CTA, Rating row
new_hero_left = """      <div class="hero-left">
      <div class="hero-left-top">
        <div class="hero-eyebrow">CSL RESALE ADVANTAGE <span>PROGRAM</span></div>
        <h1><span style="display: inline-block; white-space: nowrap;">WE MADE IT <span class="hl">EASIER & CHEAPER</span></span><br><span style="display: inline-block; white-space: nowrap;">TO EXIT YOUR INVESTMENT.</span></h1>
        
        <h2 class="hero-subheading">The CSL Resale Advantage</h2>
        <p class="hero-lead-para">We pre-negotiated an exclusive exit program with Innovate Realty and Honest Escrow to help CSL borrowers maximize their profit on the sale side of their projects:</p>
        
        <ul class="hero-bullets">
          <li><strong>1% Exclusive Listing Fee:</strong> Save thousands on commission with our dedicated real estate partner.</li>
          <li><strong>$500 Seller Escrow:</strong> Keep exit costs low with seller escrow starting at just $500.</li>
          <li><strong>20K Buyer Views:</strong> Accelerate your resale with 20K buyer views in the first 21 days.</li>
        </ul>
        
        <p class="hero-note"><strong>Note:</strong> This pre-negotiated program is entirely optional. You are always free to choose your own broker, escrow company, and other providers.</p>
      </div>
      
      <div class="hero-cta">
        <a class="btn" href="#optin">Request Information <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M12 4l-1.41 1.41L16.17 11H4v2h12.17l-5.58 5.59L12 20l8-8-8-8z" fill="currentColor"/></svg></a>
      </div>
      
      <div class="hero-rating-row">
        <span class="rating-label">Excellent</span>
        <span class="rating-stars">★★★★★</span>
        <span class="rating-text">based on 100+ CSL borrower exits</span>
      </div>
    </div>"""

html = html.replace(old_hero_left, new_hero_left)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Hero layout updated to match BiggerPockets text/bullet structure and trust rating added!")
