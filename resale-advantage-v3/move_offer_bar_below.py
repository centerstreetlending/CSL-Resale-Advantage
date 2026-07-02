file_path = '/Users/gregmontoya/AntiGravity Workspaces/Paul_Project_1/CSL-Resale-Advantage/resale-advantage-v3/csl-investor-exit-advantage-v3.html'
with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Remove the offer-bar from the top (above header)
# We match both possible variations
old_offer_bar1 = """<div class="offer-bar"><a href="#optin" style="color: inherit; text-decoration: none; display: flex; align-items: center; justify-content: center; gap: 8px;"><span class="offer-pulse"></span><b>EXCLUSIVE OFFER &gt;</b></a></div>

<header id="sticky-header">"""

old_offer_bar2 = """<div class="offer-bar"><a href="#optin" style="color: inherit; text-decoration: none; display: flex; align-items: center; justify-content: center; gap: 8px;"><span class="offer-pulse"></span><b>EXCLUSIVE OFFER &gt;</b></a></div>
<header id="sticky-header">"""

# Replace with header alone
html = html.replace(old_offer_bar1, '<header id="sticky-header">')
html = html.replace(old_offer_bar2, '<header id="sticky-header">')

# 2. Place the offer-bar BELOW the header, and change its text to "PRE-NEGOTIATED FOR CSL BORROWERS"
target_header_end = """    <a class="phone" href="tel:5555555555">(555) 555-5555</a>
  </div>
</header>"""

replacement_header_end = """    <a class="phone" href="tel:5555555555">(555) 555-5555</a>
  </div>
</header>
<div class="offer-bar">PRE-NEGOTIATED FOR CSL BORROWERS</div>"""

html = html.replace(target_header_end, replacement_header_end)

# 3. Simplify the hero layout: Remove the .hero-brand-row with the logo-tag, and just leave a plain logo image above the eyebrow
old_hero_top = """    <div class="hero-left">
      <div class="hero-left-top">
        <div class="hero-brand-row">
          <img src="logo1.svg" alt="Center Street Lending" style="height: 32px; width: auto; display: block;">
          <span class="brand-divider">|</span>
          <span class="brand-text">PRE-NEGOTIATED FOR CSL BORROWERS</span>
        </div>
        <div class="hero-eyebrow">CSL RESALE ADVANTAGE PROGRAM</div>"""

new_hero_top = """    <div class="hero-left">
      <div class="hero-left-top">
        <img src="logo1.svg" alt="Center Street Lending" style="height: 36px; width: auto; display: block; margin-bottom: 16px;">
        <div class="hero-eyebrow">CSL RESALE ADVANTAGE PROGRAM</div>"""

html = html.replace(old_hero_top, new_hero_top)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Offer bar moved below nav and updated to 'PRE-NEGOTIATED FOR CSL BORROWERS' successfully!")
