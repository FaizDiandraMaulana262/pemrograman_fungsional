import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

tinggi_badan = [165, 170, 155, 172, 180, 160, 175, 165, 185, 175, 170, 160]
interval_size = 10 

def group_into_intervals(data, interval_size):
    grouped_data = {}
    for value in data:
        interval_lower = (value // interval_size) * interval_size
        interval = (interval_lower, interval_lower + interval_size)
        grouped_data[interval] = grouped_data.get(interval, 0) + 1
    return grouped_data

frekuensi_tinggi_badan = group_into_intervals(tinggi_badan, interval_size)

intervals = list(frekuensi_tinggi_badan.keys())
frekuensi = list(frekuensi_tinggi_badan.values())

mean = np.mean(tinggi_badan) 
std = np.std(tinggi_badan)
xmin = np.min(tinggi_badan) 
xmax = np.max(tinggi_badan)
x = np.linspace(xmin, xmax, 100)
p = norm.pdf(x, mean, std)

scaling_factor = 0.5 / max(p)  
p_scaled = p * scaling_factor

flat_intervals = np.array(intervals).ravel()

sorted_intervals = sorted(flat_intervals)

plt.plot(x, p_scaled * len(tinggi_badan), label='PDF', color='red')

plt.hist(tinggi_badan, bins=sorted_intervals, label='Data',  color='blue')
plt.xlabel('Interval Tinggi Badan')
plt.ylabel('Frekuensi')
plt.title('Histogram Frekuensi Tinggi Badan')
plt.legend()
plt.show()
