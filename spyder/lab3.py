#%% Zadanie 1
b = 1.123456789*10**16

P1 = b - 1/(1/b) + 0.1
P2 = b + 0.1 - 1/(1/b)

#%% Zadanie 2
import numpy as np
import math
import matplotlib.pyplot as plt

def Gp(n: int)->list:
    temp = []
    for p in range(1, n+1):
        temp.append((1/p)*((10**p)*(1+p*np.round(math.pi, 15)*(10**(-p)))-(10**p)))
    return np.array(temp)

wyn = Gp(15)
bez = []
wzg = []

def fbez(wyn: list)->list:
    temp = []
    for i in range(len(wyn)):
        temp.append(math.fabs(wyn[i] - math.pi))
    return list(temp)


def fwzg(wyn: list)->list:
    temp = []
    for i in range(len(wyn)):
        temp.append(math.fabs((wyn[i] - math.pi)/math.pi))
    return list(temp)


bez = fbez(wyn)
wzg = fwzg(wyn)

n = np.linspace(0, 14, 15)
plt.semilogy(n, list(bez))
plt.legend("bezwzględny")
plt.xlim(left = 0)
plt.xlim(right = 15)
plt.xlabel("n")
plt.ylabel("błąd")
plt.semilogy(n, list(wzg))
plt.legend("względny")
plt.title("wykres błędów bezwzględnych i względnych")


#%% Zadanie 3

import math

def myE(stop: int)->float:
    temp = 0
    for n in range(0, stop):
        temp += 1/math.factorial(n)
    return temp

bez5 = math.fabs(math.e - myE(5))
bez10 = math.fabs(math.e - myE(10))
wzg5 = math.fabs((math.e - myE(5))/math.e)
wzg10 = math.fabs((math.e - myE(10))/math.e)

print("\nmath.e:", math.e)
print("Dla n = 5 :\ne = ", myE(5), "Błędy:\n___Bezwzględny:", bez5, "\n___Względny:", wzg5)
print("Dla n = 10 :\ne = ", myE(10), "Błędy:\n___Bezwzględny:", bez10, "\n___Względny:", wzg10)


#%% Zadanie 4

import math

def myE_power_x(stop: int, x: float)->float:
    temp = 0
    for i in range(0, stop):
        temp += (1/math.factorial(i))*x**i
    return temp

print("\n")
print("myE_poewr_x(10, 3):", myE_power_x(10, 3))
print("math.exp(3)", math.exp(3))
print("Błąd bezwzględny myE_power_x(100, 3):", math.fabs(math.e**3 - myE_power_x(100, 3)))
print("Błąd bezwzględny math.exp(3):", math.fabs(math.e**3 - math.exp(3)))

