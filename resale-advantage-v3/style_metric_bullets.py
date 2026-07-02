file_path = '/Users/gregmontoya/AntiGravity Workspaces/Paul_Project_1/CSL-Resale-Advantage/resale-advantage-v3/csl-investor-exit-advantage-v3.html'
with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update CSS styles for .hero-bullets to create the key-metric layout:
# - Large brand-blue metric numbers on the left (bullet-num)
# - Vertical text block on the right (bullet-text)
old_bullet_css = """  .hero-bullets {
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
  }"""

new_bullet_css = """  .hero-bullets {
    list-style: none;
    padding: 0;
    margin: 24px 0;
    display: flex;
    flex-direction: column;
    gap: 18px;
  }
  .hero-bullets li {
    display: flex;
    align-items: flex-start;
    gap: 16px;
    font-size: 1rem;
    line-height: 1.45;
    color: rgba(255, 255, 255, 0.85);
    font-family: 'Roboto', sans-serif;
  }
  .hero-bullets li .bullet-num {
    font-size: 1.8rem;
    font-weight: 800;
    color: var(--accent);
    line-height: 1.0;
    min-width: 60px;
    text-align: right;
    letter-spacing: -0.02em;
    flex-shrink: 0;
    padding-top: 2px;
  }
  .hero-bullets li .bullet-text {
    flex: 1;
  }
  .hero-bullets li .bullet-text strong {
    color: #fff;
    font-weight: 700;
    display: block;
    font-size: 1.05rem;
    margin-bottom: 3px;
  }"""

html = html.replace(old_bullet_css, new_bullet_css)

# 2. Update the HTML inside the hero-bullets ul container
old_bullet_html = """        <ul class="hero-bullets">
          <li><strong>1% Exclusive Listing Fee:</strong> Save thousands on commission with our dedicated real estate partner.</li>
          <li><strong>$500 Seller Escrow:</strong> Keep exit costs low with seller escrow starting at just $500.</li>
          <li><strong>20K Buyer Views:</strong> Accelerate your resale with 20K buyer views in the first 21 days.</li>
        </ul>"""

new_bullet_html = """        <ul class="hero-bullets">
          <li>
            <span class="bullet-num">1%</span>
            <div class="bullet-text">
              <strong>Exclusive Listing Fee</strong>
              Save thousands on commission with our dedicated real estate partner.
            </div>
          </li>
          <li>
            <span class="bullet-num">$500</span>
            <div class="bullet-text">
              <strong>Seller Escrow</strong>
              Keep exit costs low with seller escrow starting as low as $500.
            </div>
          </li>
          <li>
            <span class="bullet-num">20K</span>
            <div class="bullet-text">
              <strong>Buyer Views</strong>
              Accelerate your resale with 20K buyer views in the first 21 days.
            </div>
          </li>
        </ul>"""

html = html.replace(old_bullet_html, new_bullet_html)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Hero bullets updated to the high-contrast key-metric layout!")
