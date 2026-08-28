file_path = '/Users/gregmontoya/AntiGravity Workspaces/Paul_Project_1/CSL-Resale-Advantage/resale-advantage-v3/csl-investor-exit-advantage-v3.html'
with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update the HTML inside the hero-right container with the new Option 1 copy
old_ticker = """    <div class="hero-right">
      <span class="tk-label">Borrowers using the program</span>
      <span class="tk-num" id="deal-ticker" data-target="100">0</span>
      <span class="tk-sub">homes sold through CSL Resale Advantage</span>
    </div>"""

new_ticker = """    <div class="hero-right">
      <span class="tk-label">Properties Sold</span>
      <span class="tk-num" id="deal-ticker" data-target="100">0+</span>
      <span class="tk-sub">Homes successfully closed through CSL Resale Advantage</span>
    </div>"""

html = html.replace(old_ticker, new_ticker)

# 2. Update the Javascript at the bottom to append "+" to the animated numbers so it renders as "100+"
old_js_line1 = "if(window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches){ el.textContent=target; return; }"
new_js_line1 = "if(window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches){ el.textContent=target + '+'; return; }"

old_js_line2 = "el.textContent=Math.round(target*e);"
new_js_line2 = "el.textContent=Math.round(target*e) + '+';"

old_js_line3 = "el.textContent='0';"
new_js_line3 = "el.textContent='0+';"

html = html.replace(old_js_line1, new_js_line1)
html = html.replace(old_js_line2, new_js_line2)
html = html.replace(old_js_line3, new_js_line3)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Ticker copy and Javascript animation updated to Option 1 (100+ Properties Sold)!")
