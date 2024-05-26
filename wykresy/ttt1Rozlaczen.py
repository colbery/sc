import matplotlib.pyplot as plt
import numpy as np

# Dane dla ttt=1=20ms (rozłączenia)
v_values = [5, 15, 25, 35, 45]
average_disconnections = [0.827, 0.424, 0.306, 0.216, 0.17]
confidence_intervals = [0.021944, 0.030885, 0.035365, 0.02642, 0.015996]

# Tworzenie wykresu dla ttt=1=20ms (rozłączenia)
plt.figure(figsize=(10, 5))
plt.errorbar(v_values, average_disconnections, yerr=confidence_intervals, fmt='o', ecolor='orange', capsize=5, linestyle='None', marker='o', markersize=5, markerfacecolor='orange')
plt.xlabel('Prędkość (v)')
plt.ylabel('Średnia liczba rozłączeń')
plt.title('Wykres średniej liczby rozłączeń przy ttt=1=20ms')
plt.grid(True)
plt.show()
