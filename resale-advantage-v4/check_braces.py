with open('csl-investor-exit-advantage-v3.html', 'r') as f:
    html = f.read()

start = html.find('<style>')
end = html.find('</style>')
if start != -1 and end != -1:
    css = html[start:end]
    stack = []
    for i, c in enumerate(css):
        if c == '{':
            stack.append(i)
        elif c == '}':
            if not stack:
                print(f"Extra closing brace at {i}")
            else:
                stack.pop()
    if stack:
        print(f"Unclosed braces at {stack}")
    else:
        print("Braces are balanced in CSS")
