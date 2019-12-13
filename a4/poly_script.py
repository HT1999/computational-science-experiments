"""
Assignment 4
q1.c: Test script for Interpolation Curve
Author: Hassan Tariq, 100657119
"""

from set_t_values import set_t_values
from construct_pols import construct_pols

import matplotlib.pyplot as plt
import scipy

# set x and y according to table
x = [0, .5, 1.1, 1, .2]
y = [2, 2.5, 2.7, 2, 2.1]

# call functions from 1 a and b to create points to plot
t = set_t_values(x, y)              # call function from 1a to set t values
px, py = construct_pols(t, x, y)    # get interpolation points from 1b function

# plot curve on plane with interpolation points (smooth curve)
t = scipy.linspace(min(t), max(t))
plt.plot(x, y, 'p', px(t), py(t))  # plot curve itself over x and y
plt.xlabel("x")
plt.ylabel("y")
plt.title("Interpolating Curve")
plt.show()
