file_path = '/Users/gregmontoya/AntiGravity Workspaces/Paul_Project_1/CSL-Resale-Advantage/resale-advantage-v3/csl-investor-exit-advantage-v3.html'
with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update the CSS media queries to handle narrow viewport wrapping cleanly and ensure no overflow:
# - Set flex-wrap: wrap for offer-bar on mobile so it wraps naturally without horizontal scrolling overflow.
# - Clean up the header logo and phone text sizing to fit perfectly on very narrow screens (down to 320px).
# - Override header height to auto !important on mobile.

old_media_queries = """  @media(max-width:1100px){
    header { padding: 16px 0; height: auto; }
    header .wrap { padding: 0 24px; }
    .hero { padding: 40px 0; }
    .hero-main-row { flex-direction: column; align-items: center; }
    .hero-right { width: 100%; max-width: 572px; padding: 40px 24px; margin-top: 24px; }
    .hero h1 { font-family: 'Arteria Std Compress', 'Bebas Neue', sans-serif; font-size: 52px; line-height: 52px; }
  }
  @media(max-width:640px){
    .offer-bar { 
      font-size: 0.75rem; 
      padding: 8px 12px; 
      line-height: 1.4;
      flex-wrap: nowrap;
      justify-content: center;
      gap: 6px;
    }
    .offer-pulse {
      flex-shrink: 0;
    }
    header { padding: 12px 0; height: auto; }
    header .wrap { padding: 0 16px; }
    header a.phone { font-size: 0.82rem; }
    header a.wordmark img { height: 26px !important; }
    .hero-cta { flex-direction: column; gap: 16px; align-items: stretch; width: 100%; }
    .hero-cta .btn { justify-content: center; width: 100%; }
    .stat-card .num { font-size: 48px; line-height: 48px; }
  }"""

new_media_queries = """  @media(max-width:1100px){
    header { padding: 16px 0; height: auto !important; }
    header .wrap { padding: 0 24px; }
    .hero { padding: 40px 0; }
    .hero-main-row { flex-direction: column; align-items: center; }
    .hero-right { width: 100%; max-width: 572px; padding: 40px 24px; margin-top: 24px; }
    .hero h1 { font-family: 'Arteria Std Compress', 'Bebas Neue', sans-serif; font-size: 52px; line-height: 52px; }
  }
  @media(max-width:640px){
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
  }
  @media(max-width:380px){
    header a.wordmark img { height: 22px !important; }
    header a.phone { font-size: 0.78rem; }
    .offer-bar { font-size: 0.72rem; padding: 8px 10px; }
  }"""

html = html.replace(old_media_queries, new_media_queries)

# 2. Modify the HTML of the top offer bar to wrap the pulsing dot and EXCLUSIVE OFFER together 
# in an inline flex span so they stay unified on mobile when wrapping happens.
old_offer_html = """<div class="offer-bar"><span class="offer-pulse"></span><b>EXCLUSIVE OFFER</b> &mdash; pre-negotiated for CSL borrowers</div>"""
new_offer_html = """<div class="offer-bar"><span style="display: inline-flex; align-items: center; gap: 6px; white-space: nowrap;"><span class="offer-pulse"></span><b>EXCLUSIVE OFFER</b></span> &mdash; pre-negotiated for CSL borrowers</div>"""

html = html.replace(old_offer_html, new_offer_html)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Responsive mobile nav and header optimized!")
