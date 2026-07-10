file_path = '/Users/gregmontoya/AntiGravity Workspaces/Paul_Project_1/CSL-Resale-Advantage/resale-advantage-v3/csl-investor-exit-advantage-v3.html'
with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Replace the hero-cta button CSS to make it capitalized, add a premium brand glow shadow,
# and implement a tactile hover animation.

old_btn_styles = """  .hero-cta .btn { font-size: 1rem; font-weight: 600; padding: 14px 32px; border-radius: 6px; display: inline-flex; align-items: center; gap: 12px; }"""

new_btn_styles = """  .hero-cta .btn { 
    font-size: 1rem; 
    font-weight: 700; 
    padding: 16px 36px; 
    border-radius: 8px; 
    display: inline-flex; 
    align-items: center; 
    gap: 12px; 
    text-transform: uppercase; 
    letter-spacing: 0.08em;
    box-shadow: 0 6px 20px rgba(70, 131, 179, 0.4);
    transition: transform 0.2s ease, box-shadow 0.2s ease, background-color 0.2s ease;
  }
  .hero-cta .btn:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 24px rgba(70, 131, 179, 0.55);
    background-color: var(--accent-dark);
  }
  .hero-cta .btn:active {
    transform: translateY(0);
    box-shadow: 0 4px 12px rgba(70, 131, 179, 0.4);
  }"""

html = html.replace(old_btn_styles, new_btn_styles)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("CTA button updated to stand out with uppercase letters and hover animations!")
