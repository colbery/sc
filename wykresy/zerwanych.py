import matplotlib.pyplot as plt
import numpy as np

# Data from the provided Excel screenshot
ttt_values = [20, 40, 60, 80, 100]
average_values = [0.28, 0.18, 0.16, 0.18, 0.22]
confidence_intervals = [0.033278, 0.018224, 0.032657, 0.026661, 0.031419]

plt.figure(figsize=(10, 6))
plt.errorbar(ttt_values, average_values, yerr=confidence_intervals, fmt='o', ecolor='orange', capsize=5, linestyle='None', marker='o', markersize=5, markerfacecolor='orange', color='orange')

plt.title('Wykres średniej liczby zerwanych połączeń')
plt.xlabel('ttt [ms]')
plt.ylabel('Średnia liczba zerwanych połączeń')
plt.grid(True)

# Save the plot as a PNG image
plt.savefig('average_disconnections_plot.png')

# Display the plot
plt.show()
