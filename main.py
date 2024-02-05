import statistics

import numpy as np
import scipy.stats as scs
dane_zwzrostu=np.loadtxt('files/Wzrost.csv', delimiter=',')
print(dane_zwzrostu)
print('min', dane_zwzrostu.min())
print('min wzrost z numpy', np.min(dane_zwzrostu))
print('srednia', dane_zwzrostu.mean())
print('srednia wzrost z numpy', np.mean(dane_zwzrostu))
print('odchylenie', dane_zwzrostu.std())
print('odchylenie wzrost z numpy', np.std(dane_zwzrostu))

print('mediana wzrost z numpy', np.median(dane_zwzrostu))

print('min', dane_zwzrostu.min())
print('mediana wzrost z scipy', np.scoreapercentyle(dane_zwzrostu,100))
print('dominanta wzrostu', statistics.mode(dane_zwzrostu))

