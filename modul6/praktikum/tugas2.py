from PIL import Image, ImageFilter
import matplotlib.pyplot as plt

logo_path = "C:/xampp/htdocs/pemrograman_fungsional/modul6/praktikum/logo.jpeg"
background_path = "C:/xampp/htdocs/pemrograman_fungsional/modul6/praktikum/background.jpeg"

# Ubah Background
background_change = Image.open(background_path).convert("L").rotate(30).filter(ImageFilter.BLUR)
background_change.save("background_edit.jpg")
plt.imshow(background_change)
plt.show()