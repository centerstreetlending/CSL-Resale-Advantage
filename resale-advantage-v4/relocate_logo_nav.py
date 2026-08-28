file_path = '/Users/gregmontoya/AntiGravity Workspaces/Paul_Project_1/CSL-Resale-Advantage/resale-advantage-v3/csl-investor-exit-advantage-v3.html'
with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update CSS styles for the header
# - Always display .program-title (no longer hidden at scroll position 0)
# - Remove wordmark styles that toggled logo/title
old_header_css = """  /* Scroll Transition States */
  .nav-left { display: flex; align-items: center; }
  .program-title { 
    display: none; 
    font-size: 1.3rem; 
    font-weight: 700; 
    color: var(--navy); 
    letter-spacing: -0.019em; 
    opacity: 0;
    transform: translateY(-5px);
    transition: opacity 0.3s ease, transform 0.3s ease;
  }
  .program-title span {
    color: var(--accent);
  }
  
  header.scrolled {
    padding: 10px 0;
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
  }
  header.scrolled a.wordmark img {
    opacity: 0;
    display: none;
  }
  header.scrolled .program-title {
    display: inline-block;
    opacity: 1;
    transform: translateY(0);
    animation: navFadeIn 0.3s forwards;
  }
  
  @keyframes navFadeIn {
    from { opacity: 0; transform: translateY(-5px); }
    to { opacity: 1; transform: translateY(0); }
  }"""

new_header_css = """  .nav-left { display: flex; align-items: center; }
  .program-title { 
    display: inline-block; 
    font-size: 1.3rem; 
    font-weight: 700; 
    color: var(--navy); 
    letter-spacing: -0.019em; 
  }
  .program-title span {
    color: var(--accent);
  }
  
  header.scrolled {
    padding: 10px 0;
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
  }"""

html = html.replace(old_header_css, new_header_css)

# Also update mobile stylesheet queries for header logo image and wordmark which are now gone:
html = html.replace("header a.wordmark img { height: 26px !important; }", "")
html = html.replace("header a.wordmark img { height: 22px !important; }", "")

# 2. Update Header HTML: Remove the logo image from the header, leave only .program-title
old_header_html = """<header id="sticky-header">
  <div class="wrap">
    <div class="nav-left">
      <a class="wordmark" href="https://www.centerstreetlending.com/"><img src="logo1.svg" alt="Center Street Lending" style="height: 36px; width: auto; display: block;"></a>
      <span class="program-title">CSL Resale Advantage <span>Program</span></span>
    </div>
    <a class="phone" href="tel:5555555555">(555) 555-5555</a>
  </div>
</header>"""

new_header_html = """<header id="sticky-header">
  <div class="wrap">
    <div class="nav-left">
      <span class="program-title">CSL Resale Advantage <span>Program</span></span>
    </div>
    <a class="phone" href="tel:5555555555">(555) 555-5555</a>
  </div>
</header>"""

html = html.replace(old_header_html, new_header_html)

# 3. Update Hero HTML: Add CSL corporate logo (logo1.svg) inside hero-left-top above the eyebrow
old_hero_top = """    <div class="hero-left">
      <div class="hero-left-top">
        <div class="hero-eyebrow">CSL Resale Advantage Program</div>"""

new_hero_top = """    <div class="hero-left">
      <div class="hero-left-top">
        <img src="logo1.svg" alt="Center Street Lending" style="height: 36px; width: auto; display: block; margin-bottom: 8px;">
        <div class="hero-eyebrow">CSL Resale Advantage Program</div>"""

html = html.replace(old_hero_top, new_hero_top)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Corporate logo moved to hero, header set to show program name permanently.")
