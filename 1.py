import numpy as np
import matplotlib.pyplot as plt

# Statyczne dane
ttt_values = [20, 40, 60, 80, 100]
average_values = [73.952, 17.387, 4.356, 1.384, 0.861]
confidence_intervals = [1.714556353, 0.4144139796, 0.278431398, 0.08465426146, 0.0411501249]

# Tworzenie wykresu
plt.figure(figsize=(10, 6))
plt.errorbar(ttt_values, average_values, yerr=confidence_intervals, fmt='o', ecolor='blue', capsize=5, linestyle='None', marker='o', markersize=5, markerfacecolor='blue')
plt.xlabel('Oś ttt [ms]')
plt.ylabel('Oś średnia przełączeń')
plt.title('Wykres średniej liczby przełączeń na użytkownika')
plt.grid(True)  # Dodanie kratek
plt.show()
