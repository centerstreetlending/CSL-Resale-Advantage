file_path = '/Users/gregmontoya/AntiGravity Workspaces/Paul_Project_1/CSL-Resale-Advantage/resale-advantage-v3/csl-investor-exit-advantage-v3.html'
with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Let's inspect the exact lines we want to replace.
# The end of hero-left currently is:
#       <div class="hero-cta">
#         <a class="btn" href="#optin">Request Information <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M12 4l-1.41 1.41L16.17 11H4v2h12.17l-5.58 5.59L12 20l8-8-8-8z" fill="currentColor"/></svg></a>
#         <a class="btn-ghost" href="tel:9492441090">or call 949-244-1090</a>
#       </div>
#     </div>

# The end of the hero block is:
#     <div class="hero-right">
#       <div class="stat-card">
#         <div class="num">100+</div>
#         <div class="sub">CSL Borrowers selling Properties through CSL Resale Advantage Program</div>
#       </div>
#       <div class="stat-card">
#         <div class="num">$2.4M+</div>
#         <div class="sub">Estimated Total Exit Cost Savings with CSL Resale Advantage Program</div>
#       </div>
#     </div>
#       <div class="hero-optional">Entirely optional &mdash; you're always free to choose your own broker, escrow company, and other providers. Currently limited to California Only.</div>
#     </div>
#   </div>
# </div>

# We will swap the placement of hero-optional to be inside hero-left.

target = """      <div class="hero-cta">
        <a class="btn" href="#optin">Request Information <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M12 4l-1.41 1.41L16.17 11H4v2h12.17l-5.58 5.59L12 20l8-8-8-8z" fill="currentColor"/></svg></a>
        <a class="btn-ghost" href="tel:9492441090">or call 949-244-1090</a>
      </div>
    </div>
    
    <div class="hero-right">
      <div class="stat-card">
        <div class="num">100+</div>
        <div class="sub">CSL Borrowers selling Properties through CSL Resale Advantage Program</div>
      </div>
      <div class="stat-card">
        <div class="num">$2.4M+</div>
        <div class="sub">Estimated Total Exit Cost Savings with CSL Resale Advantage Program</div>
      </div>
    </div>
      <div class="hero-optional">Entirely optional &mdash; you're always free to choose your own broker, escrow company, and other providers. Currently limited to California Only.</div>
    </div>"""

replacement = """      <div class="hero-cta">
        <a class="btn" href="#optin">Request Information <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M12 4l-1.41 1.41L16.17 11H4v2h12.17l-5.58 5.59L12 20l8-8-8-8z" fill="currentColor"/></svg></a>
        <a class="btn-ghost" href="tel:9492441090">or call 949-244-1090</a>
      </div>
      <div class="hero-optional">Entirely optional &mdash; you're always free to choose your own broker, escrow company, and other providers. Currently limited to California Only.</div>
    </div>
    
    <div class="hero-right">
      <div class="stat-card">
        <div class="num">100+</div>
        <div class="sub">CSL Borrowers selling Properties through CSL Resale Advantage Program</div>
      </div>
      <div class="stat-card">
        <div class="num">$2.4M+</div>
        <div class="sub">Estimated Total Exit Cost Savings with CSL Resale Advantage Program</div>
      </div>
    </div>
    </div>"""

if target in html:
    html = html.replace(target, replacement)
    print("Direct target matched and replaced.")
else:
    # Let's do a more robust regex check
    import re
    # We want to match the whole block and restructure it.
    print("Direct replacement failed, will search with a relaxed approach.")
    # Let's inspect what we have in HTML first by finding parts.
    if "hero-right" in html:
        print("Found hero-right")
    if "hero-optional" in html:
        print("Found hero-optional")

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(html)
