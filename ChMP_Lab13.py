
from scipy import integrate
from numpy import *
import math

def f1(x):
    return 1/(sqrt((x**2) + 3.2))

def rectmethodleft(f1, a, b, n):
    h1 = (b - a)/n
    sum1 = f1(a)
    i = 0
    for i in range(1, n):
        a = a+h1
        sum1 = sum1 + f1(a)
    sum1 = sum1 * h1
    
    return sum1

print("Left rectangle method = ", rectmethodleft(f1, 1.2, 2.7, 10))

v,err = integrate.quad(f1, 1.2, 2.7)
def rectmethodright(f1, a, b, n):
    h1 = (b - a)/n
    a = a + h1
    sum1 = f1(a)
    i = 0
    for i in range(1, n):
        a = a+h1
        sum1 = sum1 + f1(a)
    sum1 = sum1 * h1
    
    return sum1

print("Right rectangle method = ", rectmethodright(f1, 1.2, 2.7, 10))

def rectmethod(f1, a, b, n):
    h1 = (b - a)/n
    sum1 = f1(a + (h1/2))
    i = 0
    for i in range(1, n-1):
        a = a+h1/2
        sum1 = sum1 + f1(a + h1/2)
    sum1 = sum1 * h1
    
    return sum1

print("Medium rectangle method = ", rectmethod(f1, 1.2, 2.7, 10))
print("Check for rectangle method = ", v)

def f2(x):
    return 1*(x+1)*math.sin(x)
def simpsonmethod(f2, a, b, n):
    h2 = (b - a)/n
    sum2 = (h2/3)*(f2(a) + 4*(f2(a+h2) + f2(a+h2*3) + f2(a+h2*5) + f2(a+h2*7)) + 2*(f2(a+h2*2) + f2(a+h2*4) + f2(a+h2*6)) + f2(a+h2*8))
    return sum2
print("Simpson method = ", simpsonmethod(f2, 1.6, 2.4, 8))

v,err = integrate.quad(f2, 1.6, 2.4)

print("Check for Simpson method = ", v)

def f3(x):
    return 1/(sqrt((x**2) + 4))
def trapmethod(f3, a, b, n):
    h = (b - a)/n
    sum = 0.5*(f3(a) + f3(b))
    for i in range(1, n):
        sum += f3(a + i*h)
    return sum*h

print("Trapezoidal method = ", trapmethod(f3, 0.5, 2.3, 20))
v,err = integrate.quad(f3, 0.5, 2.3)
print("Check for trapeziodal method = ", v)

