# Wczytaj plik regresja.xls (arkusz – zadanie2). Wyznacz zależność liczby dzieci od liczby małżeństw.
# (jeden predyktor). Wyznacz zależność liczby dzieci od pozostałych predyktorów

import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as scs
import numpy as np
dane_z_miesiace_df = pd.read_excel('files/regresja.xls', sheet_name='Zadanie2')