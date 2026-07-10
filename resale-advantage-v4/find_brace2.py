with open('csl-investor-exit-advantage-v3.html', 'r') as f:
    html = f.read()

start = html.find('<style>')
css = html[start:start+17474+50]

lines = css.split('\n')
for i, line in enumerate(lines[-5:]):
    print(f"Line: {line}")
