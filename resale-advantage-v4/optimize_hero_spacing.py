file_path = '/Users/gregmontoya/AntiGravity Workspaces/Paul_Project_1/CSL-Resale-Advantage/resale-advantage-v3/csl-investor-exit-advantage-v3.html'
with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update CSS:
# - Adjust .hero-left flex gap to 24px (down from 28px) for tighter section grouping.
# - Clean up .hero-optional to remove extra top margins so it sits closer to the button.
# - Ensure .hero-note has a tight bottom margin (0px) so the spacing above the CTA button is clean (24px).

html = html.replace(
    "  .hero-left { flex: 1; max-width: 800px; display: flex; flex-direction: column; gap: 28px; }",
    "  .hero-left { flex: 1; max-width: 800px; display: flex; flex-direction: column; gap: 24px; }"
)

html = html.replace(
    "  .hero-note {\n    font-size: 0.9rem;\n    line-height: 1.5;\n    color: rgba(255, 255, 255, 0.6);\n    margin: 20px 0;\n    font-family: 'Roboto', sans-serif;\n  }",
    "  .hero-note {\n    font-size: 0.9rem;\n    line-height: 1.5;\n    color: rgba(255, 255, 255, 0.6);\n    margin: 20px 0 0 0;\n    font-family: 'Roboto', sans-serif;\n  }"
)

# Update .hero-optional stylesheet rule to set a tight margin-top (10px) to lock it to the button
old_optional_css = "  .hero-optional { color: rgba(255, 255, 255, 0.7); font-size: 0.85rem; line-height: 1.4; text-align: left; max-width: 620px; margin-top: 20px; }"
new_optional_css = "  .hero-optional { color: rgba(255, 255, 255, 0.6); font-size: 0.85rem; line-height: 1.45; text-align: left; max-width: 620px; margin-top: 10px; }"
html = html.replace(old_optional_css, new_optional_css)

# 2. Update HTML: Nest the .hero-optional note directly inside the .hero-cta container.
# This aligns them as a single logical block, ensuring the disclaimer sits exactly 10px under the button
# on all devices, rather than being pushed away by the parent flexbox gap.

old_cta_block = """      <div class="hero-cta">
        <a class="btn" href="#optin">Request Information <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M12 4l-1.41 1.41L16.17 11H4v2h12.17l-5.58 5.59L12 20l8-8-8-8z" fill="currentColor"/></svg></a>
      </div>
      <div class="hero-optional"><strong>Note:</strong> This pre-negotiated program is entirely optional. You are always free to choose your own broker, escrow company, and other providers.</div>"""

new_cta_block = """      <div class="hero-cta" style="display: flex; flex-direction: column; align-items: flex-start;">
        <a class="btn" href="#optin">Request Information <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M12 4l-1.41 1.41L16.17 11H4v2h12.17l-5.58 5.59L12 20l8-8-8-8z" fill="currentColor"/></svg></a>
        <div class="hero-optional"><strong>Note:</strong> This pre-negotiated program is entirely optional. You are always free to choose your own broker, escrow company, and other providers.</div>
      </div>"""

html = html.replace(old_cta_block, new_cta_block)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Hero layout vertical spacing optimized successfully!")
