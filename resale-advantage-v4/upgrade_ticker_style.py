file_path = '/Users/gregmontoya/AntiGravity Workspaces/Paul_Project_1/CSL-Resale-Advantage/resale-advantage-v3/csl-investor-exit-advantage-v3.html'
with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Replace the current .hero-right and .tk- CSS styles with an upgraded premium glassmorphism card style.
# This adds backdrop-filter (frosted glass), a cleaner border, drop shadows, and refined typography spacing.

old_styles = """  .hero-right { width: 340px; flex-shrink: 0; padding: 26px 22px; background: rgba(255, 255, 255, 0.06); border: 1px solid rgba(255,255,255,.16); border-radius: 18px; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 24px; margin-top: -130px; }
  .tk-label { display: block; font-size: .7rem; text-transform: uppercase; letter-spacing: .09em; color: rgba(255,255,255,.7); text-align: center; }
  .tk-num { display: block; font-size: 3.8rem; font-weight: 800; color: #fff; line-height: 1.05; margin: 8px 0 4px; text-align: center; font-family: 'Roboto', sans-serif; }
  .tk-sub { font-size: .84rem; color: rgba(255,255,255,.82); line-height: 1.4; text-align: center; }"""

new_styles = """  .hero-right { 
    width: 350px; 
    flex-shrink: 0; 
    padding: 40px 30px; 
    background: rgba(255, 255, 255, 0.09); 
    border: 1px solid rgba(255, 255, 255, 0.18); 
    border-radius: 24px; 
    display: flex; 
    flex-direction: column; 
    align-items: center; 
    justify-content: center; 
    gap: 16px; 
    margin-top: -130px;
    box-shadow: 0 20px 40px rgba(0, 0, 0, 0.35);
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
  }
  .tk-label { 
    display: block; 
    font-size: 0.8rem; 
    font-weight: 700;
    text-transform: uppercase; 
    letter-spacing: 0.15em; 
    color: rgba(255, 255, 255, 0.85); 
    text-align: center; 
  }
  .tk-num { 
    display: block; 
    font-size: 5rem; 
    font-weight: 800; 
    color: #fff; 
    line-height: 1.0; 
    margin: 12px 0; 
    text-align: center; 
    font-family: 'Roboto', sans-serif; 
    letter-spacing: -0.03em;
    text-shadow: 0 0 20px rgba(255, 255, 255, 0.15);
  }
  .tk-sub { 
    font-size: 0.95rem; 
    color: rgba(255, 255, 255, 0.9); 
    line-height: 1.5; 
    text-align: center;
    font-weight: 400;
  }"""

html = html.replace(old_styles, new_styles)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Ticker card upgraded with premium glassmorphism styling.")
