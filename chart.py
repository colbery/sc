# import matplotlib.pyplot as plt
# import pandas as pd
# import glob
# import numpy as np

# # Funkcja do wczytywania danych z plików CSV i tworzenia wykresu
# def generate_plots():
#     # Pobierz wszystkie pliki CSV w bieżącym katalogu, które pasują do wzorca '?.csv'
#     csv_files = glob.glob('[1-10].csv')
    
#     # Filtruj pliki, aby uwzględnić tylko te, które są nazwane '1.csv', '2.csv', ..., '10.csv'
#     csv_files = [file for file in csv_files if file.split('.')[0].isdigit() and int(file.split('.')[0]) in range(1, 11)]
    
#     # Inicjalizuj listy do przechowywania danych z każdego pliku
#     all_removed_users = []
#     all_users_in_system = []
    
#     # Wczytaj dane z każdego pliku CSV
#     for file in csv_files:
#         data = pd.read_csv(file)
#         all_removed_users.append(data['Removed Users'].values)
#         all_users_in_system.append(data['Users in System'].values)
    
#     # Konwersja list na tablice numpy
#     all_removed_users = np.array(all_removed_users)
#     all_users_in_system = np.array(all_users_in_system)
    
#     # Uśrednianie danych
#     avg_removed_users = np.mean(all_removed_users, axis=0)
#     avg_users_in_system = np.mean(all_users_in_system, axis=0)
    
#     # Rysowanie wykresu
#     plt.figure(figsize=(10, 6))
#     plt.plot(avg_removed_users, avg_users_in_system, label='Średnia z 10 symulacji')
    
#     plt.xlabel('Liczba rozłączonych użytkowników')
#     plt.ylabel('Liczba użytkowników w systemie')
#     plt.title('Średnia liczba użytkowników w systemie vs Liczba rozłączonych użytkowników')
#     plt.legend()
#     plt.grid(True)
    
#     # Ustawienie kroków osi X na co 5
#     plt.xticks(np.arange(0, max(avg_removed_users) + 1, 5))
    
#     plt.show()

# # Wywołaj funkcję do generowania wykresów
# generate_plots()
