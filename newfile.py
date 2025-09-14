from PIL import Image, ImageDraw, ImageFont

# Create a blank canvas (width, height) with background color
canvas = Image.new("RGB", (800, 600), "lightblue")

# Initialize drawing context
draw = ImageDraw.Draw(canvas)

# Load default font
font_title = ImageFont.load_default()
font_mascot = ImageFont.load_default()
font_slogan = ImageFont.load_default()

# Title Banner (Rectangle)
draw.rectangle([(0, 0), (800, 100)], fill="darkblue")

# Title Text
draw.text((200, 20), "BSCS 4 - TEAM SPIRIT!", font=font_title, fill="white")

# Team Mascot (Circle Shape)
draw.ellipse([(300, 200), (500, 400)], fill="gold", outline="black", width=5)

# Mascot Name Text
draw.text((340, 420), "Golden Cats", font=font_mascot, fill="black")

# Slogan
draw.text((200, 500), "“Strength • Unity • Victory!”", font=font_slogan, fill="darkred")

# Save the poster
canvas.save("BSCS4_TeamSpirit_Poster.png")

print("Poster created successfully!")
