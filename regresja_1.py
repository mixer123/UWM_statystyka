import sklearn.linear_model as sl
import numpy as np

# metraż mieszkania
x = [[25, 1, 0], [40, 1, 0], [80, 1, 0], [100, 1, 0], [55, 1, 0],
     [20, 0, 1], [30, 0, 1], [50, 0, 1], [70,  0, 1], [80, 0, 1], [95,  0, 1]]
# cena mieszkania
y = [200, 315, 620, 860, 500, 240, 380, 620, 900, 1000, 1200]

x = np.array(x)
y = np.array(y)
print(x)
print(y)

# chcemy równanie y = ax+b
model_regresji_mieszkania = sl.LinearRegression()
model_regresji_mieszkania.fit(x, y)
wspolczynnik_a = model_regresji_mieszkania.coef_
wspolczynnik_b = model_regresji_mieszkania.intercept_
print(wspolczynnik_a[0])
print(wspolczynnik_a[1])
print(wspolczynnik_a[2])
print('Równanie regresji dla cen mieszkań na podstawie metrażu ma postać:')
print('y='+str(wspolczynnik_a[0].round(2))+'*x1+'+str(wspolczynnik_a[1].round(2))+'*x2+'\
+str(wspolczynnik_a[2].round(2))+'*x3+'+str(wspolczynnik_b.round(2)))

prognoza_ceny_mieszkania_warszawa = model_regresji_mieszkania.predict([[70,0,1]])
print('Prognozowana cena mieszkania Warszawa to:', prognoza_ceny_mieszkania_warszawa)
prognoza_ceny_mieszkania_olsztyn = model_regresji_mieszkania.predict([[70,1,0]])
print('Prognozowana cena mieszkania Olsztyn to:', prognoza_ceny_mieszkania_olsztyn)
R_sq = model_regresji_mieszkania.score(x, y)
print('Współczynnik determinacji:', R_sq)



from sklearn.ensemble import RandomForestRegressor
model_regresji_rf = RandomForestRegressor()
model_regresji_rf.fit(x,y)
R_sq_rf = model_regresji_rf.score(x,y)