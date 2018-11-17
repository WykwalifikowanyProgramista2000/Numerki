#%% Bisekcja
import math
import numpy as np
import matplotlib.pyplot as plt

def myFun(x)->float:
    return (math.e**((-2)*x))+(x**2)-1


def myFunPrime(x)->float:
    return (2*x - 2*math.e**((-2)*x))


def myFunBis(x)->float:
    return (4*math.e**(-2*x)+2)
    


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


def stycznychNewtona(x0, E0, Ex):
    for i in range(64):
        y = myFun(x0)
        yp = myFunPrime(x0)
        if abs(yp) < Ex:
            return None
        x1 = x0 - y/yp
        if abs(x0 - x1) <= E0:
            return x1
        x0 = x1
        stycznychNewtona(x0, E0, Ex)
    return None
        


bis = ['miejsca zerowe bisekcją:', bisekcja(-1, 0.5, 1.0e-6), bisekcja(0.5, 1.5, 1.0e-6)]
sie = ['miejsce zerowe siecznych', siecznych(-0.5, 0.4, 200, 1.0e-6), siecznych(0.5, 1.5, 200, 1.0e-6)]
sty = ['miejsce zerowe stycznych', stycznychNewtona(-4, 1.0e-6, 1.0e-6), stycznychNewtona(1, 1.0e-6, 1.0e-6)]

print(bis, '\n', sie, '\n', sty)


y=[]
x = np.linspace(0.8, 1.0, 300)
for i in x:
    y.append(myFun(i))
plt.plot(x, y)
plt.axhline(y = 0, color = 'r')
plt.show()

y=[]
x = np.linspace(-0.2, 0.2, 300)
for i in x:
    y.append(myFun(i))
plt.plot(x, y)
plt.axhline(y = 0, color = 'r')
plt.show()

y0, y1, y2 = [], [], []
x = np.linspace(-0.2, 1.0, 300)
for i in x:
    y0.append(myFun(i))
    y1.append(myFunPrime(i))
    y2.append(myFunBis(i))
plt.plot(x, y0, color= 'r')
plt.legend('f')
plt.plot(x, y1, color= 'g')
plt.legend("f'")
plt.plot(x, y2, color= 'b')
plt.legend("f''")
plt.axhline(y = 0, color = 'm')
plt.xlabel('x')
plt.ylabel('y')
plt.title("Funkcja f, f', f''")






