"""
Assignment 4
q1.d: Cubic interpolation visualization
Author: Hassan Tariq, 100657119
"""

from set_t_values import set_t_values
from construct_pols import construct_pols

import matplotlib.pyplot as plt
import scipy

# taken from table
x = [0, .5, 1.1, 1, .2]
y = [2, 2.5, 2.7, 2, 2.1]

# create points to piecewise interpolate
x1 = x + [0, -.3]
y1 = y + [2.15, 2.15]
t1 = set_t_values(x1, y1)
t = scipy.linspace(min(t1), max(t1))
px, py = construct_pols(x1, y1, t1)
px1 = scipy.interpolate.interp1d(t1, x1, kind='cubic')
py1 = scipy.interpolate.interp1d(t1, y1, kind='cubic')

# plot curve
plt.title("Piecewise Curve")
plt.plot(x1, y1, 'p',  px1(t), py1(t))
plt.xlabel("x")
plt.ylabel("y")
plt.show()
