Python 3.7.8 (tags/v3.7.8:4b47a5b6ba, Jun 28 2020, 08:53:46) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import matplotlib.pyplot as plt
from scipy.interpolate import UnivariateSpline
from numpy import *
#first example#
#x = [1.6, 1.7, 1.8, 1.9, 2.0, 2.1]
#y = [4.6, 4.77, 4.94, 5.11, 5.29, 5.47]

#second example#
x = [1.8, 1.9, 2, 2.1, 2.2, 2.3]
y = [2.6, 2.90, 3.21, 3.53, 3.86, 4.20]

spl = UnivariateSpline(x, y)
xs = linspace(1, 2.8, 2000)
plt.plot(x,y,'ro',xs, spl(xs), 'g')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Lab. work №14 2')
plt.grid()
plt.show()