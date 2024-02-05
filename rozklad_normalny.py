import scipy.stats as scs
import numpy as np
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as sps

import scipy.stats as scs
fig, ax = plt.subplots(1, 1)
x = np.linspace(sps.norm.ppf(0.01), sps.norm.ppf(0.99), 100)
print(x)
ax.plot(x, sps.norm.pdf(x), 'r-', lw=6, alpha=0.3, label='Normalny -teoretyczny')
rv = sps.norm(loc = 0, scale = 1)
ax.plot(x, rv.pdf(x), 'k-', lw=3, label='Normalny – z próby')
rv = sps.norm(loc = 0, scale = 0.5)
ax.plot(x, rv.pdf(x), 'g--', lw=9, label='Normalny – z próby')
ax.legend(loc='best')
plt.show()