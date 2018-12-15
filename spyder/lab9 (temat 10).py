# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 17:15:49 2018

@author: Wojti
"""
from numpy import transpose
from numpy.linalg import eig, inv
from scipy.linalg import hilbert

A = numpy.array([
        [1, 8, 2],
        [-20, 12, 0],
        [-3, 5, 17]
        ])

Aa = [
        [1, 8, 2],
        [-20, 12, 0],
        [-3, 5, 17]
        ]

b = numpy.array([
        [44],
        [8],
        [99]
        ])

H = hilbert(5)


def RowNorm(ar):
    temp = 0
    ar = abs(ar)
    for row in ar:
        if temp < sum(row):
            temp = sum(row)
    return temp
        

def ColNorm(ar):
    temp = transpose(A)
    return RowNorm(temp)


def SpectralNorm(ar):
    return max(abs(eig(ar)[0]))
    

def W_u(ar, nor_s):
    return (nor_s(ar) * nor_s(inv(ar)))    

def gauss(A):
    n = len(A)

    for i in range(0, n):
        # Search for maximum in this column
        maxEl = abs(A[i][i])
        maxRow = i
        for k in range(i+1, n):
            if abs(A[k][i]) > maxEl:
                maxEl = abs(A[k][i])
                maxRow = k

        # Swap maximum row with current row (column by column)
        for k in range(i, n+1):
            tmp = A[maxRow][k]
            A[maxRow][k] = A[i][k]
            A[i][k] = tmp

        # Make all rows below this one 0 in current column
        for k in range(i+1, n):
            c = -A[k][i]/A[i][i]
            for j in range(i, n+1):
                if i == j:
                    A[k][j] = 0
                else:
                    A[k][j] += c * A[i][j]

    # Solve equation Ax=b for an upper triangular matrix A
    x = [0 for i in range(n)]
    for i in range(n-1, -1, -1):
        x[i] = A[i][n]/A[i][i]
        for k in range(i-1, -1, -1):
            A[k][n] -= A[k][i] * x[i]
    return x

row_norm = RowNorm(A)
col_norm = ColNorm(A)
spec_norm = SpectralNorm(A)

Ws = W_u(A, SpectralNorm)
Wr = W_u(A, ColNorm)
Wc = W_u(A, RowNorm)

Ws_h = W_u(H, SpectralNorm)
Wr_h = W_u(H, ColNorm)
Wc_h = W_u(H, RowNorm)

ans = gauss(Aa)












