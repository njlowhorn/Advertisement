# Advertisement V2 by Nolan Lowhorn
# 9/15/2021

# Imports
from PIL import Image, ImageFilter, ImageEnhance, ImageFont, ImageDraw

# Opens images
image = Image.open(r"Background.jpg").resize((1750, 875))
image1 = Image.open(r"soda.png")

#
image = ImageEnhance.Color(image)
image = image.enhance(5)
image = image.filter(ImageFilter.GaussianBlur)

image1 = image1.filter(ImageFilter.SMOOTH_MORE)

image.paste(image1, (570, 310), image1)

test = ImageDraw.Draw(image)
f = ImageFont.truetype("palabi.ttf", 100)
test.text((306, 36), "Crush Your Thirst With \n \n     Crush Orange Soda", fill=(0, 0, 0), font = f)
test.text((298, 28), "Crush Your Thirst With \n \n     Crush Orange Soda", fill=(0, 0, 0), font = f)
test.text((303, 33), "Crush Your Thirst With \n \n     Crush Orange Soda", fill=(255, 255, 0), font = f)
test.text((300, 30), "Crush Your Thirst With \n \n     Crush Orange Soda", fill=(255, 0, 0), font = f)

image = image.filter(ImageFilter.EDGE_ENHANCE)

image.show()

image.save(r"C:\Users\njlowhorn\Desktop\Images\Advertisements\Advertisement.png")