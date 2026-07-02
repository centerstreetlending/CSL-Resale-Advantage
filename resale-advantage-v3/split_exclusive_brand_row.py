file_path = '/Users/gregmontoya/AntiGravity Workspaces/Paul_Project_1/CSL-Resale-Advantage/resale-advantage-v3/csl-investor-exit-advantage-v3.html'
with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Re-add CSS styles for the brand tag row and clean up mobile overrides
brand_tag_styles = """  /* Hero Brand Tag Styles */
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
  }"""

html = html.replace(
    "  header.scrolled {\n    padding: 10px 0;\n    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);\n  }",
    "  header.scrolled {\n    padding: 10px 0;\n    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);\n  }\n\n" + brand_tag_styles
)

# Replace the mobile query override for brand tag and eyebrow
html = html.replace(
    """    /* Mobile Eyebrow adjustment */
    .hero-eyebrow { font-size: 0.8rem !important; line-height: 1.4 !important; margin-bottom: 12px !important; }""",
    """    /* Mobile Brand Tag & Eyebrow stacking */
    .hero-eyebrow { margin-bottom: 12px !important; }
    .hero-brand-row { flex-direction: column; align-items: flex-start; gap: 8px; margin-bottom: 16px; }
    .brand-divider { display: none; }
    .brand-text { font-size: 0.95rem !important; }"""
)

# 2. Update HTML inside hero-left-top:
# - Eyebrow has ONLY "EXCLUSIVE OFFER" (in brand blue var(--accent))
# - Brand tag row below eyebrow has CSL logo and "| PRE-NEGOTIATED FOR CSL BORROWERS"
# - Headline below brand tag row
old_hero_top = """    <div class="hero-left">
      <div class="hero-left-top">
        <div class="hero-eyebrow"><span style="color: var(--accent);">EXCLUSIVE OFFER</span> &mdash; PRE-NEGOTIATED FOR CSL BORROWERS</div>
        <img src="logo1.svg" alt="Center Street Lending" style="height: 36px; width: auto; display: block; margin-bottom: 16px;">
        <h1><span style="display: inline-block; white-space: nowrap;">WE MADE IT <span class="hl">EASIER & CHEAPER</span></span><br><span style="display: inline-block; white-space: nowrap;">TO EXIT YOUR INVESTMENT.</span></h1>"""

new_hero_top = """    <div class="hero-left">
      <div class="hero-left-top">
        <div class="hero-eyebrow" style="color: var(--accent);">EXCLUSIVE OFFER</div>
        <div class="hero-brand-row">
          <img src="logo1.svg" alt="Center Street Lending" style="height: 32px; width: auto; display: block;">
          <span class="brand-divider">|</span>
          <span class="brand-text">PRE-NEGOTIATED FOR CSL BORROWERS</span>
        </div>
        <h1><span style="display: inline-block; white-space: nowrap;">WE MADE IT <span class="hl">EASIER & CHEAPER</span></span><br><span style="display: inline-block; white-space: nowrap;">TO EXIT YOUR INVESTMENT.</span></h1>"""

html = html.replace(old_hero_top, new_hero_top)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Split applied successfully: EXCLUSIVE OFFER as eyebrow, and PRE-NEGOTIATED FOR CSL BORROWERS side-by-side with logo!")
