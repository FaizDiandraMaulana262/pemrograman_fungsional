def point(x,y):
    return x,y

def line_equation_of(p1, M):
    x1, y1 = p1

    def hitung_konstanta(x):
        return M * (x - x1) + y1
    
    C = hitung_konstanta(0)
    return f"y = {M:.2f}x + {C:.2f}"


print("Persamaan garis yang melalui titik (6,-2) dan bergradien 2:")
print(line_equation_of(point(6,-2),-2))