import numpy as np
import scipy.stats as stats

# Dane
data_switches = [76.94, 74.89, 72.81, 70.4, 71.82, 72.82, 72.73, 78.51, 75.94, 72.66]
data_dropped_calls = [0.21, 0.26, 0.29, 0.35, 0.32, 0.3, 0.31, 0.19, 0.26, 0.27]
data_cell_boundary = [2607.822755382131, 2336.7682521888605, 2552.5524456397293, 2422.542227264091, 2309.7408519029436, 2435.103812583105, 2541.2479056647003, 2407.23929696199, 2257.0935046762734, 2633.553023831908]

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
print(f"Średnia liczba przełączeń: {mean_switches} ± {confidence_interval_switches}")
print(f"Średnia liczba zerwanych połączeń: {mean_dropped_calls} ± {confidence_interval_dropped_calls}")
print(f"Średnia granica komórek: {mean_cell_boundary} ± {confidence_interval_cell_boundary}")
