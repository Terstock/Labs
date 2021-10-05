from scipy import optimize
import math
def fun(x):
    return [math.cos(x[0]-1) + x[1] - 0.5, x[0] - math.cos(x[1]) - 3]
sol = optimize.root(fun, [0, 0], method = 'hybr')


print(sol.x)

#f1 = 0.5 - math.cos(x + 1)
#f2 = 3 - math.cos(y)

#np.diff(f1)

#print(np.diff)


#from scipy.misc import derivative
#from sympy import *
#x,y = symbols ('x, y')
#def f(x):
   # return math.cos(x - 1) + x - 0.5
#print(derivative(f, 0.5, dx= ))

