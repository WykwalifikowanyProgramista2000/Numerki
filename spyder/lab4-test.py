
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
    plt.axhline(y = 0, color = 'm')
    x1  = (a+b)/2
    plt.plot([a, b, x1], [0, 0, 0], 'bs')
    if math.fabs(myFun(x1)) <= Ex:
        return x1
    elif myFun(x1)*myFun(a) < 0:
        b = x1
    else:
        a = x1
    
    x1  = (a+b)/2
    plt.plot([a, b, x1], [0.2, 0.2, 0.2], 'g^')
    if math.fabs(myFun(x1)) <= Ex:
        return x1
    elif myFun(x1)*myFun(a) < 0:
        b = x1
    else:
        a = x1
    x1  = (a+b)/2
    plt.plot([a, b, x1], [0.4, 0.4, 0.4], 'ro')
    
    y  =[]
    x = np.linspace(-1, 1.0, 300)
    for i in x:
        y.append(myFun(i))
    plt.plot(x, y)
    plt.show()


def siecznych(x0, x1, n, Ex):
    
    y = []
    x = np.linspace(-5, 5, 300)
    for i in x:
        y.append(myFun(i))
    plt.plot(x, y)
    plt.plot([x0, x1], [0, 0], 'bs')
    plt.plot([x0, x1], [myFun(x0), myFun(x1)], 'b')
    plt.axhline(y = 0, color = 'm')
    plt.axis([-2, 1, -1, 8])
    
    if math.fabs(myFun(x1) - myFun(x0)) <= Ex:
        return x1
    x_temp = x1 - (myFun(x1)*(x1-x0)*1.0)/(myFun(x1) - myFun(x0))
    plt.plot([x_temp], [0], 'bs')
    x0 = x1
    x1 = x_temp
    plt.plot([x0, x1], [myFun(x0), myFun(x1)], 'r')
    
    if math.fabs(myFun(x1) - myFun(x0)) <= Ex:
        return x1
    x_temp = x1 - (myFun(x1)*(x1-x0)*1.0)/(myFun(x1) - myFun(x0))
    x0 = x1
    x1 = x_temp
    plt.plot([x0, x1], [myFun(x0), myFun(x1)], 'g')
    plt.plot([x_temp], [0], 'g^')


def stycznychNewtona(x0, E0, Ex):
    y = myFun(x0)
    yp = myFunPrime(x0)
    if abs(yp) < Ex:
        return None
    x1 = x0 - y/yp
    if abs(x0 - x1) <= E0:
        return x1
    x0 = x1
    stycznychNewtona(x0, E0, Ex)


bisekcja(-1, 0.5, 1.0e-6)
siecznych(-1, 0.4, 200, 1.0e-6)
stycznychNewtona(-4, 1.0e-6, 1.0e-6)