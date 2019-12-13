"""
Assignment 4
q1.a: Find values t to interpolate
Author: Hassan Tariq, 100657119
"""

import scipy.interpolate

def set_t_values(x, y):
    t = [0]
    # create list that will be used to find difference of points
    x_final, y_final = scipy.array(x[1:]) ,scipy.array(y[1:])
    # find difference b/w points
    x_diff, y_diff = x_final - x[:-1], y_final - y[:-1]
    distance = scipy.hypot(x_diff, y_diff)
    t_iterative = scipy.cumsum(distance)            # add tn-1 to next diff
    t.extend(t_iterative)                           # append array to end of list
    return t
