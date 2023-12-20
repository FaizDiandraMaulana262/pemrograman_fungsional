from PIL import Image

logo_path = "C:/xampp/htdocs/pemrograman_fungsional/modul6/praktikum/logo.jpeg"
background_path = "C:/xampp/htdocs/pemrograman_fungsional/modul6/praktikum/background.jpeg"

# Buka Kedua Gambar
logo_image = Image.open(logo_path).show()
background_image = Image.open(background_path).show()
