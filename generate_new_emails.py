import os

new_reps = [
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
    ("Jacob Cho", "jcho", "jcho@centerstreetlending.com"),
]

template = """Subject: CSL Resale Advantage – Your Custom Referral Link

Hey {first_name},

Check out the new website here: https://www.centerstreetlending.com/resale-advantage
Thanks for joining the information session this week on the new CSL Resale Advantage program! 

Below is your custom link to send to your borrowers:

https://www.centerstreetlending.com/resale-advantage?rep={username}

When a borrower uses your link, your information is automatically pushed through the form and marked in the system. As a backup, we can also always confirm you are the referral by communicating directly with Innovate Realty. 

**If you'd like to make a custom email signature with your URL, feel free to add it into your Signature block to get evergreen marketing for your referral link.** 

*Example: Find out how CSL borrowers are getting 1% exclusive listing fees on their next sale. [Learn more here.]*

If you have any questions about the program or need additional info, please reach out directly to Suzanne or Paul:

Suzanne Seini
Innovate Realty
suzanne@innovaterealty.com

— OR —

Paul Hanson
phanson@byebyehouse.com

Thanks,

Greg"""

md_template = """---

**To:** {email}
**Subject:** CSL Resale Advantage – Your Custom Referral Link

Hey **{first_name}**,

Check out the new website here: https://www.centerstreetlending.com/resale-advantage
Thanks for joining the information session this week on the new **CSL Resale Advantage** program! 

Below is **your custom link** to send to your borrowers:

**https://www.centerstreetlending.com/resale-advantage?rep={username}**

When a borrower uses your link, your information is automatically pushed through the form and marked in the system. As a backup, we can also always confirm you are the referral by communicating directly with Innovate Realty. 

**If you'd like to make a custom email signature with your URL, feel free to add it into your Signature block to get evergreen marketing for your referral link.** 

*Example: Find out how CSL borrowers are getting 1% exclusive listing fees on their next sale. [Learn more here.]*

If you have any questions about the program or need additional info, please reach out directly to Suzanne or Paul:

**Suzanne Seini**  
Innovate Realty  
suzanne@innovaterealty.com  


*— OR —*


**Paul Hanson**  
phanson@byebyehouse.com  


Thanks,

Greg

"""

rep_emails_dir = "/Users/gregmontoya/AntiGravity Workspaces/CSL-Resale-Advantage/rep_emails"
os.makedirs(rep_emails_dir, exist_ok=True)

md_file_path = "/Users/gregmontoya/.gemini/antigravity/brain/d8ed1cad-686d-4d54-bfd9-c63622b74471/customized_rep_emails.md"
with open(md_file_path, "a") as md_file:
    for name, username, email in new_reps:
        first_name = name.split()[0]
        
        # Write individual text file
        file_path = os.path.join(rep_emails_dir, f"{name.replace(' ', '_')}.txt")
        with open(file_path, "w") as f:
            f.write(template.format(first_name=first_name, username=username))
            
        # Append to master markdown
        md_file.write(md_template.format(email=email, first_name=first_name, username=username))

print("Done generating 26 files and appending to MD.")
