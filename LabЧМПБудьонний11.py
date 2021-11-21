Python 3.7.8 (tags/v3.7.8:4b47a5b6ba, Jun 28 2020, 08:53:46) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> import matplotlib.pyplot as plt

from numpy import *
import sympy as sp

def taylor(x):

    y = 0

    d1 = sp.diff(f, x) #наша перша похідна

    d2 = sp.diff(d1, x) #наша друга похідна

    d3 = sp.diff(d2, x) #наша третя похідна
    
    print('d1= ', d1, 'd2= ', d2, 'd3= ', d3)

    y += f + d1*x + d2*(x-0)**2/2 + d3*(x-0)**3/6

    print ('y= ', y)

    return y

x = sp.symbols('x')

f = sp.cos(3*x-1)+x

taylor_x = taylor(x)

pl = sp.plot(f, taylor_x, (x, -10, 10), label='Taylor')
plt.show()