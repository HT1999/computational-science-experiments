"""
Assignment 3
q1.d: Hessenberg PLU decomposition test script
Author: Hassan Tariq, 100657119
"""

from time import time
import scipy as sc
import matplotlib.pyplot as plt
from scipy import random
from scipy.sparse import diags
from Hess_LUP import Hess_LUP


resultFunc = sc.zeros((4,11))            # Holding time results of my function
resultBuiltFunc = sc.zeros((4,11))       # Holding time results of BUILT
                                         # IN function


for p in range(4, 11):                   # loop p = 4...11
    n = 2**p                             # set n = 2^p
    A = sc.triu(sc.random.randint(1, 10, (n, n)), -1) # hessenberg random
    start = time()
    ans = Hess_LUP(A)                    # get product using tridag_matvec.py
    elapsed = time() - start
    print("My tridiagonal function elapsed time: ", elapsed)
    resultFunc[0,p] = elapsed
    resultFunc[1,p] = n




# Plot the line on log scale
plt.figure()
plt.semilogy(resultFunc[1,:], resultFunc[0,:], 'r-')
plt.xscale('log')
plt.xlabel('Matrix size')
plt.ylabel('Time in seconds')
plt.title('Time taken vs Hessenberg size')
plt.show()
