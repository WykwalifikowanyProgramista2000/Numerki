import matplotlib.pyplot as plt
import math
from typing import List
import numpy


# Zadanie 1

def myfun(x: float) -> float:
     return math.e**(-(x**2))


def simple_trapezoid_method(f, begin, end):
    return (end - begin)/2*(f(begin) + f(end))


def simple_rectangle_method(f, begin, end):
    return (end - begin)*f((begin+end)/2)


def simple_simson_method(f, begin, end):
    return (end - begin)/6*(f(begin) + 4 * f((begin - end)/2) + f(end))


def advanced_trapezoid_method(f, begin, end):
    ans = 0
    n = abs(end - begin)//1*10
    for i in range(0, n-1):
        x_i = begin + i*((end - begin)/n)
        x_i_1 = begin + (i+1)*((end - begin)/n)
        ans += (x_i_1 - x_i)/2 * (f(x_i) + f(x_i_1))
    return ans
    
    
def advanced_rectangle_method(f, begin, end):
    ans = 0
    n = abs(end - begin)//1*10
    for i in range(0 , n-1):
        x_i = begin + i*((end - begin)/n)
        x_i_1 = begin + (i+1)*((end - begin)/n)
        ans += f((x_i_1 - x_i)/2) * (x_i_1 - x_i)
    return ans


def advanced_simson_method(f, begin, end):
    ans = 0
    n = abs(end - begin)//1*10
    for i in range(0 , n-1):
        x_i = begin + i*((end - begin)/n)
        x_i_1 = begin + (i+1)*((end - begin)/n)
        ans += (x_i_1 - x_i)/6 * (f(x_i) + 4 * f((x_i_1 + x_i)/2) + f(x_i_1))
    return ans


def romberg_method(f, begin: float, end: float, precission: float):
    beginVal = f(begin)
    endVal = f(end)
    matrix = [[0],[0,0]]
    
    h = (end - begin)
    xList = [begin, begin + h]
    matrix[0][0] = 0.5*h*(beginVal + endVal)
    
    h = (end - begin)/2
    xList = [begin + k*h for k in range(0, 2+1)]
    matrix[1][0] = h*(sum([f(k) for k in xList])- 0.5*(beginVal + endVal))
    
    matrix[1][1] = matrix[1][0] + (matrix[1][0] - matrix[0][0])/(4-1)
    
    step = 2
    powerOf2 = 2*2
    while abs(matrix[step-1][step-1] - matrix[step-2][step-2]) > precission:
        matrix.append([0]*(step+1))
        
        h=(end-begin)/(powerOf2)
        elem = begin
        xList = []
        
        while elem <= end:
            xList.append(elem)
            elem += h
        
        matrix[step][0] = h*(sum([f(k) for k in xList])- 0.5*(beginVal + endVal))
                
        for col in range(1, step+1):
            matrix[step][col] = matrix[step][col-1] + (matrix[step][col-1] - matrix[step-1][col-1])/(4**col-1)
        
        step += 1
        powerOf2 *= 2
    
    return matrix[step-1][step-1]

a = 0
b = 1

print(simple_trapezoid_method(myfun, a, b))
print(simple_rectangle_method(myfun, a, b))
print(simple_simson_method(myfun, a, b))

print("advanced_trapezoid_method: {0}".format(advanced_trapezoid_method(myfun, a, b)))
print("advanced_rectangle_method: {0}".format(advanced_rectangle_method(myfun, a, b)))
print("advanced_simson_method:    {0}".format(advanced_simson_method(myfun, a, b)))
print("romberg method:            {0}".format(romberg_method(myfun, a, b, 10e-6)))

x = numpy.linspace(-0.5, 1)
y = myfun(x)
plt.plot(x, y)
