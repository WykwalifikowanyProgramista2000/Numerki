import numpy as np
import math
import matplotlib.pyplot as plt

def fun(x):
    return 1/(25*(x**2) + 1)

'''
def myLagrange(xi: list, yi: list, data: list):
    wyn = [0]*len(data)
    for j in range(len(yi)):
        wzr = yi[j]
        for i in range(len(xi)):
            if xi[i] - xi[j] != 0:
                wzr *= (data - xi[i])/(xi[j] - xi[i])
        wyn = wyn + wzr
    return wyn
'''

def myLagrange(xi, yi):
    def P(x):
        ansP = 0
        for i in range(len(xi)):
            def wiel(i):
                ans = 1
                for j in range(len(xi)):
                    if xi[i] != xi[j]:
                        ans *= (x - xi[j])/(xi[i] - xi[j])
                return ans
            ansP += yi[i] * wiel(i)
        return ansP
    return P
            
def plot(f):
	x = range(-10, 100)
	y = map(f, x)
	print (y)
	plt.plot( x, y, linewidth=2.0)            
            
            

    
data = np.linspace(-1, 1, 100)

k = np.linspace(-1, 1, 10)

knots = np.cos((math.pi*k)/10)
#knots = k
knots_value = fun(k)

P = myLagrange(knots, knots_value)

y = []

for i in data:
    y.append(fun(i))

plt.plot(data, y)
#plot(P)
