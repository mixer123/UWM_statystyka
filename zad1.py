# 1, Ściągnij plik csv z https://extranet.who.int/tme/generateCSV.asp?ds=mdr_estimates.
# Zaimportuj wybraną
# kolumnę numeryczną z pliku do Pythona. Oblicz podstawowe statystyki dla zaimportowanych danych.
import statistics

import numpy as np
import pandas as pd

import scipy.stats as scs
from scipy.stats import scoreatpercentile
import matplotlib.pyplot as plt



data = pd.read_csv('files/estimates.csv', sep=',', na_values=".")
# print(data.e_rr_pct_new_lo)
data = data.e_rr_pct_new_lo
# print('min', data.min())
# print('min wzrost z numpy', np.min(data))
# print('srednia', data.mean())
# print('srednia wzrost z numpy', np.mean(data))
print('odchylenie', data.std())
# print('odchylenie wzrost z numpy', np.std(data))
# print('mediana wzrost z numpy', np.median(data))
# print('min', data.min())
# print('mediana wzrost z scipy', scoreatpercentile(data,100))
# print('dominanta wzrostu', statistics.mode(data))
#
#
#

# 2. Wgraj plik Wzrost.csv. Użyj dla niego funkcji z modułu statistics. Czym różnią się funkcje dotyczące wariancji
# i odchylenia standardowego?

# data = np.loadtxt('files/Wzrost.csv', delimiter=',')
# print(statistics.mean(data))
# print(statistics.median(data))
# print(statistics.stdev(data))

# 3. Znajdź dowolny plik csv. Zastosuj do niego statystyki z biblioteki scipy.stats. Sprawdź, jakie inne statystyki
# opisowe można znaleźć w tej bibliotece.
# 4. Załaduj plik brain_size.csv do pandas DataFrame. Znajdź średnią dla kolumny VIQ. Ile kobiet i mężczyzn jest
# wyróżnionych w pliku. Wyświetl histogramy dla zmiennych VIQ, PIQ, FSIQ. Wyświetl histogramy trzech
# kolumn tylko dla kobiet.

data = pd.read_csv('files/brain_size.csv', sep=';', na_values=".")
print(data['VIQ'].mean())
# ile kobiet
# dataframe[dataframe['Physics'] > 11]['Name'].count())
print(data[data['Gender']=='Female']['Gender'].count())
plotting.scatter_matrix(data[['VIQ','PIQ','FSIQ']])
plt.show()