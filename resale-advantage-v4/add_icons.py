import re

with open('csl-investor-exit-advantage-v3.html', 'r') as f:
    html = f.read()

# 1. Update the disclaimer text
old_disclaimer = """<div style="margin-top: 24px; text-align: center;">
      <p class="pending-inline">*Pending escrow-law / legal review: an advertised escrow fee reduction must be disclosed in writing and reflected in the escrow instructions.</p>
    </div>"""
new_disclaimer = """<div style="margin-top: 16px; text-align: left; max-width: 600px;">
      <p style="font-size: var(--text-micro); color: var(--accent); font-weight: 500;">*Pending escrow-law / legal review: an advertised escrow fee reduction must be disclosed in writing and reflected in the escrow instructions.</p>
    </div>"""
html = html.replace(old_disclaimer, new_disclaimer)

# 2. Add icons to the benefits
icons = [
    # 1. 1% listing fee (Tag)
    """<svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="var(--accent)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="margin-bottom:16px;"><path d="M20.59 13.41l-7.17 7.17a2 2 0 0 1-2.83 0L2 12V2h10l8.59 8.59a2 2 0 0 1 0 2.82z"></path><line x1="7" y1="7" x2="7.01" y2="7"></line></svg>""",
    # 2. Marketing (Megaphone)
    """<svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="var(--accent)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="margin-bottom:16px;"><polygon points="11 19 2 12 11 5 11 19"></polygon><path d="M22 12A10 10 0 0 0 11 2v20a10 10 0 0 0 11-10z"></path></svg>""",
    # 3. Network (Map pin / Users)
    """<svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="var(--accent)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="margin-bottom:16px;"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path><circle cx="9" cy="7" r="4"></circle><path d="M23 21v-2a4 4 0 0 0-3-3.87"></path><path d="M16 3.13a4 4 0 0 1 0 7.75"></path></svg>""",
    # 4. Escrow option (Shield Check)
    """<svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="var(--accent)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="margin-bottom:16px;"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path><polyline points="9 12 11 14 15 10"></polyline></svg>""",
    # 5. Planning (Calendar)
    """<svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="var(--accent)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="margin-bottom:16px;"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect><line x1="16" y1="2" x2="16" y2="6"></line><line x1="8" y1="2" x2="8" y2="6"></line><line x1="3" y1="10" x2="21" y2="10"></line></svg>""",
    # 6. Coordinated Process (Activity / Sync)
    """<svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="var(--accent)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="margin-bottom:16px;"><polyline points="22 12 18 12 15 21 9 3 6 12 2 12"></polyline></svg>"""
]

# We'll find all `<div class="benefit">` and insert the icon right after it.
# Wait, let's just do it with split.
parts = html.split('<div class="benefit">')

if len(parts) == 7: # 1 before the first, plus 6 benefits
    new_html = parts[0]
    for i in range(1, 7):
        new_html += '<div class="benefit">\n        ' + icons[i-1] + parts[i]
    
    with open('csl-investor-exit-advantage-v3.html', 'w') as f:
        f.write(new_html)
    print("Success")
else:
    print(f"Failed. Found {len(parts)-1} benefits.")
