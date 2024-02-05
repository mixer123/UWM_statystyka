# Wczytaj plik napoje.csv. Zbadaj czy istnieje zależność między spożyciem poszczególnych napojów

import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as scs
import numpy as np


dane_z_miesiace_df = pd.read_csv('files/napoje.csv', sep=';', encoding_errors= 'replace')
# print(list(dane_z_miesiace_df.columns[6:18]))
print('Korelacja miedzy napojami')
macierz_df = dane_z_miesiace_df[list(dane_z_miesiace_df.columns[2:])]
macierz_korelacji_df = macierz_df.corr().round(2)
print(macierz_korelacji_df)