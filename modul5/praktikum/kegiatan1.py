import matplotlib.pyplot as plt
from functools import reduce

nilai_mahasiswa = [75, 80, 90, 65, 70, 85, 95, 78, 88, 92]

average = reduce(lambda x, y: x + y, nilai_mahasiswa) / len(nilai_mahasiswa)

label = list(map(lambda x: x+1, range(len(nilai_mahasiswa))))

plt.bar(label, nilai_mahasiswa, color="blue")
plt.xlabel("Mahasiswa")
plt.ylabel("Nilai Ujian")
plt.title("Diagram Batang Nilai Ujian Mahasiswa")
plt.axhline(average, color="red", linestyle="dashed", label="Rata-rata : " + str(average))
plt.legend()
plt.show()