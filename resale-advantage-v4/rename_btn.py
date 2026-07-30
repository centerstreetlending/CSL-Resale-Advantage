filepath = "csl-investor-exit-advantage-v4.html"
with open(filepath, "r") as f:
    content = f.read()

# Replace class occurrences in HTML
content = content.replace('class="btn"', 'class="csl-btn"')
content = content.replace('class="btn-ghost"', 'class="csl-btn-ghost"')

# Replace occurrences in CSS
content = content.replace('.btn{', '.csl-btn{')
content = content.replace('.btn:hover', '.csl-btn:hover')
content = content.replace('.btn-ghost', '.csl-btn-ghost')
content = content.replace('.btn:active', '.csl-btn:active')
content = content.replace('.btn {', '.csl-btn {')
content = content.replace('a.btn', 'a.csl-btn')

with open(filepath, "w") as f:
    f.write(content)

print("Renamed buttons successfully!")
