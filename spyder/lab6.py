import math
import numpy as np
import matplotlib.pyplot as plt
import scipy.interpolate as inter

def fun(x):
    return 1/(25*(x**2) + 1)


def splajn_1(xk: list, yk: list, xnew: list)->list:
    y = []
    for k in range(len(xk)-1):
        for x in xnew:
            if x >= xk[k] and x<= xk[k+1]:
                y.append(yk[k] + ((yk[k+1]-yk[k])*(x - xk[k]))/(xk[k+1]-xk[k]))
    return y
       # print("x_k = {0}, x_k+1 = {1}".format(xk0, xk1))
        


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














