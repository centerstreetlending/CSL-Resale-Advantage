file_path = '/Users/gregmontoya/AntiGravity Workspaces/Paul_Project_1/CSL-Resale-Advantage/resale-advantage-v3/csl-investor-exit-advantage-v3.html'
with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update header styles to make it sticky, add scroll transitions, and set up the .program-title typography
old_header_css = """  header { background: #fff; padding: 16px 0; height: 72px; border: none; }
  header .wrap { max-width: 1080px; display: flex; align-items: center; justify-content: space-between; margin: 0 auto; padding: 0 24px; }
  header a.phone { color: var(--navy); font-size: .95rem; font-weight: 600; text-decoration: none; }
  header a.phone:hover { text-decoration: underline; }
  header img { height: 33px; width: auto; display: block; }"""

new_header_css = """  header { 
    background: #fff; 
    padding: 16px 0; 
    border-bottom: 1px solid var(--line); 
    position: sticky;
    top: 0;
    z-index: 1000;
    transition: padding 0.3s ease, box-shadow 0.3s ease, background-color 0.3s ease;
  }
  header .wrap { max-width: 1080px; display: flex; align-items: center; justify-content: space-between; margin: 0 auto; padding: 0 24px; }
  header a.phone { color: var(--navy); font-size: .95rem; font-weight: 700; text-decoration: none; transition: font-size 0.3s ease; }
  header a.phone:hover { text-decoration: underline; }
  header img { height: 33px; width: auto; display: block; transition: height 0.3s ease; }
  
  /* Scroll Transition States */
  .nav-left { display: flex; align-items: center; }
  .program-title { 
    display: none; 
    font-size: 1.15rem; 
    font-weight: 700; 
    color: var(--navy); 
    letter-spacing: -0.01em; 
    opacity: 0;
    transform: translateY(-5px);
    transition: opacity 0.3s ease, transform 0.3s ease;
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

html = html.replace(old_header_css, new_header_css)

# Update the mobile responsive query to override sticky states or keep them clean:
html = html.replace(
    "header { padding: 12px 0; height: auto !important; }",
    "header { padding: 12px 0; height: auto !important; position: sticky; top: 0; }"
)

# 2. Update the HTML inside <header> to wrap the logo and include the new program title span
old_header_html = """<header>
  <div class="wrap">
    <a class="wordmark" href="https://www.centerstreetlending.com/"><img src="logo1.svg" alt="Center Street Lending" style="height: 36px; width: auto; display: block;"></a>
    <a class="phone" href="tel:5555555555">(555) 555-5555</a>
  </div>
</header>"""

new_header_html = """<header id="sticky-header">
  <div class="wrap">
    <div class="nav-left">
      <a class="wordmark" href="https://www.centerstreetlending.com/"><img src="logo1.svg" alt="Center Street Lending" style="height: 36px; width: auto; display: block;"></a>
      <span class="program-title">CSL Resale Advantage Program</span>
    </div>
    <a class="phone" href="tel:5555555555">(555) 555-5555</a>
  </div>
</header>"""

html = html.replace(old_header_html, new_header_html)

# 3. Inject the Scroll Event Listener script before the closing </body> tag
scroll_script = """  // --- Sticky Header Scroll Transition ---
  window.addEventListener('scroll', function() {
    var header = document.getElementById('sticky-header');
    if (header) {
      if (window.scrollY > 120) {
        header.classList.add('scrolled');
      } else {
        header.classList.remove('scrolled');
      }
    }
  });"""

# Inject before document.getElementById('deal-ticker') script or near end of scripts
html = html.replace(
    "  // --- Form submit ---",
    scroll_script + "\n\n  // --- Form submit ---"
)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Sticky transitioning nav header successfully implemented!")
