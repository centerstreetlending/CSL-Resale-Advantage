filepath = "csl-investor-exit-advantage-v4.html"
with open(filepath, "r") as f:
    content = f.read()

old_dropdown = """<select id="timeline" name="timeline" required>
            <option value="">Select one&hellip;</option>
            <option value="ASAP">ASAP</option>
            <option value="30-60 days">30-60 days</option>
            <option value="60-90 days">60-90 days</option>
            <option value="90+ days">90+ days</option>
            <option value="Just exploring my options">Just exploring my options</option>
          </select>"""

new_radios = """<div class="timeline-radios">
            <label class="radio-btn"><input type="radio" name="timeline_radio" value="ASAP" required> <span>ASAP</span></label>
            <label class="radio-btn"><input type="radio" name="timeline_radio" value="30-60 days"> <span>30-60 days</span></label>
            <label class="radio-btn"><input type="radio" name="timeline_radio" value="60-90 days"> <span>60-90 days</span></label>
            <label class="radio-btn"><input type="radio" name="timeline_radio" value="90+ days"> <span>90+ days</span></label>
            <label class="radio-btn" style="grid-column: 1 / -1;"><input type="radio" name="timeline_radio" value="Just exploring my options"> <span>Just exploring my options</span></label>
          </div>
          <input type="hidden" id="timeline" name="timeline">
          <script>
            document.querySelectorAll('input[name="timeline_radio"]').forEach(radio => {
              radio.addEventListener('change', function() {
                document.getElementById('timeline').value = this.value;
              });
            });
          </script>"""

old_css = "/* form */"
new_css = """/* form */
  .timeline-radios { display: grid; grid-template-columns: 1fr 1fr; gap: 10px; }
  .radio-btn { display: block; position: relative; cursor: pointer; }
  .radio-btn input { position: absolute; opacity: 0; cursor: pointer; height: 0; width: 0; }
  .radio-btn span { display: block; padding: 12px 16px; border: 1px solid var(--line); border-radius: 6px; font-size: 15px; text-align: center; background: #fff; color: var(--ink); transition: all 0.2s; }
  .radio-btn input:checked ~ span { background: var(--accent); color: #fff; border-color: var(--accent); font-weight: 600; }
  .radio-btn:hover span { border-color: var(--accent); }"""

if old_dropdown in content and old_css in content:
    content = content.replace(old_dropdown, new_radios)
    content = content.replace(old_css, new_css)
else:
    print("Could not find targets!")

with open(filepath, "w") as f:
    f.write(content)

print("Replaced dropdown with radios!")
