Python 3.7.8 (tags/v3.7.8:4b47a5b6ba, Jun 28 2020, 08:53:46) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from numpy import *
import matplotlib.pyplot as plt
x = [0.1, 0.15, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.47, 0.5]
y = []
xx = 0
yy = 0
xx2 = 0
xy = 0
a1 = 0
a0 = 0
i = 0

while i < len(x):
    y.append(cos(3*x[i] - 1) +x[i])
    i +=1
i = 0

while i < (len(x) - 1):
    xx += x[i]
    yy += y[i]
    xx2 += (x[i])**2
    xy += x[i] *y[i]
    i += 1

xx /= len(x)
yy /= len(x)
xx2 /= len(x)
xy /= len(x)

print("x avg---", xx, "y avg---", yy, "xy ---", xy, "xx**2 ---", xx2)
a1 = (xy - xx * yy) / (xx2 - xx**2)
a0 = yy - a1 * xx
print("a1 ---", a1, "a0 ---", a0)

def F(x):
    global a1
    global a0
    f = a0 + a1 * x
    return f

xs = array(linspace(0, 1))
f = vectorize(F)
plt.plot(x, y, 'ro', xs, f(xs))
plt.axis([0, 1, 0, 3])
plt.scatter (x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.show()