#%% Bisekcja
import math
import numpy as np
import matplotlib.pyplot as plt

def myFun(x)->float:
    return (math.e**((-2)*x))+(x**2)-1
    


def bisekcja(a: float, b: float, Ex: float)->float:
    while math.fabs(a - b) > Ex:
        x1  = (a+b)/2
        
        if math.fabs(myFun(x1)) <= Ex:
            return x1
        elif myFun(x1)*myFun(a) < 0:
            b = x1
        else:
            a = x1
    return ((a+b)/2)


def siecznych(x0, x1, n, Ex):
    for i in range(n):
        if math.fabs(myFun(x1) - myFun(x0)) <= Ex:
            return x1
        x_temp = x1 - (myFun(x1)*(x1-x0)*1.0)/(myFun(x1) - myFun(x0))
        x0 = x1
        x1 = x_temp
    return x1


def stycznychNewtona(f, df, x0, e):
    delta = dx(f, x0)
    while delta > e:
        x0 = x0 - f(x0)/df(x0)
        delta = dx(f, x0)
    print ('root is at)


bis = ['miejsca zerowe bisekcją:', bisekcja(-1, 0.5, 1.0e-6), bisekcja(0.5, 1.5, 1.0e-6)]
sie = ['miejsce zerowe siecznych', siecznych(-0.5, 0.4, 200, 1.0e-6), siecznych(0.5, 1.5, 200, 1.0e-6)]

print(bis, '\n', sie)


y=[]
x = np.linspace(0.5, 1.2, 300)
for i in x:
    y.append(myFun(i))
plt.plot(x, y)
plt.axhline(y = 0, color = 'r')
