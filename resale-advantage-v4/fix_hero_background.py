file_path = '/Users/gregmontoya/AntiGravity Workspaces/Paul_Project_1/CSL-Resale-Advantage/resale-advantage-v3/csl-investor-exit-advantage-v3.html'
with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Current CSS background property:
# .hero { background: linear-gradient(180deg, rgba(0,0,0,0.90) 0%, rgba(0,0,0,0) 100%), rgba(0,0,0,0.50) url('Frame 129.png') no-repeat center center; background-size: cover; background-blend-mode: multiply, normal, normal; padding: 72px 0 60px; display: flex; flex-direction: column; align-items: center; gap: 64px; animation: none; color: #fff; }

# We will replace the dark black multiply overlay with a rich, inviting navy brand gradient (using #2C3842 / RGB 44, 56, 66) at a much lighter opacity.

old_bg = "background: linear-gradient(180deg, rgba(0,0,0,0.90) 0%, rgba(0,0,0,0) 100%), rgba(0,0,0,0.50) url('Frame 129.png') no-repeat center center; background-size: cover; background-blend-mode: multiply, normal, normal;"
new_bg = "background: linear-gradient(180deg, rgba(44, 56, 66, 0.75) 0%, rgba(44, 56, 66, 0.35) 100%), url('Frame 129.png') no-repeat center center; background-size: cover;"

html = html.replace(old_bg, new_bg)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Hero background overlay updated to be lighter and more inviting.")
