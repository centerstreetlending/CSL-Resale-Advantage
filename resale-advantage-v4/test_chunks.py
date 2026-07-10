import glob

# Read all chunks in order
files = sorted(glob.glob("webflow_embeds/*.txt"))
content = ""
for f in files:
    with open(f, "r") as file:
        content += file.read() + "\n"

with open("combined_chunks.html", "w") as out:
    out.write(content)

# Test for unclosed tags or syntax errors
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.tags = []
        self.errors = []
        
    def handle_starttag(self, tag, attrs):
        if tag not in ['img', 'br', 'hr', 'input', 'meta', 'link', 'path', 'circle', 'line', 'polygon', 'source']:
            self.tags.append(tag)
            
    def handle_endtag(self, tag):
        if tag not in ['img', 'br', 'hr', 'input', 'meta', 'link', 'path', 'circle', 'line', 'polygon', 'source']:
            if not self.tags:
                self.errors.append(f"Unexpected end tag {tag}")
            elif self.tags[-1] == tag:
                self.tags.pop()
            else:
                self.errors.append(f"Mismatched end tag {tag}, expected {self.tags[-1]}")

parser = MyHTMLParser()
parser.feed(content)

print(f"Remaining open tags: {parser.tags}")
print(f"Errors: {parser.errors}")

