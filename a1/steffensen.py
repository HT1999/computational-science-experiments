"""
Assignment 1
q2.a: Steffensen's iteration
Author: Hassan Tariq, 100657119
"""

# Create a function implementing a single Newton step function
def newtonStep(f,df,x):
    r = f(x)
    dx = -r/df(x)
    x = x + dx
    return x

# Implement Steffensen pesudocode provided
# Inputs: function (f), derivative (df), intial guess (x0),
#         error (err),  max iterations (kmax)
def steffensen(f, df, x0, err, kmax):
    for N in range(1,kmax+1):
        y1 = x0
        y2 = newtonStep(f, df, y1)
        y3 = newtonStep(f, df, y2)
        x0 = y1 - (((y2-y1)**2.) / (y3-2.*y2+y1))
        print("it=%d x=%s err=%e |f(x)|=%s" % (N, x0, abs(x0-y1), abs(f(x0))))
        if abs(f(x0)) < err:
            print('\tConverged!')
            break

    print('\tOutput',x0)
