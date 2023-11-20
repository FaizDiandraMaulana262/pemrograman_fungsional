import transformation as transform
import linear as line

@transform.dilatasi
@transform.rotasi
@transform.translasi
def setVal(x, y):
    return {"x" : x, "y" : y}

def main():
    x = int(input("Masukan Nilai X : "))
    y = int(input("Masukan Nilai Y : "))
    z = int(input("Masukan Nilai Z : "))
    
    transform = setVal(x, y)
    print(f"Persamaan garis yang melalui titik ({x},{y}) dan ({y},{z}) :\n{line.line_equation_of((x, y), (y, z))}")
    print(f"Persamaan garis baru setelah transformasi:\ny = {transform["x"]}x + {transform["y"]}")

if __name__ == "__main__":
    main()