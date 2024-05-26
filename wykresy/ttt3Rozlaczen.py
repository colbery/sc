import matplotlib.pyplot as plt
import numpy as np

# Dane dla ttt=3=60ms (rozłączenia)
v_values = [5, 15, 25, 35, 45]
average_disconnections = [0.646, 0.278, 0.278, 0.152, 0.114]
confidence_intervals = [0.035939, 0.024945, 0.024945, 0.030246, 0.021797]

# Tworzenie wykresu dla ttt=3=60ms (rozłączenia)
plt.figure(figsize=(10, 5))
plt.errorbar(v_values, average_disconnections, yerr=confidence_intervals, fmt='o', ecolor='orange', capsize=5, linestyle='None', marker='o', markersize=5, markerfacecolor='orange')
plt.xlabel('Prędkość (v)')
plt.ylabel('Średnia liczba rozłączeń')
plt.title('Wykres średniej liczby rozłączeń przy ttt=3=60ms')
plt.grid(True)
plt.show()
