file_path = '/Users/gregmontoya/AntiGravity Workspaces/Paul_Project_1/CSL-Resale-Advantage/resale-advantage-v3/csl-investor-exit-advantage-v3.html'
with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Replace all Inter and Arteria/Oswald with Roboto
html = html.replace("font-family: 'Arteria Std Compress', 'Oswald', sans-serif;", "font-family: 'Roboto', sans-serif;")
html = html.replace("font-family: 'Inter', sans-serif;", "font-family: 'Roboto', sans-serif;")

# Remove the Arteria @font-face block
arteria_css = """  @font-face {
    font-family: 'Arteria Std Compress';
    src: local('Arteria Std Compress');
    font-display: swap;
  }"""
html = html.replace(arteria_css, "")

# Clean up google fonts link
html = html.replace('Oswald:wght@700&family=Inter:wght@400;700&display=swap', 'display=swap')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Roboto applied everywhere.")
