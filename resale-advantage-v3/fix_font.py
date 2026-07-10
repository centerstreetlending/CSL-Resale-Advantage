import os

dir_path = "webflow_embeds"
for filename in os.listdir(dir_path):
    if filename.endswith(".txt"):
        filepath = os.path.join(dir_path, filename)
        with open(filepath, "r") as f:
            content = f.read()
        
        # Remove the @font-face block entirely
        import re
        content = re.sub(r'^\s*@font-face\s*\{\s*font-family:\s*\'Arteria Std Compress\';\s*src:\s*local\(\'Arteria Std Compress\'\);\s*font-display:\s*swap;\s*\}', '', content, flags=re.MULTILINE)
        
        # Replace the font-family strings
        content = content.replace("'Arteria Std Compress', 'Bebas Neue', sans-serif", "'Bebas Neue', 'Roboto', sans-serif")
        
        with open(filepath, "w") as f:
            f.write(content)

print("Font replaced!")
