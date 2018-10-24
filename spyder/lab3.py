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
#print(wyn, "XXX", len(wyn))

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

#print("bez:", bez, "\nwzg:", wzg)


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
    for n in range(1, stop+1):
        temp += 1/math.factorial(n)
    return temp

bez5 = math.fabs(math.e - myE(5))
bez10 = math.fabs(math.e - myE(10))
wzg5 = math.fabs((math.e - myE(5))/math.e)
wzg10 = math.fabs((math.e - myE(10))/math.e)

print("Błędy dla n = 5 to:\n___Bezwzględny:", bez5, "\n___Względny:", wzg5)
print("Błędy dla n = 10 to:\n___Bezwzględny:", bez10, "\n___Względny:", wzg10)


#%% Zadanie 4























