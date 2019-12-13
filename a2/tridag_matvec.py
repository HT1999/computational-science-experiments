"""
Assignment 1
q2.c: Tridiagonal Matrix Product Vector Function
Author: Hassan Tariq, 100657119
"""
#define scipy to do array transformation
import scipy as sc

"""
TriMatProduct() inputs:
Vextor x (x), Diag Vectors (a), Diag Vectors (b), Diag Vectors (c)

TriMatProduct() output:
Scipy array of vector dot product
"""

def TriMatProduct(x, a, b, c):

    y = []
    k = len(a)

    for i in range(k):

        data = a[i] * x[i]              # run diagonal A every loop to initialize
                                        # data at that point
        if i < k - 1:
            data += b[i] * x[i+1]       # b diagonal

        if i < k - 2:
            data += c[i] * x[i+2]       # c diagonal

        y.append(data)                  # append data to final answer


    return sc.array(y)               # return as scipy for consistency with
                                        # scipy.dot(A) return type
