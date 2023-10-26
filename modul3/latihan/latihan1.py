data = ["3 minggu 3 hari 7 jam 21 menit",
        "5 minggu 5 hari 8 jam 11 menit", 
        "7 minggu 1 hari 5 jam 33 menit"]

def split(datas):
    angka = []
    for i in datas :
        angka.append([int(word) for word in i.split() if word.isdigit()])
    return angka
            
def currying(minggu):
    def hari(hari):
        def jam(jam):
            def menit(menit):
                return (((minggu * 7) * 24) * 60) + ((hari * 24) * 60) + (jam * 60) + menit
            return menit
        return jam
    return hari

def main():
    for i in split(data):
        print(currying(i[0])(i[1])(i[2])(i[3]))

if __name__ == "__main__":
    main()