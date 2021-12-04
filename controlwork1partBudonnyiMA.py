Python 3.7.8 (tags/v3.7.8:4b47a5b6ba, Jun 28 2020, 08:53:46) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
import math
import matplotlib.pyplot as plt
import numpy as np
from scipy import integrate
from scipy.interpolate import interp1d

# step №1 #

speed = np.array([25, 35, 45, 30, 60, 120, 100, 100, 70, 75, 80, 65])
times = np.linspace(0, 11, 12, dtype=int)

# step №2 #

print("Our time array: ", times)

# step №3 #

plt.plot(times, speed, 'r-', times, speed, 'bo')
plt.axis([0, 11, 0, 130])
plt.xlabel(' Our time ')
plt.ylabel(' Our speed ')
plt.grid()
plt.show()

# step №4 #

f = interp1d(times, speed, kind='cubic')
urnewx = np.linspace(0, 11, 10000)
plt.plot(times, speed, 'r-', times, speed, 'bo', urnewx, f(urnewx), 'y--')
plt.axis([0, 11, 0, 130])
plt.xlabel(' Our time ')
plt.ylabel(' Our speed ')
plt.grid()
plt.show()

# step №5 #

def S(ti1, ti2):
    speed = np.array([25, 35, 45, 30, 60, 120, 100, 100, 70, 75, 80, 65])
    S = (speed[ti2]*ti2)*(ti2**2) - (speed[ti1]*ti1)*(ti1**2)
    return S

print("Our S = ", S(0, 11))