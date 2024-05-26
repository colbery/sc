import numpy as np
import scipy.stats as stats

# Dane
data_switches = [17, 16.61, 16.56, 17.73, 17.56, 17.13, 17.98, 17.36, 18.55, 17.39]
data_dropped_calls = [0.16, 0.2, 0.19, 0.17, 0.13, 0.22, 0.16, 0.18, 0.17, 0.21]
data_cell_boundary = [2514.4238644481356, 2394.928548437426, 2406.68728409233, 2408.161168374117, 2500.687923670506, 2390.6020294168984, 2315.0515720484514, 2526.7299917489913, 2289.4602281258694, 2487.0932871208693]

# Obliczanie średniej i odchylenia standardowego
mean_switches = np.mean(data_switches)
std_switches = np.std(data_switches, ddof=1)

mean_dropped_calls = np.mean(data_dropped_calls)
std_dropped_calls = np.std(data_dropped_calls, ddof=1)

mean_cell_boundary = np.mean(data_cell_boundary)
std_cell_boundary = np.std(data_cell_boundary, ddof=1)

# Liczebność próby
n = len(data_switches)

# Wartość t dla 95% poziomu ufności i 9 stopni swobody
t_value = stats.t.ppf(1 - 0.025, n - 1)

# Przedział ufności dla średniej liczby przełączeń użytkowników między stacjami
confidence_interval_switches = t_value * (std_switches / np.sqrt(n))

# Przedział ufności dla średniej liczby zerwanych połączeń radiowych
confidence_interval_dropped_calls = t_value * (std_dropped_calls / np.sqrt(n))

# Przedział ufności dla średniej granicy komórek
confidence_interval_cell_boundary = t_value * (std_cell_boundary / np.sqrt(n))

# Wyniki
print(f"Średnia liczba przełączeń: {mean_switches:.3f} ± {confidence_interval_switches:.3f}")
print(f"Przedział ufności: {confidence_interval_switches:.3f}")
print(f"Różnica: {confidence_interval_switches * 2:.3f}\n")

print(f"Średnia liczba zerwanych połączeń: {mean_dropped_calls:.3f} ± {confidence_interval_dropped_calls:.3f}")
print(f"Przedział ufności: {confidence_interval_dropped_calls:.3f}")
print(f"Różnica: {confidence_interval_dropped_calls * 2:.3f}\n")

print(f"Średnia granica komórek: {mean_cell_boundary:.3f} ± {confidence_interval_cell_boundary:.3f}")
print(f"Przedział ufności: {confidence_interval_cell_boundary:.3f}")
print(f"Różnica: {confidence_interval_cell_boundary * 2:.3f}\n")
