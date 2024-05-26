import matplotlib.pyplot as plt
import numpy as np

# Dane dla ttt=1=20ms
v_values_1 = [5, 15, 25, 35, 45]
average_switches_1 = [216.087, 122.012, 79.64, 59.782, 48.324]
confidence_intervals_1 = [12.63897, 3.65155, 2.524685, 1.24333, 0.805787]

# Tworzenie wykresu dla ttt=1=20ms
plt.figure(figsize=(10, 5))
plt.errorbar(v_values_1, average_switches_1, yerr=confidence_intervals_1, fmt='o', ecolor='blue', capsize=5, linestyle='None', marker='o', markersize=5, markerfacecolor='blue')
plt.xlabel('Prędkość (v)')
plt.ylabel('Średnia liczba przełączeń')
plt.title('Wykres średniej liczby przełączeń przy ttt=1=20ms')
plt.grid(True)
plt.show()

# Dane dla ttt=3=60ms
v_values_3 = [5, 15, 25, 35, 45]
average_switches_3 = [15.362, 7.119, 4.633, 3.428, 2.728]
confidence_intervals_3 = [0.595234, 0.210962, 0.25749, 0.145441, 0.125046]

# Tworzenie wykresu dla ttt=3=60ms
plt.figure(figsize=(10, 5))
plt.errorbar(v_values_3, average_switches_3, yerr=confidence_intervals_3, fmt='o', ecolor='blue', capsize=5, linestyle='None', marker='o', markersize=5, markerfacecolor='blue')
plt.xlabel('Prędkość (v)')
plt.ylabel('Średnia liczba przełączeń')
plt.title('Wykres średniej liczby przełączeń przy ttt=3=60ms')
plt.grid(True)
plt.show()
