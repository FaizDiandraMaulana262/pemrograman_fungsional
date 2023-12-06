import matplotlib.pyplot as plt
import numpy as np

data_transaksi = [
    ("Produk A", 50, 10),
    ("Produk B", 30, 25),
    ("Produk C", 20, 30),
    ("Produk D", 60, 8),
    ("Produk E", 40, 15),
    ("Produk F", 70, 5),
]

label1 = [item[1] for item in data_transaksi]
sell = [item[2] for item in data_transaksi]

income = [item[1] * item[2] for item in data_transaksi]
label2 = [item[0] for item in data_transaksi]

fig, (plot1, plot2) = plt.subplots(1, 2, figsize=(10, 5))

plot1.scatter(label1, sell, color='red')
plot1.set_xlabel('Harga Produk')
plot1.set_ylabel('Jumlah Produk Terjual')
plot1.set_title('Scatter Plot Hubungan Harga dan Jumlah Terjual')

plot2.bar(label2, income, color='red')
plot2.set_xlabel('Produk')
plot2.set_ylabel('Total Pendapatan')
plot2.set_title('Diagram Balok Total Pendapatan Produk')

plt.show()
