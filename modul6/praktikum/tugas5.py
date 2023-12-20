from PIL import Image, ImageDraw, ImageFont
import matplotlib.pyplot as plt

image_path = "C:/xampp/htdocs/pemrograman_fungsional/modul6/praktikum/image.jpg"
font_path = "C:/xampp/htdocs/pemrograman_fungsional/modul6/praktikum/Arial.ttf"

#Draw Image
image = Image.open(image_path).resize((500, 300))
font = ImageFont.truetype(font_path, 24)
draw = ImageDraw.Draw(image).text((250, 100), "INFORMATIKA JOSSS!", font=font, fill=0)

image.save("image_draw.jpg")