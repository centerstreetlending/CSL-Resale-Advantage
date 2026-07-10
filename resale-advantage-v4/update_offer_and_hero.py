file_path = '/Users/gregmontoya/AntiGravity Workspaces/Paul_Project_1/CSL-Resale-Advantage/resale-advantage-v3/csl-investor-exit-advantage-v3.html'
with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update the top announcement bar to just show the pulsing dot and "EXCLUSIVE OFFER >" (linked to the opt-in form)
old_top_bar = """<div class="offer-bar"><span style="display: inline-flex; align-items: center; gap: 6px; white-space: nowrap;"><span class="offer-pulse"></span><b>EXCLUSIVE OFFER</b></span> &mdash; pre-negotiated for CSL borrowers</div>"""

new_top_bar = """<div class="offer-bar"><a href="#optin" style="color: inherit; text-decoration: none; display: flex; align-items: center; justify-content: center; gap: 8px;"><span class="offer-pulse"></span><b>EXCLUSIVE OFFER &gt;</b></a></div>"""

html = html.replace(old_top_bar, new_top_bar)

# 2. Remove the "EXCLUSIVE OFFER" eyebrow from the hero text column header spot
old_hero_top = """    <div class="hero-left">
      <div class="hero-left-top">
        <div class="hero-eyebrow" style="color: var(--accent);">EXCLUSIVE OFFER</div>
        <div class="hero-brand-row">"""

new_hero_top = """    <div class="hero-left">
      <div class="hero-left-top">
        <div class="hero-brand-row">"""

html = html.replace(old_hero_top, new_hero_top)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Top bar updated to EXCLUSIVE OFFER > and hero eyebrow removed successfully!")
