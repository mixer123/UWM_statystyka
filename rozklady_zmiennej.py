import scipy.stats as scs
import numpy as np
import matplotlib.pyplot as plt
#Rozkład Bernoulliego
import scipy.stats as scs
p = 0.3
size = 10
n=20
k=2
mu=2
data = scs.bernoulli.rvs(p, size=size)
mean, var, skew, kurt = scs.bernoulli.stats(p, moments = 'mvsk')
# print(data)
statystyki = scs.describe(data)
print('parametry dla rozkładu Bernoulliego', statystyki[2], statystyki[3],statystyki[4],statystyki[5])
print('parametry dla rozkładu teoretycznego', mean , var, skew, kurt)
#rozkład dwumianowy prawdopodob. k sukcesów w n próbach
p_binom = scs.binom.rvs(n, p, size=size)
print(p_binom)
suma = 0
for k in range(n+1):
    p_k_n_binom = scs.binom.pmf(k,n,p)
    print(p_k_n_binom)
    suma += p_k_n_binom
print(suma)
# rozklad Poissona
x = np.arange(scs.poisson.ppf(0.01, mu), scs.poisson.ppf(0.99, mu))
rv = scs.poisson(mu)
fig,ax = plt.subplots(1 ,1)
ax.vlines(x,0,rv.pmf(x), colors='b', linestyles='-', lw=1, label='frozenpmf')
ax.legend(loc='best', frameon=False)
plt.show()


