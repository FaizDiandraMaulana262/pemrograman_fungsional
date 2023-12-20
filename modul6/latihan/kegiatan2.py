from PIL import ImageDraw, ImageFont, Image
import matplotlib.pyplot as plt

bg_path = "C:/xampp/htdocs/pemrograman_fungsional/modul6/bg.png"
overlay_path = "C:/xampp/htdocs/pemrograman_fungsional/modul6/WhatsApp Image 2023-12-08 at 14.04.00_90cdadd3.jpg"

background_image = Image.open(bg_path)
overlay_image = Image.open(overlay_path)

overlay_image = overlay_image.convert("RGB")

plt.imshow(overlay_image)
plt.show()