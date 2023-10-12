def hitung_nilai_akhir(uts, uas):
    nilai_akhir = (uts + uas) / 2
    return nilai_akhir

def hitung_nilai_akhir_semua_mahasiswa(data_mahasiswa):
    temp_data_nilai_akhir = {}
    for nama, nilai in data_mahasiswa.items():
        uts = nilai["uts"]
        uas = nilai["uas"]
        nilai_akhir = hitung_nilai_akhir(uts, uas)
        temp_data_nilai_akhir[nama] = nilai_akhir
    return temp_data_nilai_akhir

def tampilkan_nilai_akhir(data_nilai_akhir):
    print("Hasil Nilai Akhir Mahasiswa: ")
    for nama, nilai_akhir in data_nilai_akhir.items():
        print("Nama : {}\tNilai Akhir: {:.2f}".format(nama, nilai_akhir))

def main():
    data_mahasiswa = {
        "lorem": {"uts": 75, "uas": 85}, "ipsum": {"uts": 70, "uas": 90}, "dolor": {"uts": 87, "uas": 70}
    }
    
    data_nilai_akhir = hitung_nilai_akhir_semua_mahasiswa(data_mahasiswa)
    
    tampilkan_nilai_akhir(data_nilai_akhir)
    
if __name__ == "__main__":
    main()