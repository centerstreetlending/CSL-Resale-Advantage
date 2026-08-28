file_path = '/Users/gregmontoya/AntiGravity Workspaces/Paul_Project_1/CSL-Resale-Advantage/resale-advantage-v3/csl-investor-exit-advantage-v3.html'
with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Replace the header HTML
old_header = """<header>
  <div class="wrap">
    <a class="wordmark" href="https://www.centerstreetlending.com/">CENTER STREET <span>LENDING</span></a>
    <a class="phone" href="tel:5555555555">Call <span style="text-decoration:underline;">(555) 555-5555</span></a>
  </div>
</header>"""

new_header = """<header>
  <div class="wrap">
    <a class="wordmark" href="https://www.centerstreetlending.com/"><img src="logo1.svg" alt="Center Street Lending" style="height: 36px; width: auto; display: block;"></a>
    <a class="phone" href="tel:949-676-5617">Call 949-676-5617</a>
  </div>
</header>"""

html = html.replace(old_header, new_header)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Header replaced successfully!")
