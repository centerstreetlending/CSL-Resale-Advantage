import re

file_path = '/Users/gregmontoya/AntiGravity Workspaces/Paul_Project_1/CSL-Resale-Advantage/resale-advantage-v3/csl-investor-exit-advantage-v3.html'
with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Add Inter font to the Google Fonts link
html = html.replace('Oswald:wght@700&display=swap', 'Oswald:wght@700&family=Inter:wght@400;700&display=swap')

# Add font-face for Arteria Std Compress if they don't have it (fallback logic)
arteria_css = """
  @font-face {
    font-family: 'Arteria Std Compress';
    src: local('Arteria Std Compress');
    font-display: swap;
  }
"""
html = html.replace('<style>', '<style>' + arteria_css)

# CSS replacements
# H1 and stat num font
html = html.replace("font-family: 'Oswald', sans-serif;", "font-family: 'Arteria Std Compress', 'Oswald', sans-serif;")
# Header phone
html = html.replace('Call <span>(949) 244-1090</span>', 'Call <span style="text-decoration:underline;">(555) 555-5555</span>')
html = html.replace('href="tel:949-244-1090"', 'href="tel:5555555555"')

# Add eyebrow CSS
eyebrow_css = """
  .section-eyebrow { color: var(--accent, #4683B3); font-size: 16px; font-weight: 700; text-transform: uppercase; line-height: 20px; letter-spacing: 2.40px; margin-bottom: 12px; }
  .section-title { color: var(--navy-darkest, #2C3842); font-size: 32px; font-weight: 700; line-height: 40px; margin-bottom: 12px; }
  .section-sub { color: #5D6871; font-size: 20px; font-weight: 400; line-height: 25px; margin-bottom: 32px; max-width: 800px; }
  .card h3, .benefit h3 { font-size: 24px; font-weight: 700; line-height: 27.6px; margin-bottom: 12px; color: var(--navy-darkest, #2C3842); }
  .card p, .benefit p { font-size: 20px; font-weight: 400; line-height: 25px; color: #5D6871; }
  #compare table.cmp { font-family: 'Inter', sans-serif; font-size: 18px; }
  #compare .cmp td.csl { background: var(--accent); color: #fff; }
  #compare .cmp thead th.csl { background: var(--accent); color: #fff; }
  
  .dark-stats { background: #2C3842; color: white; padding: 60px 0; }
  .dark-stats .wrap { display: flex; justify-content: space-around; flex-wrap: wrap; gap: 40px; text-align: center; }
  .dark-stats .stat-num { font-size: 42px; font-family: 'Roboto', sans-serif; font-weight: 700; line-height: 63px; }
  .dark-stats .stat-label { font-size: 18px; font-family: 'Roboto', sans-serif; font-weight: 500; line-height: 27px; max-width: 200px; margin: 0 auto; }
  
  .trusted-network { background: var(--accent); color: white; padding: 80px 0; text-align: center; }
  .trusted-network h2 { color: white; font-size: 32px; margin-bottom: 24px; line-height: 40px; }
  .trusted-network p { font-size: 20px; line-height: 25px; margin-bottom: 16px; max-width: 800px; margin-left: auto; margin-right: auto; }
"""
html = html.replace('/* hero */', eyebrow_css + '\n  /* hero */')

# Section 1 HTML replacement (Who this is for)
sec1_old = """<h2>Who this is for</h2>
    <p class="sub">Resale Advantage is built for CSL borrowers thinking about the sale side of their project.</p>"""
sec1_new = """<div class="section-eyebrow">who is the CSL REsale advantage Program for?</div>
    <h2 class="section-title">Does this sound like you?</h2>
    <p class="section-sub">Resale Advantage is built for CSL borrowers nearing their exit, and thinking about the sale side of their project.</p>"""
html = html.replace(sec1_old, sec1_new)

# Card text replacements
html = html.replace('Approaching resale or maturity', 'Approaching Resale or Maturity')
html = html.replace('Repeat borrowers', 'Repeat Borrower')

# Section 2 HTML replacement (Benefits)
sec2_old = """<h2>What you can request through the program</h2>
    <p class="sub">Eligible CSL borrowers can ask for information about any of the following. Everything is optional &mdash; pick what's useful to you.</p>"""
sec2_new = """<div class="section-eyebrow">Key advantages of the CSL resale advantage</div>
    <h2 class="section-title">What you can request through the program</h2>
    <p class="section-sub">Eligible CSL borrowers can ask for information about any of the following. Everything is optional &mdash; pick what's useful to you.</p>"""
html = html.replace(sec2_old, sec2_new)

# Section 3 HTML replacement (Comparison)
sec3_old = """<h2>What changes when you use the program</h2>
    <p class="sub">Same project, different exit. Here's how a coordinated path compares with handling the sale on your own.</p>"""
sec3_new = """<div class="section-eyebrow">Key advantages of the CSL resale advantage</div>
    <h2 class="section-title">What changes when you use the program</h2>
    <p class="section-sub">Same project, different exit. Here's how a coordinated path compares with handling the sale on your own.</p>"""
html = html.replace(sec3_old, sec3_new)

