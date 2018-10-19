#%% Zadanie 1

def fib(n: int)->list:
    vect = [1, 1]
    if n <= 0:
        return None
    if n == 1:
        return [1]
    for i in range(n - 2):
        vect.append(vect[i] + vect[i + 1])
    return vect


vect = fib(4)
print(vect)
print(len(vect))


#%% Zadanie 2

from numpy import zeros
from random import randint

def customMatrix(m: int, n: int)->list:
    tempTab = zeros((m, n))
    if m > n:
        temp = m
    else:
        temp = n
    for j in range(m):
        for i in range(n):
            tempTab[j][i] = temp
    return tempTab


matrix = customMatrix(randint(3, 7), randint(3, 7))
print(matrix)


#%% Zadanie 3

from scipy.linalg import hilbert
from random import randint as rng

matrix = hilbert(3)


def myHilbert(n: int)->list:
    if n <= 0:
        return None
    if n == 1:
        return [1]
    temp = numpy.zeros((n,n), float)
    for j in range(n):
        for i in range(n):
            temp[j, i] = 1/(i+j+2-1)
    return temp
print(matrix)
print(myHilbert(3))

#%% Zadanie 4

import numpy
import scipy

matrix = numpy.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(matrix, "\n")
'''
lo_matrix = numpy.tril(matrix, 0)
print(lo_matrix, "\n")
'''
def myTril(matrix):
    for j in range(len(matrix)):
        for i in range(len(matrix)):
            if j > i:
                matrix[j, i] = 0
    return matrix

print(myTril(matrix), "\n")

'''
up_matrix = numpy.triu(matrix, 0)
print(up_matrix)
'''

def myTriu(matrix):
    for j in range(len(matrix)):
        for i in range(len(matrix)):
            if j < i:
                matrix[j, i] = 0
    return matrix

print(myTriu(matrix), "\n")

def myDiag(m: list)->list:
    return numpy.tril(numpy.triu(m))

di_matrix = myDiag(matrix)
print(di_matrix, "\n")


#%% Zadanie 5

import numpy

matrix = numpy.random.randint(3, 7, size = (3, 3))
print(matrix)

print("max: ", numpy.amax(matrix))
print("min: ", numpy.amin(matrix))
print("mean: ", numpy.mean(matrix))
'''
max_matrix = deepcopy(matrix)
min_matrix = deepcopy(matrix)
mean_matrix = deepcopy(matrix)

max_matrix.fill(numpy.amax(max_matrix))
min_matrix.fill(numpy.amin(min_matrix))
mean_matrix.fill(numpy.mean(mean_matrix))

print("max filled \n", max_matrix)
print("min filled \n", min_matrix)
print("mean filled \n", mean_matrix)
'''

#%% Zadanie 6

from numpy import multiply as mul
from numpy import array
from numpy import dot
from numpy import matmul

v1 = array([1, 3, 13])
v2 = array([8, 5, -2])

print(mul(v1, 4))
print(mul(-1,v2) + 2)
print()
print(mul(v1, v2))

#%% Zadanie 7






