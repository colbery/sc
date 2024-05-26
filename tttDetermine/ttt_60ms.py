import numpy as np
import scipy.stats as stats

# Dane dla ttt=60ms
data_switches_60ms = [5, 4.21, 4.57, 4.24, 4.55, 4.68, 4.03, 3.9, 4.25, 4.13]
data_dropped_calls_60ms = [0.13, 0.2, 0.14, 0.13, 0.07, 0.17, 0.22, 0.18, 0.11, 0.21]
data_cell_boundary_60ms = [2249.4973594378803, 2336.3501726280224, 2330.8817178286617, 2484.253987127968, 2556.015245219203, 2519.1401213853596, 2578.537098536014, 2606.0142377933316, 2343.104063013652, 2658.9809814985483]

# Obliczanie średniej i odchylenia standardowego
mean_switches_60ms = np.mean(data_switches_60ms)
std_switches_60ms = np.std(data_switches_60ms, ddof=1)

mean_dropped_calls_60ms = np.mean(data_dropped_calls_60ms)
std_dropped_calls_60ms = np.std(data_dropped_calls_60ms, ddof=1)

mean_cell_boundary_60ms = np.mean(data_cell_boundary_60ms)
std_cell_boundary_60ms = np.std(data_cell_boundary_60ms, ddof=1)

# Liczebność próby
n_60ms = len(data_switches_60ms)

# Wartość t dla 95% poziomu ufności i 9 stopni swobody
t_value_60ms = stats.t.ppf(1 - 0.025, n_60ms - 1)

# Przedział ufności dla średniej liczby przełączeń użytkowników między stacjami
confidence_interval_switches_60ms = t_value_60ms * (std_switches_60ms / np.sqrt(n_60ms))

# Przedział ufności dla średniej liczby zerwanych połączeń radiowych
confidence_interval_dropped_calls_60ms = t_value_60ms * (std_dropped_calls_60ms / np.sqrt(n_60ms))

# Przedział ufności dla średniej granicy komórek
confidence_interval_cell_boundary_60ms = t_value_60ms * (std_cell_boundary_60ms / np.sqrt(n_60ms))

# Wyniki
print(f"Średnia liczba przełączeń: {mean_switches_60ms:.3f} ± {confidence_interval_switches_60ms:.3f}")
print(f"Przedział ufności: {confidence_interval_switches_60ms:.3f}")
print(f"Różnica: {confidence_interval_switches_60ms * 2:.3f}\n")

print(f"Średnia liczba zerwanych połączeń: {mean_dropped_calls_60ms:.3f} ± {confidence_interval_dropped_calls_60ms:.3f}")
print(f"Przedział ufności: {confidence_interval_dropped_calls_60ms:.3f}")
print(f"Różnica: {confidence_interval_dropped_calls_60ms * 2:.3f}\n")

print(f"Średnia granica komórek: {mean_cell_boundary_60ms:.3f} ± {confidence_interval_cell_boundary_60ms:.3f}")
print(f"Przedział ufności: {confidence_interval_cell_boundary_60ms:.3f}")
print(f"Różnica: {confidence_interval_cell_boundary_60ms * 2:.3f}\n")
