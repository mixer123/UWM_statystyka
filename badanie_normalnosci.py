import numpy as np
import scipy.stats as sps
import pandas
data = np.loadtxt("files/Wzrost.csv", delimiter=',', skiprows=0, unpack=True)
test_results = sps.normaltest(data)
print(test_results)