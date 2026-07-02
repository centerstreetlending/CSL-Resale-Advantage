import re

with open('csl-investor-exit-advantage-v3.html', 'r') as f:
    text = f.read()

# 1. Extract TRUST section
trust_marker = "<!-- TRUST / PARTNER NETWORK SECTION -->"
benefits_marker = "<!-- BENEFITS -->"
trust_start = text.find(trust_marker)
benefits_start = text.find(benefits_marker)

if trust_start != -1 and benefits_start != -1:
    trust_block = text[trust_start:benefits_start]
    # Remove from original location
    text = text[:trust_start] + text[benefits_start:]
    
    # 2. Find the end of "Who this is for"
    # It ends with:
    #     <div class="who-right">
    #       <img src="Rectangle 22.png" alt="Happy couple in new home">
    #     </div>
    # 
    #   </div>
    # </section>
    
    who_end_str = '  </div>\n</section>'
    who_marker_idx = text.find("<!-- WHO THIS IS FOR -->")
    
    # Find the FIRST </section> after WHO THIS IS FOR
    first_section_close = text.find("</section>", who_marker_idx)
    insert_idx = first_section_close + len("</section>\n")
    
    text = text[:insert_idx] + "\n" + trust_block + "\n" + text[insert_idx:]
    
    with open('csl-investor-exit-advantage-v3.html', 'w') as f:
        f.write(text)
    print("Success")
else:
    print("Could not find TRUST or BENEFITS marker")
