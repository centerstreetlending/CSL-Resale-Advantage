file_path = '/Users/gregmontoya/AntiGravity Workspaces/Paul_Project_1/CSL-Resale-Advantage/resale-advantage-v3/csl-investor-exit-advantage-v3.html'
with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Embed the HubSpot Script Loader (CSL Portal 22311313) right before </body>
old_end = "</body>\n</html>"
new_end = """<!-- Start of HubSpot Embed Code -->
<script type="text/javascript" id="hs-script-loader" async defer src="//js.hs-scripts.com/22311313.js"></script>
<!-- End of HubSpot Embed Code -->
</body>
</html>"""

html = html.replace(old_end, new_end)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("HubSpot Tracking Code & Chatbot Embed script added successfully!")
