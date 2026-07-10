import re

with open('csl-investor-exit-advantage-v3.html', 'r') as f:
    text = f.read()

# Define patterns
trust_marker = "<!-- TRUST / PARTNER NETWORK SECTION -->"
benefits_marker = "<!-- BENEFITS -->"
comparison_marker = "<!-- COMPARISON TABLE"

# Extract TRUST section
trust_start = text.find(trust_marker)
comparison_start = text.find(comparison_marker)

if trust_start != -1 and comparison_start != -1:
    trust_block = text[trust_start:comparison_start]
    
    # Remove from original location
    text = text[:trust_start] + text[comparison_start:]
    
    # Insert before BENEFITS
    benefits_start = text.find(benefits_marker)
    if benefits_start != -1:
        text = text[:benefits_start] + trust_block + text[benefits_start:]
        
        with open('csl-investor-exit-advantage-v3.html', 'w') as f:
            f.write(text)
        print("Success")
    else:
        print("BENEFITS section not found")
else:
    print("TRUST or COMPARISON section not found")
