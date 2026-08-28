import re

with open('csl-investor-exit-advantage-v3.html', 'r') as f:
    text = f.read()

# Define patterns
trust_marker = "<!-- TRUST / PARTNER NETWORK SECTION -->"
who_marker = "<!-- WHO THIS IS FOR -->"
benefits_marker = "<!-- BENEFITS -->"

# Extract WHO THIS IS FOR block
who_start = text.find(who_marker)
benefits_start = text.find(benefits_marker)

if who_start != -1 and benefits_start != -1:
    who_block = text[who_start:benefits_start]
    
    # Remove from original location
    text = text[:who_start] + text[benefits_start:]
    
    # Insert before TRUST
    trust_start = text.find(trust_marker)
    if trust_start != -1:
        text = text[:trust_start] + who_block + text[trust_start:]
        
        with open('csl-investor-exit-advantage-v3.html', 'w') as f:
            f.write(text)
        print("Success")
    else:
        print("TRUST section not found")
else:
    print("WHO or BENEFITS section not found")
