"""
Assignment 1
Question 1 test script for both iteration.py and recursion.py
Author: Hassan Tariq, 100657119
"""

from iteration import iteration
from recursion import recursion
import math
pi = math.pi

# Define both function
def f(x):
    return math.sin(pi*x) - x*x

# Define derivative of function
def g(x):
    return 1/(2*math.pi) * math.sin(math.pi*x) - 1/(2*math.pi) * x**2 + x

#Initialize variables
x0 = 1
tolx = tolf = 1e-6
kmax = 50
print("\n\tIterative solution for question 1")
iteration(f, g, x0, kmax, tolx, tolf)

# Initialize extra recursion counter variable
i = 0
print("\n\n\tRecursive solution for question 1")
recursion(f, g, x0, tolx, tolf, kmax, i)
