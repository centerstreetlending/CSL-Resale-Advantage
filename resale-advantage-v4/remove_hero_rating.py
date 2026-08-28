file_path = '/Users/gregmontoya/AntiGravity Workspaces/Paul_Project_1/CSL-Resale-Advantage/resale-advantage-v3/csl-investor-exit-advantage-v3.html'
with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Remove the hero-rating-row element completely
old_rating_row = """      <div class="hero-rating-row">
        <span class="rating-label">Excellent</span>
        <span class="rating-stars">★★★★★</span>
        <span class="rating-text">based on 100+ CSL borrower exits</span>
      </div>"""

html = html.replace(old_rating_row + "\n", "")
html = html.replace(old_rating_row, "")

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Hero rating row removed successfully!")
