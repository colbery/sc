import numpy as np
import scipy.stats as stats

# Dane dla ttt=80ms
data_switches_80ms = [1.32, 1.37, 1.49, 1.54, 1.39, 1.23, 1.42, 1.36, 1.31, 1.23]
data_dropped_calls_80ms = [0.17, 0.19, 0.17, 0.22, 0.17, 0.2, 0.11, 0.14, 0.17, 0.25]
data_cell_boundary_80ms = [2336.4327195071774, 2547.5089676782445, 2340.8953999147566, 2335.452800528955, 2343.68613214103, 2461.998147926693, 2473.692655848722, 2301.319071821805, 2480.8739412696873, 2618.4743608212348]

# Obliczanie średniej i odchylenia standardowego
mean_switches_80ms = np.mean(data_switches_80ms)
std_switches_80ms = np.std(data_switches_80ms, ddof=1)

mean_dropped_calls_80ms = np.mean(data_dropped_calls_80ms)
std_dropped_calls_80ms = np.std(data_dropped_calls_80ms, ddof=1)

mean_cell_boundary_80ms = np.mean(data_cell_boundary_80ms)
std_cell_boundary_80ms = np.std(data_cell_boundary_80ms, ddof=1)

# Liczebność próby
n_80ms = len(data_switches_80ms)

# Wartość t dla 95% poziomu ufności i 9 stopni swobody
t_value_80ms = stats.t.ppf(1 - 0.025, n_80ms - 1)

# Przedział ufności dla średniej liczby przełączeń użytkowników między stacjami
confidence_interval_switches_80ms = t_value_80ms * (std_switches_80ms / np.sqrt(n_80ms))

# Przedział ufności dla średniej liczby zerwanych połączeń radiowych
confidence_interval_dropped_calls_80ms = t_value_80ms * (std_dropped_calls_80ms / np.sqrt(n_80ms))

# Przedział ufności dla średniej granicy komórek
confidence_interval_cell_boundary_80ms = t_value_80ms * (std_cell_boundary_80ms / np.sqrt(n_80ms))

# Wyniki
print(f"Średnia liczba przełączeń: {mean_switches_80ms:.3f} ± {confidence_interval_switches_80ms:.3f}")
print(f"Przedział ufności: {confidence_interval_switches_80ms:.3f}")
print(f"Różnica: {confidence_interval_switches_80ms * 2:.3f}\n")

print(f"Średnia liczba zerwanych połączeń: {mean_dropped_calls_80ms:.3f} ± {confidence_interval_dropped_calls_80ms:.3f}")
print(f"Przedział ufności: {confidence_interval_dropped_calls_80ms:.3f}")
print(f"Różnica: {confidence_interval_dropped_calls_80ms * 2:.3f}\n")

print(f"Średnia granica komórek: {mean_cell_boundary_80ms:.3f} ± {confidence_interval_cell_boundary_80ms:.3f}")
print(f"Przedział ufności: {confidence_interval_cell_boundary_80ms:.3f}")
print(f"Różnica: {confidence_interval_cell_boundary_80ms * 2:.3f}\n")
