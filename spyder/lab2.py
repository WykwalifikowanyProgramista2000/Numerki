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
import numpy as np

matrix = hilbert(3)


def myHilbert(n: int)->list:
    if n <= 0:
        return None
    if n == 1:
        return [1]
    temp = np.zeros((n,n), float)
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
import copy

v1 = array([1, 3, 13])
v2 = array([8, 5, -2])
v3 = copy.deepcopy(v1)

print(dot(v1, 4), "\n")
print(dot(-1,v2) + 2, "\n")
print(matmul(v1,v2), "\n")    
print(mul(v1, v2), "\n")

'''
t1 = [[1, 0], [0, 1]]
t2 = [[4, 1], [2, 2]]

print(matmul(t1, t2), "\n")
print(mul(t1, t2), "\n")
'''

#%% Zadanie 7
import numpy as np
m1 = array([[1, -7, 3], [-12, 3, 4], [5, 13, -3]])

v2 = array([8, 5, -2])

print(dot(3, m1))
print(dot(3, m1) + 1, "\n")

def myTransNxN(m: list)->list:
    temp = array([[0]*len(m[0])]*len(m))
    print(temp, "\n")
    for j in range(0, len(m)):
        for i in range(0, len(m[j])):
            temp[j][i] = m[i][j]

    return array(temp)

v2 = v2[np.newaxis]
print(m1, "\n")
print(myTransNxN(m1), "\n")
print(matmul(m1, v1), "\n")
print(mul(v2.T, m1), "\n")
#%% Zadanie 8
from numpy.linalg import det

def solveM(wsp, wyn)->list:
    mx = [0]*(len(wyn)+1)
    mx[len(wyn)] = det(wsp)
    for i in range(len(wsp)):
        for j in range(len(wsp[i])):
            wsp[j][i], wyn[j] = wyn[j], wsp[j][i]
            
        #print("#", det(wsp), "\n", wsp, "\n##", mx[3])
              
        mx[i] = det(wsp)/mx[len(wyn)]
        for j in range(len(wsp[i])):
            wsp[j][i], wyn[j] = wyn[j], wsp[j][i]
    return list(mx[:-1])

wspolczynniki = array([[1, 3, 2], [-1, 2, 3], [8, 2, -3]])
wyniki = array([7, -2, 28])

print(solveM(wspolczynniki, wyniki))
#%% Test
        
m = [[0]*3]*3

temp = array([[7, 3, 2], [-2, 2, 3], [28, 2, -3]])
print(det(wspolczynniki))
print(det(temp))
print(det(temp)/det(wspolczynniki))





