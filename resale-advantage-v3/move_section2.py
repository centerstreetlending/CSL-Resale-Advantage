import re

with open('csl-investor-exit-advantage-v3.html', 'r') as f:
    text = f.read()

# Define patterns
trust_marker = "<!-- TRUST / PARTNER NETWORK SECTION -->"
benefits_marker = "<!-- BENEFITS -->"
comparison_marker = "<!-- COMPARISON TABLE"

# Extract TRUST section
trust_start = text.find(trust_marker)
benefits_start = text.find(benefits_marker)

if trust_start != -1 and benefits_start != -1:
    trust_block = text[trust_start:benefits_start]
    
    # Remove from original location
    text = text[:trust_start] + text[benefits_start:]
    
    # Insert after BENEFITS (before COMPARISON)
    comparison_start = text.find(comparison_marker)
    if comparison_start != -1:
        text = text[:comparison_start] + trust_block + text[comparison_start:]
        
        with open('csl-investor-exit-advantage-v3.html', 'w') as f:
            f.write(text)
        print("Success")
    else:
        print("COMPARISON section not found")
else:
    print("TRUST or BENEFITS section not found")
