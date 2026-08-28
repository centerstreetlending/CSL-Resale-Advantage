import re
with open('csl-investor-exit-advantage-v3.html', 'r') as f:
    text = f.read()

# I messed up header a.phone by removing the brace
text = text.replace('header a.phone{color:var(--navy);font-weight:600;text-decoration:none;font-size:var(--text-body)', 'header a.phone{color:var(--navy);font-weight:600;text-decoration:none;font-size:var(--text-body)}')

# I also messed up .hero h1 matching across lines
broken_block = """.hero h1{font-size:var(--text-h1); 
    color: #fff; 
    text-align: center; 
    padding: 12px 16px; 
    font-size: 0.92rem; 
    letter-spacing: 0.06em; 
    font-family: 'Roboto', sans-serif; 
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 8px;
    border-bottom: 1px solid rgba(255, 255, 255, 0.03);
    margin: 0;
    cursor: pointer;
    transition: background 0.3s ease, border-color 0.3s ease;
  }"""

fixed_block = """}
  .offer-bar {
    background: var(--navy-deep);
    color: #fff; 
    text-align: center; 
    padding: 12px 16px; 
    font-size: var(--text-body); 
    letter-spacing: 0.06em; 
    font-family: 'Roboto', sans-serif; 
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 8px;
    border-bottom: 1px solid rgba(255, 255, 255, 0.03);
    margin: 0;
    cursor: pointer;
    transition: background 0.3s ease, border-color 0.3s ease;
  }"""

if broken_block in text:
    text = text.replace(broken_block, fixed_block)
    print("Fixed offer-bar block")

with open('csl-investor-exit-advantage-v3.html', 'w') as f:
    f.write(text)
