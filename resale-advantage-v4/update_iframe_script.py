filepath = "csl-investor-exit-advantage-v4.html"
with open(filepath, "r") as f:
    content = f.read()

# I will replace the existing iframe resizer script with the new one
old_script = """<script>
  // Send height to parent window for iframe resizing
  function sendHeight() {
    var height = document.body.scrollHeight;
    window.parent.postMessage({ 'frameHeight': height }, '*');
  }
  window.addEventListener('load', sendHeight);
  window.addEventListener('resize', sendHeight);
  
  // Create a MutationObserver to watch for DOM changes (like accordions opening)
  const observer = new MutationObserver(sendHeight);
  observer.observe(document.body, { childList: true, subtree: true, attributes: true });
</script>"""

new_script = """<script>
  // Send height to parent window for iframe resizing
  function sendHeight() {
    var height = document.body.scrollHeight;
    window.parent.postMessage({ 'frameHeight': height }, '*');
  }
  window.addEventListener('load', sendHeight);
  window.addEventListener('resize', sendHeight);
  
  // Create a MutationObserver to watch for DOM changes
  const observer = new MutationObserver(sendHeight);
  observer.observe(document.body, { childList: true, subtree: true, attributes: true });

  // Intercept anchor clicks to scroll the parent window
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
      e.preventDefault();
      const targetId = this.getAttribute('href').substring(1);
      const targetElement = document.getElementById(targetId);
      if (targetElement) {
        const offsetTop = targetElement.offsetTop;
        window.parent.postMessage({ 'scrollToOffset': offsetTop }, '*');
      }
    });
  });
</script>"""

if old_script in content:
    content = content.replace(old_script, new_script)
else:
    print("Old script not found!")

with open(filepath, "w") as f:
    f.write(content)

print("Updated script successfully!")
