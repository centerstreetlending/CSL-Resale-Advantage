file_path = '/Users/gregmontoya/AntiGravity Workspaces/Paul_Project_1/CSL-Resale-Advantage/resale-advantage-v3/csl-investor-exit-advantage-v3.html'
with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update CSS for .hero-optional to be left-aligned, muted, and clean
old_css = '.hero-optional { color: rgba(255, 255, 255, 0.85); font-size: 0.95rem; line-height: 1.5; text-align: center; max-width: none; width: 100%; margin-top: 40px; font-weight: 500; }'
new_css = '.hero-optional { color: rgba(255, 255, 255, 0.7); font-size: 0.85rem; line-height: 1.4; text-align: left; max-width: 620px; margin-top: 20px; }'

html = html.replace(old_css, new_css)

# 2. Relocate the HTML element from the bottom of the hero to inside the left column, under the CTA button
old_bottom_part = """  </div>
  <div class="wrap">
    <div class="hero-optional">Entirely optional &mdash; you're always free to choose your own broker, escrow company, and other providers. Currently limited to California Only.</div>
  </div>
</div>"""

new_bottom_part = """  </div>
</div>"""

html = html.replace(old_bottom_part, new_bottom_part)

old_cta_part = """      <div class="hero-cta">
        <a class="btn" href="#optin">Request Information <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M12 4l-1.41 1.41L16.17 11H4v2h12.17l-5.58 5.59L12 20l8-8-8-8z" fill="currentColor"/></svg></a>
      </div>
    </div>"""

new_cta_part = """      <div class="hero-cta">
        <a class="btn" href="#optin">Request Information <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M12 4l-1.41 1.41L16.17 11H4v2h12.17l-5.58 5.59L12 20l8-8-8-8z" fill="currentColor"/></svg></a>
      </div>
      <div class="hero-optional">Entirely optional &mdash; you're always free to choose your own broker, escrow company, and other providers. Currently limited to California Only.</div>
    </div>"""

html = html.replace(old_cta_part, new_cta_part)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Disclosure relocated under the CTA button and styled cleanly.")
