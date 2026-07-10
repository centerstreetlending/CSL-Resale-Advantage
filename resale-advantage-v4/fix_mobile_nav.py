file_path = '/Users/gregmontoya/AntiGravity Workspaces/Paul_Project_1/CSL-Resale-Advantage/resale-advantage-v3/csl-investor-exit-advantage-v3.html'
with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Let's inspect the media query blocks.
# Currently in stylesheet:
#   @media(max-width:1100px){
#     header { padding: 17px 24px; }
#     .hero { padding: 40px 24px; }
#     .hero-main-row { flex-direction: column; align-items: center; }
#     .hero-right { width: 100%; max-width: 572px; padding: 40px 24px; margin-top: 0; }
#     .hero h1 { font-family: 'Arteria Std Compress', 'Bebas Neue', sans-serif; font-size: 52px; line-height: 52px; }
#   }
#   @media(max-width:640px){
#     .stat-card .num { font-size: 48px; line-height: 48px; }
#     .hero-cta { flex-direction: column; gap: 24px; align-items: flex-start; }
#     .offer-bar { flex-direction: column; }
#   }

# We want to replace these blocks with highly polished, professional responsive rules for the header, nav, and top bar.
# Specifically:
# - Scaling logo and phone font-size on mobile so they fit side-by-side beautifully without wrapping or colliding.
# - Scaling top bar font-size and padding on mobile, and ensuring the pulsing dot stays aligned inline.
# - Setting header height: auto so it doesn't get cut off.

old_media_queries = """  @media(max-width:1100px){
    header { padding: 17px 24px; }
    .hero { padding: 40px 24px; }
    .hero-main-row { flex-direction: column; align-items: center; }
    .hero-right { width: 100%; max-width: 572px; padding: 40px 24px; margin-top: 0; }
    .hero h1 { font-family: 'Arteria Std Compress', 'Bebas Neue', sans-serif; font-size: 52px; line-height: 52px; }
  }
  @media(max-width:640px){
    .stat-card .num { font-size: 48px; line-height: 48px; }
    .hero-cta { flex-direction: column; gap: 24px; align-items: flex-start; }
    .offer-bar { flex-direction: column; }
  }"""

new_media_queries = """  @media(max-width:1100px){
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

html = html.replace(old_media_queries, new_media_queries)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Mobile navigation and header responsive styling fixed!")
