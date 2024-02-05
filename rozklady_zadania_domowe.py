import scipy.stats as scs
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as scs


# 1. Dla zmiennych losowych przedstawionych w tabelach obliczyć podstawowe statystyki
data = np.array([1, 2, 3,4,5,6])
print(data.min())
print(data.max())
print(data.mean())
print(data.std())
#
# 2. Wygeneruj próby dla n=100 dla następujących rozkładów: Bernoulliego, Dwumianowego, Poissona
n=100
size=100
k=2
mu=2
p=0.4
data = scs.bernoulli.rvs(p, size=size)
mean, var, skew, kurt = scs.bernoulli.stats(p, moments = 'mvsk')
print('Schemat Bernoulliego ',mean,var,skew,kurt)
print('schemat dwumianowy')
p_binom = scs.binom.rvs(n, p, size=size)
print(p_binom)
suma = 0
for k in range(n+1):
    p_k_n_binom = scs.binom.pmf(k,n,p)
    print(p_k_n_binom)
    suma += p_k_n_binom
print(suma)
print('Rozkald Poissona')
step = abs((scs.poisson.ppf(0.01, mu) -  scs.poisson.ppf(0.99, mu)))/100
print(step)
x = np.arange(scs.poisson.ppf(0.0001, mu), scs.poisson.ppf(0.999999, mu))
rv = scs.poisson(mu)
fig,ax = plt.subplots(1 ,1)
ax.vlines(x,0,rv.pmf(x), colors='b', linestyles='-', lw=1, label='frozenpmf')
ax.legend(loc='best', frameon=False)
plt.show()

# Policz dla nich statystyki podstawowe (średnią, wariancję, kurtozę i skośność).
# 3. Dla rozkładów Bernoulliego, Dwumianowego i Poissona narysuj wykres składający się z 3 części, gdzie
# każda część będzie zawierać wykres rozkładu prawdopodobieństwa
fig, ax = plt.subplots(1, 1)
x = np.linspace(sps.norm.ppf(0.01), sps.norm.ppf(0.99), 100)
print(x)
ax.plot(x, sps.norm.pdf(x), 'r-', lw=6, alpha=0.3, label='Normalny -teoretyczny')
# 4. Dla rozkładu Poissona wygeneruj rozkład prawdopodobieństwa dla n = 20, k = 0, ..., 20 oraz p = 0.4.
# Sprawdź, czy suma prawdopodobieństw wygenerowana dla rozkładu dwumianowego jest równa 1.
# 5. Wygeneruj 100 danych dla rozkładu normalnego o średniej równej 0 i odchyleniu standardowym
# równym 2. Wyznacz wszystkie statystyki podstawowe – czy są one równe z wartościami teoretycznymi?
# Sprawdź, czy zwiększenie liczby danych zwiększy dokładność wyliczeń statystyk opisowych.
# 6. Narysować na jednym wykresie histogram dla rozkładu normalnego o parametrach: średnia = 1,
# odchylenie =2, wykres dla rozkładu standardowego, oraz wykres gęstości dla średniej równej -1 oraz
# odchylenia równego 0.5.