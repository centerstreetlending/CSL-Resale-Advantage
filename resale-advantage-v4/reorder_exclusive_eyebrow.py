file_path = '/Users/gregmontoya/AntiGravity Workspaces/Paul_Project_1/CSL-Resale-Advantage/resale-advantage-v3/csl-investor-exit-advantage-v3.html'
with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update Hero Left Top HTML structure:
# - Remove the old .hero-brand-row
# - Add back .hero-eyebrow at the top containing "EXCLUSIVE OFFER — PRE-NEGOTIATED FOR CSL BORROWERS" (with "EXCLUSIVE OFFER" in brand blue span)
# - Place the CSL logo below the eyebrow
# - Place the H1 headline below the logo

old_hero_top = """    <div class="hero-left">
      <div class="hero-left-top">
        <div class="hero-brand-row">
          <img src="logo1.svg" alt="Center Street Lending" style="height: 32px; width: auto; display: block;">
          <span class="brand-divider">|</span>
          <span class="brand-text"><b>EXCLUSIVE OFFER</b> &mdash; PRE-NEGOTIATED FOR CSL BORROWERS</span>
        </div>
        <h1><span style="display: inline-block; white-space: nowrap;">WE MADE IT <span class="hl">EASIER & CHEAPER</span></span><br><span style="display: inline-block; white-space: nowrap;">TO EXIT YOUR INVESTMENT.</span></h1>"""

new_hero_top = """    <div class="hero-left">
      <div class="hero-left-top">
        <div class="hero-eyebrow"><span style="color: var(--accent);">EXCLUSIVE OFFER</span> &mdash; PRE-NEGOTIATED FOR CSL BORROWERS</div>
        <img src="logo1.svg" alt="Center Street Lending" style="height: 36px; width: auto; display: block; margin-bottom: 16px;">
        <h1><span style="display: inline-block; white-space: nowrap;">WE MADE IT <span class="hl">EASIER & CHEAPER</span></span><br><span style="display: inline-block; white-space: nowrap;">TO EXIT YOUR INVESTMENT.</span></h1>"""

html = html.replace(old_hero_top, new_hero_top)

# 2. Update CSS:
# - Clean up the unused .hero-brand-row, .brand-divider, and .brand-text mobile styling
# - Add .hero-eyebrow font-size and line-height scale down on mobile (640px query)
html = html.replace(
    """    /* Mobile Brand Tag stacking */
    .hero-brand-row { flex-direction: column; align-items: flex-start; gap: 8px; margin-bottom: 16px; }
    .brand-divider { display: none; }
    .brand-text { font-size: 0.95rem !important; }""",
    """    /* Mobile Eyebrow adjustment */
    .hero-eyebrow { font-size: 0.8rem !important; line-height: 1.4 !important; margin-bottom: 12px !important; }"""
)

# Remove the unused styles in CSS to keep it clean
html = html.replace(
    """  /* Hero Brand Tag Styles */
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
  }""",
    ""
)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Exclusive offer text successfully styled as eyebrow with blue accent line and placed above CSL logo!")
