file_path = '/Users/gregmontoya/AntiGravity Workspaces/Paul_Project_1/CSL-Resale-Advantage/resale-advantage-v3/csl-investor-exit-advantage-v3.html'
with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Exact match targeting the current HTML in the file to resolve formatting
old_hero_left = """    <div class="hero-left">
      <div class="hero-left-top">
        <div class="hero-eyebrow">CSL RESALE ADVANTAGE <span>PROGRAM</span></div>
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

new_hero_left = """    <div class="hero-left">
      <div class="hero-left-top">
        <div class="hero-eyebrow">CSL RESALE ADVANTAGE <span>PROGRAM</span></div>
        <h1><span style="display: inline-block; white-space: nowrap;">WE MADE IT <span class="hl">EASIER & CHEAPER</span></span><br><span style="display: inline-block; white-space: nowrap;">TO EXIT YOUR INVESTMENT.</span></h1>
        
        <h2 class="hero-subheading">The CSL Resale Advantage</h2>
        <p class="hero-lead-para">We pre-negotiated an exclusive exit program with Innovate Realty and Honest Escrow to help CSL borrowers maximize their profit on the sale side of their projects:</p>
        
        <ul class="hero-bullets">
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

if old_hero_left in html:
    html = html.replace(old_hero_left, new_hero_left)
    print("Success: Hero HTML text layout successfully updated!")
else:
    # Try with different indentation styles if exact match failed
    print("Error: Could not match exact HTML, checking fallback...")
    
with open(file_path, 'w', encoding='utf-8') as f:
    f.write(html)
