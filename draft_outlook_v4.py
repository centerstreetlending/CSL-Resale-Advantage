import os
import subprocess

reps = [
    ("Alec Ralph", "aralph", "aralph@centerstreetlending.com"),
    ("Allyssa Michaelson", "amichaelson", "amichaelson@centerstreetlending.com"),
    ("Angelica Naranjo", "anaranjo", "anaranjo@centerstreetlending.com"),
    ("Christine Flores", "cflores", "cflores@centerstreetlending.com"),
    ("Daniel Ayache", "dayache", "dayache@centerstreetlending.com"),
    ("Diana Smith", "dsmith", "dsmith@centerstreetlending.com"),
    ("Jeremy Mullins", "jmullins", "jmullins@centerstreetlending.com"), 
    ("Kevin Martinez", "kmartinez", "kmartinez@centerstreetlending.com"),
    ("Luis Montero", "lmontero", "lmontero@centerstreetlending.com"),
    ("Marlena DiMauro Lacourse", "mlacourse", "mlacourse@centerstreetlending.com"),
    ("Richard Vu", "rvu", "rvu@centerstreetlending.com"),
    ("Ryan Guerrero", "rguerrero", "rguerrero@centerstreetlending.com"),
    ("Sherif Hashem", "shashem", "shashem@centerstreetlending.com"),
    ("Erik Brown", "ebrown", "ebrown@centerstreetlending.com"),
    ("Jeremiah Wiedman", "jwiedman", "jwiedman@centerstreetlending.com"),
    ("Justin Wollmershauser", "jwollm", "jwollm@centerstreetlending.com"),
    ("Ryan St John", "rstjohn", "rstjohn@centerstreetlending.com"),
    ("Tanner Podres", "tpodres", "tpodres@centerstreetlending.com"),
    ("Angie Allen", "aallen", "aallen@centerstreetlending.com"),
    ("Austin Steedman", "asteedman", "asteedman@centerstreetlending.com"),
    ("Kara Armstrong", "karmstrong", "karmstrong@centerstreetlending.com"),
    ("Max Woodyard", "mwoodyard", "mwoodyard@centerstreetlending.com"),
    ("Michael Price", "mprice", "mprice@centerstreetlending.com"),
    ("Robert Newcomer", "rnewcomer", "rnewcomer@centerstreetlending.com"),
    ("Sean Burbidge", "sburbidge", "sburbidge@centerstreetlending.com"),
    ("Dallin Waldvogel", "dwaldvogel", "dwaldvogel@centerstreetlending.com"),
    ("Ford Fairon", "ffairon", "ffairon@centerstreetlending.com"),
    ("Guy Clauss", "gclauss", "gclauss@centerstreetlending.com"),
    ("Jack Guenther", "jguenther", "jguenther@centerstreetlending.com"),
    ("Ryan Clayton", "rclayton", "rclayton@centerstreetlending.com"),
    ("Sean Klement", "sklement", "sklement@centerstreetlending.com"),
    ("Brandon Herbert", "bherbert", "bherbert@centerstreetlending.com"),
    ("Crystal Mora", "cmora", "cmora@centerstreetlending.com"),
    ("Jacob Woodyard", "jwoodyard", "jwoodyard@centerstreetlending.com"),
    ("Lauren Lipinski", "llipinski", "llipinski@centerstreetlending.com"),
    ("Richard Kim", "rkim", "rkim@centerstreetlending.com"),
    ("Trevor Burbidge", "tburbidge", "tburbidge@centerstreetlending.com"),
    ("Jacob Cho", "jcho", "jcho@centerstreetlending.com")
]

subject = "CSL Resale Advantage – Your Custom Referral Link"

applescript_commands = []
applescript_commands.append('tell application "Microsoft Outlook"')

for name, username, email in reps:
    first_name = name.split()[0]
    
    body = f"""Hey {first_name},<br><br>

Check out the new website here: <a href="https://www.centerstreetlending.com/resale-advantage">https://www.centerstreetlending.com/resale-advantage</a><br><br>

Thanks for joining the information session this week on the new CSL Resale Advantage program!<br><br>

Below is your custom link to send to your borrowers:<br><br>

<strong><a href="https://www.centerstreetlending.com/resale-advantage?rep={username}">https://www.centerstreetlending.com/resale-advantage?rep={username}</a></strong><br><br>

When a borrower uses your link, your information is automatically pushed through the form and marked in the system. As a backup, we can also always confirm you are the referral by communicating directly with Innovate Realty.<br><br>

<strong>If you'd like to make a custom email signature with your URL, feel free to add it into your Signature block to get evergreen marketing for your referral link.</strong><br><br>

<em>Example: Find out how CSL borrowers are getting 1% exclusive listing fees on their next sale. [Learn more here.]</em><br><br>

If you have any questions about the program or need additional info, please reach out directly to Suzanne or Paul:<br><br>

<strong>Suzanne Seini</strong><br>
Innovate Realty<br>
suzanne@innovaterealty.com<br>
<em>— OR —</em><br>
<strong>Paul Hanson</strong><br>
phanson@byebyehouse.com<br><br><br>"""

    # Escape quotes and backslashes for AppleScript
    body = body.replace('\\', '\\\\').replace('"', '\\"')
    # Remove any actual newlines so applescript gets a single string for content
    body = body.replace('\n', '')
    
    applescript_commands.append(f'''
    set newMessage to make new outgoing message with properties {{subject:"{subject}", content:"{body}"}}
    make new to recipient at newMessage with properties {{email address:{{address:"{email}"}}}}
    open newMessage
    ''')

applescript_commands.append('end tell')
applescript = "\n".join(applescript_commands)

with open("/Users/gregmontoya/AntiGravity Workspaces/CSL-Resale-Advantage/open_outlook_v4.scpt", "w") as f:
    f.write(applescript)

print("Generated V4 AppleScript ready to run.")
