file_path = '/Users/gregmontoya/AntiGravity Workspaces/Paul_Project_1/CSL-Resale-Advantage/resale-advantage-v3/csl-investor-exit-advantage-v3.html'
with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Replace the top-down gradient with a left-to-right (90deg) gradient that is darker on the left (under the text)
# and fades to a very light, inviting overlay on the right (under the stats card).
old_bg = "background: linear-gradient(180deg, rgba(44, 56, 66, 0.85) 0%, rgba(44, 56, 66, 0.50) 100%), url('Frame 129.png') no-repeat center center; background-size: cover;"
new_bg = "background: linear-gradient(90deg, rgba(0, 0, 0, 0.85) 0%, rgba(0, 0, 0, 0.15) 100%), url('Frame 129.png') no-repeat center center; background-size: cover;"

html = html.replace(old_bg, new_bg)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Hero background changed to match the mockup (left-to-right gradient overlay).")
