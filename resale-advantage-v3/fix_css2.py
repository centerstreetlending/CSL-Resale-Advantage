with open('csl-investor-exit-advantage-v3.html', 'r') as f:
    text = f.read()

text = text.replace('header a.phone{color:var(--navy);font-weight:600;text-decoration:none;font-size:var(--text-body)}}', 'header a.phone{color:var(--navy);font-weight:600;text-decoration:none;font-size:var(--text-body)}')

with open('csl-investor-exit-advantage-v3.html', 'w') as f:
    f.write(text)
