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


#%% Zadanie 5

import math
import numpy as np
import matplotlib.pyplot as plt

def my8bitFloatPoint(num: list)->float:
    mantissa = 0
    exponent = 0
    base = 2
    for i in range(1, 5):
        mantissa += num[i]/(base**i)
    mantissa *= (-1) if num[0] == 1 else 1
    for i in range(7, 5, -1):
        exponent += num[i]*(2**(i-6))
    exponent *= (-1) if num[5] == 1 else 1
    return mantissa*(base**exponent)


def myFltPt()->list:
    temp = [[],[]]
    base = 2
    for j in range(1, 9):
        mantissaMax = 0
        mantissaMin = (1/(2**j))
        exponent = 3
        
        for i in range(1, j+1):
            mantissaMax += 1/(base**i)

        temp[0].append(mantissaMin*(base**(exponent*(-1))))
        temp[1].append(mantissaMax*(base**(exponent*(1))))
    return temp

aList = [1, 1, 1, 1, 0, 0, 1, 1]
print(my8bitFloatPoint(aList))

# Zakres
maxi = [0, 1, 1, 1, 1, 0, 1, 1]
mini = [0, 0, 0, 1, 1, 1, 1, 1]
num_0_2 = [0, 1, 1, 0, 0, 1, 1, 0]
print("a) Reprezentowany zakres to: <-", my8bitFloatPoint(maxi), ";-", my8bitFloatPoint(mini), "> + {0} + <", my8bitFloatPoint(mini), ";", my8bitFloatPoint(maxi), ">")
print("b) Blad niedomiaru dla 0.001:", math.fabs(0.001 - my8bitFloatPoint(mini)))
print("c) Blad nadmiaru dla 8:", math.fabs(8 - my8bitFloatPoint(maxi)))
print("d)\n  Blad zaokraglenia bezwzgledny to:", math.fabs(0.2 - my8bitFloatPoint(num_0_2)))
print("  Blad zaokraglenia wzgledny to:", math.fabs((0.2 - my8bitFloatPoint(num_0_2))/0.2))
print("e)")
fltpt = myFltPt()
for i in range(1, 9):
    print(i, "bit: <", fltpt[0][i-1], ";", fltpt[1][i-1], ">")
    
x = np.linspace(1, 8, 8)
plt.plot(x, fltpt[0])
plt.plot(x, fltpt[1])
plt.title("wartosci maksymalne i minimalne")
plt.xlabel("bity")
plt.ylabel("wartosc")
plt.show()
    
#%% Zadanie 6
    
import pylab as pl
import numpy as np
 
x = np.linspace(-np.pi/2+0.1, np.pi/2-0.1, 100)
y = np.tan(x)
pl.plot(x, y)
pl.show()

#%% Zadanie 7
import math
import matplotlib.pyplot as plt
import numpy as np

tab = []
bzw = []
wzg = []
pi = (math.sqrt((sum(1/(n**2) for n in range(1, 10000)))*6))

for i in range(1, 101):
    tab.append((math.sqrt((sum(1/(n**2) for n in range(1, i)))*6)))
    bzw.append(math.fabs(tab[i-1] - math.pi))
    wzg.append(bzw[i-1]/math.pi)

x = np.linspace(1, 100, 100)
plt.show()
plt.plot(x, bzw)
plt.legend("bezwzgledne")
plt.plot(x, wzg)
plt.legend("wzgledne")
plt.xlabel("n")
plt.ylabel("blad")
#%% test

(0.5)*(2**(-3))