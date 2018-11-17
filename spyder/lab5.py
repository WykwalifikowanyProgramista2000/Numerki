import numpy as np
import math

def fun(x):
    return 1/(x**2 + 1)


def myLagrange(xi: list, yi: list, data: list):
    

    
data = np.linspace(-1, 1, 1000)

k = np.linspace(-1, 1, 10)

knots = np.cos((math.pi*k)/10)
knots_value = fun(k)

myLagrange(knots, knots_value, data)

