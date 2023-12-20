from PIL import ImageDraw, ImageFont, Image
import matplotlib.pyplot as plt

image_path = "C:/xampp/htdocs/pemrograman_fungsional/modul6/WhatsApp Image 2023-12-08 at 14.04.00_90cdadd3.jpg"
imageSave_path = "C:/xampp/htdocs/pemrograman_fungsional/modul6/test.jpg"
font_path = "C:/xampp/htdocs/pemrograman_fungsional/modul6/Poppins/Poppins-Light.ttf"

gambarku = Image.open(image_path)
gambarConvert = gambarku.convert("L")

draw = ImageDraw.Draw(gambarConvert)
font = ImageFont.truetype(font_path, 24)
text = "Faiz Diandra Maulana_202110370311262"
draw.text((450, 300), text, font = font)
gambarConvert.save("test.jpg")

gambarkuSave = Image.open(imageSave_path)
plt.imshow(gambarkuSave)
plt.show()