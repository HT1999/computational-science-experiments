"""
Assignment 3
q1.d: Hessenberg PLU decomposition pseduo code implemented
Author: Hassan Tariq, 100657119
"""

import math
import scipy
import copy

def Hess_LUP(A):
    ok = False                                    # set to True if we encounter division by 0
    small = 1e-12                                 # pivots smaller than this are considered 0
    n = scipy.shape(A)[0]                         # initialize L, U and P
    U = copy.copy(A)
    L = scipy.identity(n)
    P = scipy.identity(n)

    for j in range(n-1):                          # loop over columns n times

        """
        Find the largest number in column below diagonal, the diagonals under j+1 are
        not nessecary since A is a Hessenberg matrix and all values under subdiagonal
        are 0's.
        """
        if U[j, j] < U[j + 1, j]:
            U = swap(U,j,j+1,n)                   # if the largest number is not on the diagonal, swap rows
            P = swap(P,j,j+1,n)
            if j>0:
                L = swap(L,j,j+1,j)

        if abs(U[j, j]) < small:                 # check for zero pivot (nearly singular matrix)
            print("Near-zero pivot!")
            ok = True                                # encounter division by 0
            break

        """
        Gaussian elimination only nessecary on subdiagonal below main diagonal
        since under the subdiagonal the values are already 0. Doing Gaussian
        elimination on only this subdiagonal decreases flop count.
        """
        L[j + 1, j] = U[j + 1, j] / U[j, j]
        U[j + 1, j:n] = U[j + 1, j:n] - L[j + 1, j] * U[j, j:n]

    return L,U,P,ok

def swap(M,i,j,k):
    # Swap rows i and j from column 0 up to (not including) k
    dum = copy.copy(M[i,0:k])
    M[i,0:k] = copy.copy(M[j,0:k])
    M[j,0:k] = copy.copy(dum)
    return M
