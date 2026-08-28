filepath = "csl-investor-exit-advantage-v4.html"
with open(filepath, "r") as f:
    content = f.read()

script = """
<script>
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
</script>
</body>
"""

content = content.replace("</body>", script)

with open(filepath, "w") as f:
    f.write(content)

print("Added iframe resizer script!")
