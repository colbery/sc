import numpy as np
import scipy.stats as stats

# Dane wejściowe
switch_counts = [16.74, 14.7, 15.2, 15.23, 14.55, 14.38, 14.75, 15.12, 16.41, 16.54]
disconnections = [0.58, 0.64, 0.74, 0.58, 0.67, 0.68, 0.69, 0.67, 0.61, 0.6]
cell_boundaries = [2352.9271804058003, 2626.0698639451316, 2625.4630263153654, 2513.6434018144436,
                   2625.1124398621064, 2568.783727398729, 2678.4134237283665, 2521.026521165391,
                   2604.365326020276, 2644.5052599753612]

# Obliczenia średnich
mean_switch_counts = np.mean(switch_counts)
mean_disconnections = np.mean(disconnections)
mean_cell_boundaries = np.mean(cell_boundaries)

# Obliczenia przedziałów ufności
confidence_level = 0.95
degrees_freedom = len(switch_counts) - 1
sample_standard_error = stats.sem(switch_counts)
confidence_interval_switch_counts = stats.t.interval(confidence_level, degrees_freedom, mean_switch_counts, sample_standard_error)

sample_standard_error = stats.sem(disconnections)
confidence_interval_disconnections = stats.t.interval(confidence_level, degrees_freedom, mean_disconnections, sample_standard_error)

sample_standard_error = stats.sem(cell_boundaries)
confidence_interval_cell_boundaries = stats.t.interval(confidence_level, degrees_freedom, mean_cell_boundaries, sample_standard_error)

# Wyliczenie połowy różnicy dla przedziałów ufności
half_range_switch_counts = (confidence_interval_switch_counts[1] - confidence_interval_switch_counts[0]) / 2
half_range_disconnections = (confidence_interval_disconnections[1] - confidence_interval_disconnections[0]) / 2
half_range_cell_boundaries = (confidence_interval_cell_boundaries[1] - confidence_interval_cell_boundaries[0]) / 2

# Wyświetlanie wyników
print("Średnia liczba przełączeń użytkowników między stacjami:", mean_switch_counts)
print("Średnia liczba zerwanych połączeń radiowych:", mean_disconnections)
print("Średnia granica komórek:", mean_cell_boundaries)

print("Przedział ufności dla liczby przełączeń użytkowników między stacjami (połowa różnicy):", half_range_switch_counts)
print("Przedział ufności dla liczby zerwanych połączeń radiowych (połowa różnicy):", half_range_disconnections)
print("Przedział ufności dla granicy komórek (połowa różnicy):", half_range_cell_boundaries)
