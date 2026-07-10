file_path = '/Users/gregmontoya/AntiGravity Workspaces/Paul_Project_1/CSL-Resale-Advantage/resale-advantage-v3/csl-investor-exit-advantage-v3.html'
with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Target the CTA block exactly as it is now and inject the .hero-optional text right below it
target_cta = """      <div class="hero-cta">
        <a class="btn" href="#optin">Request Information <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M12 4l-1.41 1.41L16.17 11H4v2h12.17l-5.58 5.59L12 20l8-8-8-8z" fill="currentColor"/></svg></a>
        
      </div>
    </div>"""

replacement_cta = """      <div class="hero-cta">
        <a class="btn" href="#optin">Request Information <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M12 4l-1.41 1.41L16.17 11H4v2h12.17l-5.58 5.59L12 20l8-8-8-8z" fill="currentColor"/></svg></a>
      </div>
      <div class="hero-optional">Entirely optional &mdash; you're always free to choose your own broker, escrow company, and other providers.</div>
    </div>"""

if target_cta in html:
    html = html.replace(target_cta, replacement_cta)
    print("Optional text successfully inserted under the CTA button.")
else:
    print("Failed to match the target CTA block.")

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(html)
