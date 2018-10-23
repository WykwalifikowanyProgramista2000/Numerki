#%% Zadanie 1
b = 1.123456789*10**16

P1 = b - 1/(1/b) + 0.1
P2 = b + 0.1 - 1/(1/b)

#%% Zadanie 2

import numpy as np
import math
import matplotlib.pyplot as plt

def GG(n: int)
def Gp(n: int)->list:
    temp = []
    for p in range(1, n+1):
        temp.append((1/p)*((10**p)*(1+p*np.round(pi, 15)*(10**(-p)))-(10**p)))
    return np.array(temp)

wyn = Gp(15)
print(Gp(15), "XXX", len(wyn))


#%% Zadanie 3

bez = []
wzg = []

def fbez(wyn: list)->list:
    temp = []
    for i in range(len(wyn)):
        temp.append(math.fabs(wyn[i] - math.pi))
    return temp


def fwzg(wyn: list)->list:
    temp = []
    for i in range(len(wyn)):
        temp.append(math.fabs((wyn[i] - math.pi)/math.pi))
    return temp

bez = fbez(wyn)
wzg = fwzg(wyn)

x = np.linspace(0, 14)
plt.plot(x, list(bez))
plt.semilogy(y)
plt.show()


