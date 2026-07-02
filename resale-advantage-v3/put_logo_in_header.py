file_path = '/Users/gregmontoya/AntiGravity Workspaces/Paul_Project_1/CSL-Resale-Advantage/resale-advantage-v3/csl-investor-exit-advantage-v3.html'
with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update the Header HTML: Remove the program-title text and put the CSL corporate logo image (logo1.svg) back in the header
old_header_html = """<header id="sticky-header">
  <div class="wrap">
    <div class="nav-left">
      <span class="program-title">CSL Resale Advantage <span>Program</span></span>
    </div>
    <a class="phone" href="tel:5555555555">(555) 555-5555</a>
  </div>
</header>"""

new_header_html = """<header id="sticky-header">
  <div class="wrap">
    <div class="nav-left">
      <a class="wordmark" href="https://www.centerstreetlending.com/"><img src="logo1.svg" alt="Center Street Lending" style="height: 36px; width: auto; display: block;"></a>
    </div>
    <a class="phone" href="tel:5555555555">(555) 555-5555</a>
  </div>
</header>"""

html = html.replace(old_header_html, new_header_html)

# 2. Make sure the CSS has standard image rules for the header logo
# We re-enable the program-title hiding and wordmark styling, or just set standard styles.
# Let's check what styles we have currently:
#   .nav-left { display: flex; align-items: center; }
#   .program-title { 
#     display: inline-block; 
#     font-size: 1.3rem; 
#     font-weight: 700; 
#     color: var(--navy); 
#     letter-spacing: -0.019em; 
#   }
#   .program-title span {
#     color: var(--accent);
#   }

# Since we removed the .program-title element from the HTML, we can just hide it and make sure header image styles are clean:
# Let's ensure header img height and hover states are set up.
# Currently in CSS:
#   header img { height: 33px; width: auto; display: block; transition: height 0.3s ease; }
# This is perfect. Let's make sure the mobile queries still handle the logo image correctly:
# We already added the logo image overrides in revert_to_previous.py:
#   header a.wordmark img { height: 26px !important; }

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Corporate logo restored to header, program title removed!")
