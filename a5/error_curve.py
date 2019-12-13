"""
Assignment 5
q1.c: Script for error
Author: Hassan Tariq, 100657119
"""

import matplotlib.pyplot as plt
import scipy.interpolate

# define function
def f(x):
    return scipy.log((x + 2) / (x + 1))

x1 = scipy.array([0, 1, 3])                    # interpolation points of 0,1,3
maxError = []                                  # max error array


for k in range(3, 101):                        # range from 3 to 100
    xk = scipy.linspace(0, 3, k)               # equidistant grid with k nodes
    p = scipy.interpolate.lagrange(xk, f(xk))  # interpolation points
    x = scipy.linspace(x1[-1], x1[0], 1000)    # fine grid
    maxError += [max(abs(f(x) - p(x)))]        # max of |f(x)-p(x)|

plt.semilogy(maxError)                         # plot on log scale
plt.xlabel("K nodes (3 to 100)")
plt.ylabel("Error")
plt.title("Error as a function of K")
plt.show()
