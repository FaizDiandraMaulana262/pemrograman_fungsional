def translasi(x, y):
    def pergeseran(a, b):
        return (x + a), (y + b)
    return pergeseran

print(translasi(3, 5)(2, -1))

def dilatasi(x, y):
    def transform(a, b):
        return (a * x), (b * y)
    return transform

print(dilatasi(3, 5)(2, -1))

def rotasi(sudut):
    import math
    def transform(a, b):
        new_x = a * math.cos(math.radians(sudut)) - b * math.sin(math.radians(sudut))
        new_y = a * math.sin(math.radians(sudut)) + b * math.cos(math.radians(sudut))
        return new_x, new_y
    return transform

print(rotasi(30)(3, 5))