file_path = '/Users/gregmontoya/AntiGravity Workspaces/Paul_Project_1/CSL-Resale-Advantage/resale-advantage-v3/csl-investor-exit-advantage-v3.html'
with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Replace the plain logo image in the hero-left-top with a flex row containing the logo and "| Borrower Offer" text
old_top_markup = """      <div class="hero-left-top">
        <img src="logo1.svg" alt="Center Street Lending" style="height: 36px; width: auto; display: block; margin-bottom: 24px;">"""

# We style the flex row to vertically center align the logo image and the thin tag text, matching the screenshot style.
new_top_markup = """      <div class="hero-left-top">
        <div class="hero-brand-row" style="display: flex; align-items: center; gap: 14px; margin-bottom: 24px;">
          <img src="logo1.svg" alt="Center Street Lending" style="height: 32px; width: auto; display: block;">
          <span style="color: rgba(255, 255, 255, 0.8); font-size: 1.15rem; font-weight: 300; font-family: 'Roboto', sans-serif; letter-spacing: 0.02em;">| &nbsp; Borrower Offer</span>
        </div>"""

html = html.replace(old_top_markup, new_top_markup)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("CSL Logo and '| Borrower Offer' badge added above headline successfully!")
