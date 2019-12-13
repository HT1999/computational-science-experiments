"""
Assignment 3
q2.c: Intepolation points
Author: Hassan Tariq, 100657119
"""
import matplotlib.pyplot as plt
import scipy.linalg


yk = [0, 1, 5, 14, 35]                               # form vandermode matrix
n = len(yk)
xk = range(n)
vandermore = scipy.vander(xk, increasing=False)      # 5x5 vandermore matrix
interpolation = scipy.linalg.solve(vandermore, yk)   # linear system of interpolation


p = scipy.poly1d(interpolation)                      # interpolants points in the table
x = scipy.linspace(xk[1]-1, xk[-1]+1)                # create linspace for xk


#plot
plt.plot(yk, 's', x, p(x))
plt.xlabel("x")
plt.ylabel("y")
plt.title("Interpolation Points Plot")
plt.show()
