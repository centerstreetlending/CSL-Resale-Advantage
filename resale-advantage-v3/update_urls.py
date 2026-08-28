import os

replacements = {
    "Frame 129.png": "https://cdn.prod.website-files.com/6875101e8b0848abe318fec3/6a515bd6440e3e36c2027a6c_Frame%20129.png",
    "Frame 166.png": "https://cdn.prod.website-files.com/6875101e8b0848abe318fec3/6a515bd69f565305fecfe7f3_Frame%20166.png",
    "Frame 169.png": "https://cdn.prod.website-files.com/6875101e8b0848abe318fec3/6a515bd6f9871e13803a5386_Frame%20169.png",
    "Frame 170.png": "https://cdn.prod.website-files.com/6875101e8b0848abe318fec3/6a515bd660aba88be11b2bcb_Frame%20170.png",
    "Rectangle 22.png": "https://cdn.prod.website-files.com/6875101e8b0848abe318fec3/6a515bd6ab320d0c10421561_Rectangle%2022.png",
    "innolaunch-brochure.jpg": "https://cdn.prod.website-files.com/6875101e8b0848abe318fec3/6a515bd6c3758e22331cfa5a_innolaunch-brochure.jpg",
    "innolaunch-campaign-app.jpg": "https://cdn.prod.website-files.com/6875101e8b0848abe318fec3/6a515bd66aee0d0a81fa8ee8_innolaunch-campaign-app.jpg",
    "innolaunch-flyer.jpg": "https://cdn.prod.website-files.com/6875101e8b0848abe318fec3/6a515bd6df26519519ab2c10_innolaunch-flyer.jpg",
    "innolaunch-ipad-debut.jpg": "https://cdn.prod.website-files.com/6875101e8b0848abe318fec3/6a515bd6ab320d0c10421547_innolaunch-ipad-debut.jpg",
    "innolaunch-postcard.jpg": "https://cdn.prod.website-files.com/6875101e8b0848abe318fec3/6a515bd611a6c9167e8f3406_innolaunch-postcard.jpg",
    "Company Logo.svg": "https://cdn.prod.website-files.com/6875101e8b0848abe318fec3/6a515fc78379809575373d48_Company%20Logo.svg",
    "HonestEscrow.svg": "https://cdn.prod.website-files.com/6875101e8b0848abe318fec3/6a515fc78379809575373d62_HonestEscrow.svg",
    "Innovate.svg": "https://cdn.prod.website-files.com/6875101e8b0848abe318fec3/6a515fc7b5dc722117959432_Innovate-1.svg",
    "logo1.svg": "https://cdn.prod.website-files.com/6875101e8b0848abe318fec3/6a515d82df26519519abc412_logo1.svg"
}

dir_path = "webflow_embeds"
for filename in os.listdir(dir_path):
    if filename.endswith(".txt"):
        filepath = os.path.join(dir_path, filename)
        with open(filepath, "r") as f:
            content = f.read()
        
        for k, v in replacements.items():
            content = content.replace(f'"{k}"', f'"{v}"')
            content = content.replace(f"'{k}'", f"'{v}'")
            
        with open(filepath, "w") as f:
            f.write(content)

print("Update complete!")
