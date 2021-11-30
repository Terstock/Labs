
#Приклад №1#

#import matplotlib.pyplot as plt
#plt.plot([1, 3, 2, 4])
#plt.show()

#Приклад №2#

#from numpy import * # для використання функцій exp та linespace
#import matplotlib.pyplot as plt
#def f(t):
#    return t ** 2 * exp(-t ** 2)
#t = linspace(0, 3, 51) # 51 точка між 0 та 3
#y = f(t)
#plt.plot(t, y)
#plt.show()

#Приклад №3#

#from numpy import *
#import matplotlib.pyplot as plt
#t = linspace(0, 3, 51)
#y = t ** 2 * exp(-t ** 2)
#plt.plot(t, y, 'g--', label='t^2*exp(-t^2)')
#plt.axis([0, 3, -0.05, 0.5]) # [xmin, xmax, ymin, ymax]
#plt.xlabel('t') # позначення вісі абсцис
#plt.ylabel('y') # позначення е вісі ординат
#plt.title('My first normal plot') # назва графіка
#plt.legend() # вставка легенди (тексту в label)
#plt.show()

#Приклад №4#

#from numpy import *
#import matplotlib.pyplot as plt
#t = linspace(0, 3, 51)
#y1 = t ** 2 * exp(-t ** 2)
#y2 = t ** 4 * exp(-t ** 2)
#y3 = t ** 6 * exp(-t ** 2)
#plt.plot(t, y1, 'g^', # маркери із зелених трикутників
#t, y2, 'b--', # синя штриховая
#t, y3, 'ro-') # червоні круглі маркери
# з'єднані суцільною лінією
#plt.xlabel('t')
#plt.ylabel('y')
#plt.title('Plotting with markers')
#plt.legend(['t^2*exp(-t^2)',
#'t^4*exp(-t^2)',
#'t^6*exp(-t^2)'], # список легенди
#loc='upper left') # положення легенди
#plt.show()

#Приклад власний#

#from numpy import *
#import math
#import matplotlib.pyplot as plt
#t = linspace(-5, 5, 51)
#y1 = 1 / t * sin(5 * t)
#plt.plot(t, y1, 'g--') # маркери із зелених трикутників
#t, y2, 'b--', # синя штриховая
#t, y3, 'ro-') # червоні круглі маркери з'єднані суцільною лінією
#plt.xlabel('t')
#plt.ylabel('y')
#plt.title('Моє власне завдання')
#plt.legend(['=1/t*sin(5*t)'], loc='upper right')
#plt.plot(t, y1)
#plt.grid()

#plt.show()

from numpy import *
import math
import matplotlib.pyplot as plt
def f(t):
    return 1 / t * sin(5 * t)
t = linspace(5,-5, 6)
plt.plot(t, f(t), 'k-', label = '1/t*sin(5*t)')
plt.xticks(range(len(t)), ['a', 'b', 'c', 'd', 'e', 'f'])
plt.yticks(range(4, 10, 2))

plt.show()