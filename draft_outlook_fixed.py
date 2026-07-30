import os
import subprocess
import re

md_path = "/Users/gregmontoya/.gemini/antigravity/brain/d8ed1cad-686d-4d54-bfd9-c63622b74471/customized_rep_emails.md"
with open(md_path, 'r') as f:
    content = f.read()

chunks = content.split('---')

applescript_commands = []
applescript_commands.append('tell application "Microsoft Outlook"')

count = 0
for chunk in chunks:
    chunk = chunk.strip()
    if not chunk.startswith('**To:**'):
        continue
    
    # Extract email
    email_match = re.search(r'\*\*To:\*\* (.*?)\n', chunk)
    if not email_match:
        continue
    email = email_match.group(1).strip()
    
    # Extract subject
    subject_match = re.search(r'\*\*Subject:\*\* (.*?)\n', chunk)
    subject = subject_match.group(1).strip() if subject_match else "CSL Resale Advantage – Your Custom Referral Link"
    
    # Extract body
    body_raw = chunk.split(subject_match.group(0))[1].strip()
    
    # Remove markdown formatting for the actual email
    body = body_raw.replace('**', '')
    
    # Convert newlines to HTML line breaks so Outlook doesn't flatten them!
    body = body.replace('\n', '<br>')
    
    # Escape quotes and backslashes for AppleScript
    body = body.replace('\\', '\\\\').replace('"', '\\"')
    
    applescript_commands.append(f'''
    set newMessage to make new outgoing message with properties {{subject:"{subject}", content:"{body}"}}
    make new to recipient at newMessage with properties {{email address:{{address:"{email}"}}}}
    open newMessage
    ''')
    
    count += 1

applescript_commands.append('end tell')
applescript = "\n".join(applescript_commands)

with open("/Users/gregmontoya/AntiGravity Workspaces/CSL-Resale-Advantage/open_outlook_fixed.scpt", "w") as f:
    f.write(applescript)

print("Generated fixed AppleScript. Running...")
result = subprocess.run(["osascript", "/Users/gregmontoya/AntiGravity Workspaces/CSL-Resale-Advantage/open_outlook_fixed.scpt"], capture_output=True, text=True)
print("Return code:", result.returncode)
if result.stdout:
    print("Stdout:", result.stdout)
if result.stderr:
    print("Stderr:", result.stderr)
