import re

with open('csl-investor-exit-advantage-v3.html', 'r') as f:
    text = f.read()

# Make specific replacements
replacements = [
    (r'\.debut-feature figcaption\{margin-top:10px;font-size:\.84rem;', r'.debut-feature figcaption{margin-top:10px;font-size:var(--text-small);'),
    (r'\.slide figcaption\{margin-top:10px;font-size:\.82rem;', r'.slide figcaption{margin-top:10px;font-size:var(--text-small);'),
    (r'\.gallery-note\{font-size:\.78rem;', r'.gallery-note{font-size:var(--text-micro);'),
    (r'\.he-stars span\{display:inline-block;color:#F2BD63;font-size:1\.3rem;', r'.he-stars span{display:inline-block;color:#F2BD63;font-size:var(--text-h4);'),
    (r'\.he-quote \.q-stars\{color:#F2BD63;font-size:1\.1rem;', r'.he-quote .q-stars{color:#F2BD63;font-size:var(--text-lead);'),
    (r'\.wordmark\{font-weight:800;color:var\(--navy\);font-size:1\.05rem;', r'.wordmark{font-weight:800;color:var(--navy);font-size:var(--text-lead);'),
    (r'header a\.phone\{color:var\(--navy\);font-weight:600;text-decoration:none;font-size:\.95rem', r'header a.phone{color:var(--navy);font-weight:600;text-decoration:none;font-size:var(--text-body)'),
    (r'\.section-title \{ color: var\(--navy-darkest, #2C3842\); font-size: 32px;', r'.section-title { color: var(--navy-darkest, #2C3842); font-size: var(--text-h2);'),
    (r'#compare table\.cmp \{ font-family: \'Roboto\', sans-serif; font-size: 18px;', r'#compare table.cmp { font-family: \'Roboto\', sans-serif; font-size: var(--text-body);'),
    (r'\.trustbar \.stat strong\{display:block;font-size:1\.6rem;', r'.trustbar .stat strong{display:block;font-size:var(--text-h3);'),
    (r'\.trustbar \.stat span\{font-size:\.85rem;', r'.trustbar .stat span{font-size:var(--text-small);'),
    
    # other specific lines that popped up
    (r'font-size: 0\.85rem;', r'font-size: var(--text-small);'),
    (r'font-size: 0\.95rem;', r'font-size: var(--text-body);'),
    (r'font-size: 1\.2rem;', r'font-size: var(--text-h3);'),
    (r'font-size: 0\.78rem;', r'font-size: var(--text-micro);'),
    (r'font-size: 0\.72rem;', r'font-size: var(--text-micro);'),
    (r'font-size: 1\.05rem;', r'font-size: var(--text-lead);'),
]

for old, new in replacements:
    text = re.sub(old, new, text)

# There are also some font-size in the media query block and some class styles like `font-size: 2rem; /* Standardized to 32px */`
text = re.sub(r'font-size: 2rem;\s*/\* Standardized to 32px \*/', r'font-size: var(--text-h2);', text)

with open('csl-investor-exit-advantage-v3.html', 'w') as f:
    f.write(text)

print("Done phase 2.")
