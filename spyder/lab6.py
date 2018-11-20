import math
import numpy as np
import matplotlib.pyplot as plt
import scipy.interpolate as inter

def fun(x):
    return 1/(25*(x**2) + 1)

def fun_p(x):
    return -((50*x)/((25*(x**2) + 1)**2))


def splajn_1(xk: list, yk: list, xnew: list)->list:
    y = []
    for k in range(len(xk)-1):
        for x in xnew:
            if x >= xk[k] and x<= xk[k+1]:
                y.append(yk[k] + ((yk[k+1]-yk[k])*(x - xk[k]))/(xk[k+1]-xk[k]))
    return y

       
def p(i, data, x):
    n = 1
    for j in np.arange(i):
        n *= (data - x[j])
    return n


def a(i, j, x, y):
    if i == 0:
        return y[0]
    elif i - j == 1:
        return (y[i] - y[j])/(x[i] - x[j])
    else:
        return (a(i, j+1, x, y) - a(i-1, j, x, y))/(x[i]-x[j])


def myNewton(data, x, y):
    Nn = 0
    for i in range(len(x)):
        Nn += a(i, 0, x, y) * p(i, data, x)
    return Nn       
        


#%% Funkcja Interpolowana
x0 = np.linspace(-1.5, 1.5, 1000)
y0 = fun(x0)
plt.plot(x0, y0)
plt.title('Wykres funkcji interpolowanej')
plt.show()

#%% Węzły interpolacji i ich wartoci
k1 = np.linspace(-1, 1, 20)
knots_value = fun(k1)

#%% Biblioteczny slajn st.1
x1 = np.linspace(-1, 1, 1000)
y1 = inter.spline(k1, knots_value, x1, order=1)

plt.plot(x1, y1)
plt.title("biblioteczny splajn")
plt.show()

#%% Mój splajn st.1
y2 = splajn_1(k1, knots_value, x1)

plt.plot(x1, y2)
plt.title("Mój_splajn_1")
plt.show()

#%% Porównanie mojego splajnu st.1 i splajnu bibliotecznego st.1
data = np.linspace(-1, 1, 1000)

bledy_splajnu_bibliotecznego = abs(y0 - y1)
bledy_splajnu_mojego = abs(y0 - y2)

plt.plot(data, bledy_splajnu_bibliotecznego, color='red')
plt.plot(data, bledy_splajnu_mojego, color='green')
plt.show()


#%% ZADANIE 5 Porównanie interporacji splajnem st.1, st.3 i interpolacją newtona
data = np.linspace(-1, 1, 1000)
data_value = fun(data)
knots = np.linspace(-1, 1, 20)
knots_value = fun(knots)

y0 = inter.spline(knots, knots_value, data, order=1)
y1 = inter.spline(knots, knots_value, data, order=3)
y2 = myNewton(data, knots, knots_value)

plt.plot(data, y0, color='green')
plt.plot(data, y1, color='red')
plt.plot(data, y2, color='purple')
plt.title("Porównanie wyników dla wszystkich trzech interpolacji")
plt.ylim(-0.3, 1.5)
plt.show()

bledy_bibl_spline_1 = abs(data_value - y0)
bledy_bibl_spline_3 = abs(data_value - y1)
bledy_myNewton = abs(data_value - y2)

plt.plot(data, bledy_bibl_spline_1)
plt.title("Bledy dla splanu bibliotecznego st.1")
plt.show()

plt.plot(data, bledy_bibl_spline_3)
plt.title("Bledy dla splanu bibliotecznego st.3")
plt.show()

plt.plot(data, bledy_myNewton)
plt.title("Bledy dla mojej Interpolacji Newtona")
plt.show()

#%% ZADANIE 6

y1p = inter.InterpolatedUnivariateSpline(knots, knots_value,  k=1).derivative()
y3p = inter.InterpolatedUnivariateSpline(knots, knots_value,  k=3).derivative()

bledy_pochodnej_splajnu_1 = abs(y1p(data) - fun_p(data))
bledy_pochodnej_splajnu_3 = abs(y3p(data) - fun_p(data))

plt.plot(data, fun_p(data), color='red')
plt.title("Pierwsza pochodna badanej funkcji\n")
plt.plot(data, y1p(data), color='orange')
plt.title("Pierwsza pochodna splajnu st.1\n")
plt.plot(data, y3p(data))
plt.title("Pierwsza pochodna splajnu st.3\n", color='green')
plt.show()

plt.plot(data, bledy_pochodnej_splajnu_1)
plt.title("Bledy pierwszej pochodnej splajnu st.1")
plt.show()

plt.plot(data, bledy_pochodnej_splajnu_3)
plt.title("Bledy pierwszej pochodnej splajnu st.3")
plt.show()




