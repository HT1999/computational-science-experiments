"""
Assignment 1
q1.c: Iteration function for solving g(x)
Author: Hassan Tariq, 100657119
"""
# Functions defined in test script

"""
Could not name this function iteration.m due to syntax limitations

iteration() inputs:
function (f), function (g), intial guess (x0),
max iterations (kmax), error tolerance (tolx),
residual tolerance (tolf),
"""

def iteration(f,g,x0, kmax, tolx, tolf):
    x = x0
    conv = False
    for i in range(1,kmax+1):
        xNew = g(x)
        res = abs(f(xNew))
        err = abs(xNew - x)
        print('it=%d x=%s err=%e res=%e' % (i,xNew,err,res))
        if err < tolx and res < tolf:
            conv = True
            print("\napprox.solution=%s err=%e res=%e" % (x,err,res))
            return xNew, err, res
        x = xNew
    print("\napprox.solution=%s err=%e res=%e" % (x,err,res))
