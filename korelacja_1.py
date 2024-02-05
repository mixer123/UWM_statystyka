import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as scs
import numpy as np
import seaborn

dane_mozgowe = pd.read_csv('files/brain_size1.csv', sep=';')
wsp_pearson = scs.pearsonr(dane_mozgowe['VIQ'], dane_mozgowe['PIQ'])
print('wsp korelacji liniowej dla PIQ, VIQ', wsp_pearson)

wsp_pearson = scs.pearsonr(dane_mozgowe['Weight'], dane_mozgowe['Height'])
print('wsp korelacji liniowej dla weight height', wsp_pearson)

# Macierz korelacji numpy
macierz = [dane_mozgowe['PIQ'], dane_mozgowe['VIQ'], dane_mozgowe['FSIQ'],dane_mozgowe['Weight'], dane_mozgowe['Height']]
macierz_korelacji = np.corrcoef(macierz).round(2)
print(macierz_korelacji)



# Macierz korelacji pandas
macierz = [dane_mozgowe['PIQ'], dane_mozgowe['VIQ'], dane_mozgowe['FSIQ'],dane_mozgowe['Weight'], dane_mozgowe['Height']]
macierz_df = dane_mozgowe[['PIQ','VIQ','FSIQ','Weight','Height']]
macierz_korelacji_df = macierz_df.corr().round(2)
print(macierz_korelacji_df)
seaborn.heatmap(macierz_korelacji_df, annot=True, cmap='jet')
plt.show()

