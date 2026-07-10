file_path = '/Users/gregmontoya/AntiGravity Workspaces/Paul_Project_1/CSL-Resale-Advantage/resale-advantage-v3/csl-investor-exit-advantage-v3.html'
with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Revert the .hero-subheading CSS to its clean original state:
# - Remove the border-left and padding (the "blue line")
# - Set size back to 1.4rem (original size)
# - Set weight back to 700
# - Remove display: inline-block and align-self: flex-start so it behaves as a normal header block
old_subheading_css = """  .hero-subheading {
    display: inline-block;
    align-self: flex-start;
    border-left: 5px solid var(--accent);
    color: #fff;
    font-size: 1.35rem;
    font-weight: 700;
    letter-spacing: -0.01em;
    padding: 2px 0 2px 16px;
    margin: 28px 0 20px 0;
    font-family: 'Roboto', sans-serif;
    line-height: 1.0;
  }"""

new_subheading_css = """  .hero-subheading {
    font-size: 1.4rem;
    font-weight: 700;
    color: #fff;
    margin: 24px 0 10px;
    font-family: 'Roboto', sans-serif;
    letter-spacing: -0.01em;
  }"""

html = html.replace(old_subheading_css, new_subheading_css)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Subheading 'blue line' removed and font-size reverted back to 1.4rem successfully!")
