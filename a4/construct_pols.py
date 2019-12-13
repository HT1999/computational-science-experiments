"""
Assignment 4
q1.b: Construct polynominal points used to plot
Author: Hassan Tariq, 100657119
"""

import scipy.interpolate

# function to construct poly points
def construct_pols(t, x, y):
    px = scipy.interpolate.lagrange(t, x)  # use scipy to calculate
    py = scipy.interpolate.lagrange(t, y)

    return px, py
