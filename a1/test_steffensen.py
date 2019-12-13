"""
Assignment 1
q2.b: Steffensen's iteration test script
Author: Hassan Tariq, 100657119
"""

import math
from steffensen import steffensen

# Define function
def f(x):
    return math.exp(-x**2.+x) - (1./2.)*x - 1.0836

# Define derivative of function
def df(x):
    return math.exp(-x**2.+x) * (-2.*x+1.) - (1./2.)

# Use newton method to compare
def newtons(f,df,x0,tolx,tolf,kmax):
    x = x0                      # Save intital value in temp var
    conv = False                # Track if convergence occurred
    for i in range(1,kmax+1):   # Run kmax number of times
        dx = -f(x)/df(x)        # Newton step
        x = x + dx              # Update x for residual and next iteration
        err = abs(dx)           # Update error
        res = abs(f(x))         # Update residual
        print('it=%d x=%s err=%e |f(x)|=%e' % (i,x,err,res))
        if err < tolx and res < tolf:
            conv = True
            print('\tConverged!')
            break


    # Convergence failed prompt
    if conv == False:
        print('\tNo convergence!')
    print("\tOutput %s" % (x))
    return x

# Initial guess value given in 2.b, x = 1
x0 = 1
# Max iterations for both methods
kmax = 100

# Same tolerances for both methods to see quadratic converging
err = 1e-8 # Steffensen error
tolx = tolf = err  # Newton tolerance

print("\n\tSteffensen's iteration")
steffensen(f, df, x0, err, kmax)

print("\n\tNewton's iteration")
newtons(f, df, x0, tolx, tolf, kmax)
