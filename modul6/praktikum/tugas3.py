from PIL import Image, ImageEnhance
import matplotlib.pyplot as plt

logo_path = "C:/xampp/htdocs/pemrograman_fungsional/modul6/praktikum/logo.jpeg"
background_path = "C:/xampp/htdocs/pemrograman_fungsional/modul6/praktikum/background.jpeg"

# Kecerahan dan Contras

logo = Image.open(logo_path)
kecerahan = ImageEnhance.Brightness(logo).enhance(1.6)
kontras = ImageEnhance.Contrast(kecerahan).enhance(1.2)
kontras.save("logo_edit.jpg")
plt.imshow (kontras)
plt.show()