"""
Assignment 5
q1.1: Script for intepolation curve and error
Author: Hassan Tariq, 100657119
"""
import matplotlib.pyplot as plt
import scipy.interpolate

# define function
def f(x):
    return scipy.log((x + 2) / (x + 1))

x1 = scipy.array([0.0, 1.0, 3.0])                    # interpolation points of 0,1,3
p = scipy.interpolate.lagrange(x1, f(x1))            # find second order of x_1

x_diff = x1[-1] - x1[0]                              # find difference to create linspace
x = scipy.linspace(0, 3)                             # create x intervals
error = abs(f(x) - p(x))


# plot function and the interpolant
plt.plot(x1, f(x1), 's',                             # interpolation points
         x, f(x),                                    # function points
         x, p(x))                                    # interpolant curve
plt.xlabel("x")
plt.ylabel("y")
plt.title("Interpolating Curve")
plt.legend(['Interpolating points',
            'f(x)',
            'Interpolant'])
plt.show()


# plot the interpolation error
plt.plot(x, error)                                   # interpolation error points
plt.xlabel("x")
plt.ylabel("y")
plt.title("Interpolation Error")
plt.legend(['error'])
plt.show()