# Add Dark Stats & Trusted Network BEFORE InnoLaunch
dark_stats_html = """
<!-- DARK STATS -->
<section class="dark-stats">
  <div class="wrap">
    <div>
      <div class="stat-num">$7.6B+</div>
      <div class="stat-label">Funded by Center Street Lending</div>
    </div>
    <div>
      <div class="stat-num">3,200+</div>
      <div class="stat-label">Homes sold by Innovate Realty</div>
    </div>
    <div>
      <div class="stat-num">$1.1B+</div>
      <div class="stat-label">Closed by Honest Escrow</div>
    </div>
  </div>
</section>

<!-- TRUSTED NETWORK -->
<section class="trusted-network">
  <div class="wrap">
    <div class="section-eyebrow" style="color: white;">A TRUSTED network of PROFESSIONALS</div>
    <h2>You Created the Value. Keep More of It.</h2>
    <p>The goal is simple. Buy, renovate, or build. Increase value. Sell. Repeat.</p>
    <p>You worked hard to create equity. When it's time to sell, more of that value should stay in your pocket.</p>
    <p>CSL Resale Advantage gives Center Street Lending borrowers access to preferred pricing and trusted real estate and escrow professionals who already know the CSL process, <strong style="font-weight:700;">making the final stage of your project simpler, more coordinated, and more cost-effective.</strong></p>
  </div>
</section>
"""
html = html.replace('<!-- INNOLAUNCH SHOWCASE -->', dark_stats_html + '\n<!-- INNOLAUNCH SHOWCASE -->')

# InnoLaunch Section
inno_old = """<h2>What an InnoLaunch debut looks like</h2>
    <p class="sub">Sample marketing materials prepared for an Innovate Realty listing &mdash; the kind of launch support included when you list with an Innovate Realty agent.</p>
    <ul class="inno-points">
      <li><strong>20,000 buyer views in 21 days</strong> &mdash; a coordinated launch built to get eyes on your property fast</li>
      <li>Email marketing &amp; targeted digital ads</li>
      <li>A dedicated property website</li>
      <li>Printed brochures, flyers &amp; postcards</li>
      <li>Marketing can begin before construction is complete &mdash; for a head start</li>
    </ul>"""
inno_new = """<div class="section-eyebrow">Marketing and sales expertise</div>
    <h2 class="section-title">What an InnoLaunch debut looks like</h2>
    <p class="section-sub">Sample marketing materials prepared for an Innovate Realty listing &mdash; the kind of launch support included when you list with an Innovate Realty agent.</p>
    <ul class="inno-points" style="font-family: 'Inter', sans-serif; font-size: 18px; margin-bottom: 24px;">
      <li><strong>20,000 buyer views in 21 days</strong> &mdash; a coordinated launch built to get eyes on your property fast</li>
      <li>Email marketing &amp; targeted digital ads</li>
      <li>A dedicated property website</li>
      <li>Printed brochures, flyers &amp; postcards</li>
      <li>Get a head start with marketing before construction is complete</li>
    </ul>"""
html = html.replace(inno_old, inno_new)

# Honest Escrow Section
honest_old = """<span class="he-eyebrow">Your escrow option</span>
        <h2>Meet Honest Escrow.</h2>
        <p class="he-sub">An independent Southern California escrow team that keeps the closing process clear, calm, and human &mdash; and is familiar with CSL payoff and closing requirements.</p>
        <ul class="he-points">
          <li>Escrow officers with more than 15 years of experience</li>
          <li>Clear communication at every milestone, from opening to closing</li>
          <li>Familiar with CSL payoff demands and closing coordination</li>
          <li>Optional &mdash; you are always free to choose your own escrow company</li>
        </ul>"""
honest_new = """<span class="he-eyebrow" style="background:transparent; color: var(--accent); padding:0; letter-spacing:2.4px; margin-bottom:12px;">your escrow option</span>
        <h2 style="font-family: 'Roboto', sans-serif; font-size: 32px;">Meet Honest Escrow.</h2>
        <p class="he-sub" style="font-size: 20px; line-height: 25px;">An independent Southern California escrow team that keeps the closing process clear, calm, and human &mdash; and is familiar with CSL payoff and closing requirements.</p>
        <ul class="he-points" style="font-family: 'Inter', sans-serif; font-size: 18px; gap: 16px;">
          <li>Escrow officers with more than 15 years of experience</li>
          <li>Clear communication at every milestone, from opening to closing</li>
          <li>Familiar with CSL payoff demands and closing coordination</li>
          <li>Optional &mdash; you are always free to choose your own escrow company</li>
        </ul>"""
html = html.replace(honest_old, honest_new)

# Optin Section
optin_old = """<h2>Request information</h2>
    <p class="sub">No obligation. Use of any introduced provider is optional &mdash; you always choose your own providers.</p>"""
optin_new = """<div class="section-eyebrow" style="color:var(--accent);">request information</div>
    <h2 style="font-family: 'Arteria Std Compress', 'Oswald', sans-serif; font-size: 101px; line-height: 90.9px; text-transform: uppercase;">ready to maximize<br>your exit?</h2>
    <p class="section-sub" style="color: white;">Submit your project details today. A CSL program advisor will review your request, calculate your estimated commission and escrow discounts, and connect you with our preferred partners.</p>
    <div style="margin-bottom: 24px;">
      <strong style="font-size: 20px;">Questions?</strong><br>
      <span style="font-size: 20px;">Call us directly at <a href="tel:5555555555" style="color:white;">(555) 555-5555</a></span>
    </div>"""
html = html.replace(optin_old, optin_new)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Done")
