"""
Assignment 1
q1.d: Iteration function for solving g(x)
Author: Hassan Tariq, 100657119
"""
# Functions defined in test script

"""
Could not name this function recursion.m due to syntax limitations

recursion() inputs:
function (f), function (g), intial guess (x0),
max iterations (kmax), error tolerance (tolx),
residual tolerance (tolf), recursion counter passed as 0 (i)
"""
def recursion(f,g,x0,kmax,tolx,tolf,i):
    x = x0
    xNew = g(x)             # Create new x for g function
    res = abs(f(xNew))      # Update residual
    err = abs(xNew - x)     # Update error
    i = i + 1               # Update recursion counter
    kmax = kmax - 1         # Update loop counter
    print('it=%d x=%s err=%e res=%e' % (i,xNew,err,res))

    # Check tolerances to recurse or return values
    if err > tolx or res > tolf:
        x=xNew
        return recursion(f,g,x,tolf,tolx,kmax,i)
    elif kmax <= 0:
        print("\napprox.solution=%s err=%e res=%e" % (xNew,err,res))
        return xNew,err,res
    else:
        print("\napprox.solution=%s err=%e res=%e" % (x,err,res))
        return x,err,res
