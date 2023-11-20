# lengkapi kode berikut untuk mendapatkan persamaan garis lurus bagi NIM GENAP
def point(x,y):
    return x,y

def line_equation_of(p1, p2):
    x1, y1 = p1
    x2, y2 = p2

    M = (y2 - y1) / (x2 - x1)
    C = y1 - M * x1
    return f"y = {M:.2f}x + {C:.2f}"

print("Persamaan garis yang melalui titik A dan B:")
print(line_equation_of(point(4,-2),point(-1,3)))