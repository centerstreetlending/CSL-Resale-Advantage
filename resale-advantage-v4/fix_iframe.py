filepath = "csl-investor-exit-advantage-v4.html"
with open(filepath, "r") as f:
    content = f.read()

old_script = """<script>
  // Send height to parent window for iframe resizing
  function sendHeight() {
    var height = document.body.scrollHeight;
    window.parent.postMessage({ 'frameHeight': height }, '*');
  }"""

new_script = """<script>
  // Send height to parent window for iframe resizing
  var lastHeight = 0;
  function sendHeight() {
    var height = document.body.scrollHeight;
    if (height !== lastHeight) {
      lastHeight = height;
      window.parent.postMessage({ 'frameHeight': height }, '*');
    }
  }"""

if old_script in content:
    content = content.replace(old_script, new_script)
else:
    print("Old script not found!")

with open(filepath, "w") as f:
    f.write(content)

print("Fixed iframe script!")
