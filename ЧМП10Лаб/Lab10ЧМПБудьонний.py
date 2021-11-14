Python 3.7.8 (tags/v3.7.8:4b47a5b6ba, Jun 28 2020, 08:53:46) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import matplotlib.pyplot as plt
from scipy.interpolate import UnivariateSpline
from numpy import *
x = [1, 1.3, 1.7, 2.2, 2.8]
y = [2.95, 3.89, 1.54, 3.38, 2.34]
spl = UnivariateSpline(x, y)
xs = linspace(1, 2.8, 2000)
plt.plot(x,y,'ro',xs, spl(xs), 'g')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Lab. work №10')
plt.grid()
plt.show()

