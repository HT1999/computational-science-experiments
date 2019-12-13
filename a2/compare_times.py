"""
Assignment 2
q2.c q2.d: Plotting time taken vs Matrix size
Author: Hassan Tariq, 100657119
"""

#define libraries
from time import time
import scipy as sc
import matplotlib.pyplot as plt
from scipy import random
from scipy.sparse import diags
from tridag_matvec import TriMatProduct


resultFunc = sc.zeros((2,5))             # Holding time results of my function
resultBuiltFunc = sc.zeros((2,5))        # Holding time results of BUILT
                                         # IN function


for k in range(2, 5):                    # loop k = 2...7
    n = 10**k                            # set n = 10^k

    a = random.randint(1, 10, n)         # generate diagonals and vector
    b = random.randint(1, 10, n-1)
    c = random.randint(1, 10, n-2)
    x = random.randint(1, 10, n)

    start = time()
    ans = TriMatProduct(x, a, b, c)      # get product using tridag_matvec.py
    elapsed = time() - start
    print("My tridiagonal function elapsed time: ", elapsed)
    resultFunc[0,k] = elapsed
    resultFunc[1,k] = n

    A = diags([a, b, c], [0, 1, 2])      # from scipy.sparse create sparse
                                         # matrix for memory efficiency
    start = time()
    ans = sc.dot(A,x)                    # get product using built-in functions from Scipy
    elapsed = time() - start
    print("Scipy buit-in function elapsed time: ", elapsed)
    resultBuiltFunc[0,k] = elapsed
    resultBuiltFunc[1,k] = n


# Plot the two lines with labels and legend
plt.figure()
plt.semilogy(resultFunc[1,:], resultFunc[0,:], 'r-', resultBuiltFunc[1,:], resultBuiltFunc[0,:], 'b-')
plt.xscale('log')
plt.xlabel('Matrix size (nxn)')
plt.ylabel('Time in seconds')
plt.title('Time taken vs N size (Vector Multiplication)')
plt.legend(['My Tridiagonal Function', 'Scipy.dot Built-in Function'])
plt.show()
