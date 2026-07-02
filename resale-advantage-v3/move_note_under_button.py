file_path = '/Users/gregmontoya/AntiGravity Workspaces/Paul_Project_1/CSL-Resale-Advantage/resale-advantage-v3/csl-investor-exit-advantage-v3.html'
with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Remove the note from above the CTA button in the hero-left-top block
old_note = """        <p class="hero-note"><strong>Note:</strong> This pre-negotiated program is entirely optional. You are always free to choose your own broker, escrow company, and other providers.</p>"""

html = html.replace(old_note + "\n", "")
html = html.replace(old_note, "")

# 2. Place the note under the Request Information CTA button (.hero-cta) with .hero-optional styling
old_cta_block = """      <div class="hero-cta">
        <a class="btn" href="#optin">Request Information <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M12 4l-1.41 1.41L16.17 11H4v2h12.17l-5.58 5.59L12 20l8-8-8-8z" fill="currentColor"/></svg></a>
      </div>"""

new_cta_block = """      <div class="hero-cta">
        <a class="btn" href="#optin">Request Information <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M12 4l-1.41 1.41L16.17 11H4v2h12.17l-5.58 5.59L12 20l8-8-8-8z" fill="currentColor"/></svg></a>
      </div>
      <div class="hero-optional"><strong>Note:</strong> This pre-negotiated program is entirely optional. You are always free to choose your own broker, escrow company, and other providers.</div>"""

html = html.replace(old_cta_block, new_cta_block)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Note successfully moved below the CTA button!")
