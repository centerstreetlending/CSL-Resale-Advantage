file_path = '/Users/gregmontoya/AntiGravity Workspaces/Paul_Project_1/CSL-Resale-Advantage/resale-advantage-v3/csl-investor-exit-advantage-v3.html'
with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update the CSS for .hero-subheading to include the vertical blue accent line styling,
# matching the eyebrow styling but adjusted for the subheading position.
old_subheading_css = """  .hero-subheading {
    font-size: 1.4rem;
    font-weight: 700;
    color: #fff;
    margin: 24px 0 10px;
    font-family: 'Roboto', sans-serif;
    letter-spacing: -0.01em;
  }"""

new_subheading_css = """  .hero-subheading {
    display: inline-block;
    align-self: flex-start;
    border-left: 5px solid var(--accent);
    color: #fff;
    font-size: 1.25rem;
    font-weight: 800;
    text-transform: uppercase;
    letter-spacing: 0.15em;
    padding: 2px 0 2px 16px;
    margin: 28px 0 20px 0;
    font-family: 'Roboto', sans-serif;
    line-height: 1.0;
  }
  .hero-subheading span {
    color: var(--accent);
  }"""

html = html.replace(old_subheading_css, new_subheading_css)

# Remove the old unused .hero-eyebrow styles since it's going away
html = html.replace(
    """  .hero-eyebrow { 
    display: inline-block; 
    align-self: flex-start; 
    border-left: 5px solid var(--accent); 
    color: #fff; 
    font-size: 1.05rem; 
    font-weight: 800; 
    text-transform: uppercase; 
    letter-spacing: 0.15em; 
    padding: 2px 0 2px 16px; 
    margin-bottom: 20px; 
    background: none;
  }
  .hero-eyebrow span {
    color: var(--accent);
  }""",
    ""
)

# 2. Update HTML of hero-left:
# - Remove the top .hero-eyebrow block (so H1 is at the very top of hero content)
# - Replace .hero-subheading with capitalized "CSL RESALE ADVANTAGE <span>PROGRAM</span>"
old_hero_left = """    <div class="hero-left">
      <div class="hero-left-top">
        <div class="hero-eyebrow">CSL RESALE ADVANTAGE <span>PROGRAM</span></div>
        <h1><span style="display: inline-block; white-space: nowrap;">WE MADE IT <span class="hl">EASIER & CHEAPER</span></span><br><span style="display: inline-block; white-space: nowrap;">TO EXIT YOUR INVESTMENT.</span></h1>
        
        <h2 class="hero-subheading">The CSL Resale Advantage</h2>"""

new_hero_left = """    <div class="hero-left">
      <div class="hero-left-top">
        <h1><span style="display: inline-block; white-space: nowrap;">WE MADE IT <span class="hl">EASIER & CHEAPER</span></span><br><span style="display: inline-block; white-space: nowrap;">TO EXIT YOUR INVESTMENT.</span></h1>
        
        <h2 class="hero-subheading">CSL RESALE ADVANTAGE <span>PROGRAM</span></h2>"""

html = html.replace(old_hero_left, new_hero_left)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Eyebrow moved to subheading position and styled with vertical blue accent line!")
