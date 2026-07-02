file_path = '/Users/gregmontoya/AntiGravity Workspaces/Paul_Project_1/CSL-Resale-Advantage/resale-advantage-v3/csl-investor-exit-advantage-v3.html'
with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Match the correct margin-bottom: 12px that is currently in the file and inject the Borrower Offer badge
old_top_markup = """      <div class="hero-left-top">
        <img src="logo1.svg" alt="Center Street Lending" style="height: 36px; width: auto; display: block; margin-bottom: 12px;">"""

new_top_markup = """      <div class="hero-left-top">
        <div class="hero-brand-row" style="display: flex; align-items: center; gap: 14px; margin-bottom: 24px;">
          <img src="logo1.svg" alt="Center Street Lending" style="height: 32px; width: auto; display: block;">
          <span style="color: rgba(255, 255, 255, 0.8); font-size: 1.15rem; font-weight: 300; font-family: 'Roboto', sans-serif; letter-spacing: 0.02em;">| &nbsp; Borrower Offer</span>
        </div>"""

if old_top_markup in html:
    html = html.replace(old_top_markup, new_top_markup)
    print("Success: Borrower Offer badge applied correctly!")
else:
    print("Error: Could not match the markup.")

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(html)
