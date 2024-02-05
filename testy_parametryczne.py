import numpy as np
import scipy.stats as sps
data = np.loadtxt("files/Wzrost.csv", delimiter=',', skiprows=0, unpack=True)
data1 = np.loadtxt("files/Wzrost1.csv", delimiter=',', skiprows=0, unpack=True)
data2 = np.loadtxt("files/Wzrost2.csv", delimiter=',', skiprows=0, unpack=True)
test_jedna_proba = sps.ttest_1samp(data,176)
print(test_jedna_proba, data.mean(), data.std())
#proby nie zalezne
test_dwie_proba = sps.ttest_1samp(data1,176)
print(test_dwie_proba, data1.mean(), data1.std())
# proby zalezne
test_dwie_proba = sps.ttest_rel(data,176)
print(test_dwie_proba, data1.mean(), data1.std())

