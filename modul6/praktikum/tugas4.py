from PIL import Image, ImageFilter
import matplotlib.pyplot as plt

logo_path = "C:/xampp/htdocs/pemrograman_fungsional/modul6/praktikum/logo_edit.jpg"
background_path = "C:/xampp/htdocs/pemrograman_fungsional/modul6/praktikum/background_edit.jpg"

logo = Image.open(logo_path)
background = Image.open(background_path)

#Tumpuk Gambar
background.paste(logo, (50, 50))
background.save("image.jpg")