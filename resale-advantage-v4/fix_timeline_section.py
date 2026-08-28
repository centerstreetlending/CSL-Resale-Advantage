with open('csl-investor-exit-advantage-v3.html', 'r') as f:
    html = f.read()

# Let's see if we can wrap the timeline in a <section class="timeline-section"> or remove the dangling </section>
# The timeline is:
#   <div class="wrap">
#     <div class="tl" id="exit-timeline">
# ...
#       </div>
#     </div>
#   </div>
# </section>
# <!-- BENEFITS -->

# If we just replace </section>\n\n<!-- BENEFITS --> with <!-- BENEFITS -->, that might fix it.
# Wait, actually, let's just make it a valid section by adding <section class="timeline-section"> before <div class="wrap">

timeline_start = '  <div class="wrap">\n    <div class="tl" id="exit-timeline">'
html = html.replace(timeline_start, '<section class="timeline-section">\n' + timeline_start)

with open('csl-investor-exit-advantage-v3.html', 'w') as f:
    f.write(html)
print("Added section tag")
