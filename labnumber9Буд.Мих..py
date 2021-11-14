Python 3.7.8 (tags/v3.7.8:4b47a5b6ba, Jun 28 2020, 08:53:46) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import math
from numpy import *
import matplotlib.pyplot as plt

x = [0.101, 0.106, 0.111, 0.116, 0.121, 0.126, 0.131, 0.136, 0.141, 0.146, 0.151]
y = [1.2618, 1.2764, 1.2912, 1.3061, 1.3213, 1.3366, 1.3520, 1.3677, 1.3835, 1.3985, 1.4157]
x1 = 0.112
x2 = 0.145
h = x[1] - x[0]
q1 = (x1 - x[0])/0.005
q2 = (x2 - x[0])/0.005
print("q1 = ",  q1)
print("q2 = ", q2)

def firstnut(y, j):
    mas1 = []
    for i in range(len(y)):
        mas1.append(y[i] - y[i-1])
    mas1.pop(0)

    if j == 1:
        return mas1
    else:
        j -= 1
        return firstnut(mas1, j)
   
form1 = y[0] + q1 * firstnut(y, 1)[0] + q1*(q1-1)* firstnut(y, 2)[0]/math.factorial(2)
form2 = q1*(q1-1)*(q1-2) * firstnut(y, 3)[0]/math.factorial(3)
form3 = q1*(q1-1)*(q1-2)*(q1-3) * firstnut(y, 4)[0]/math.factorial(4)
form4 = q1*(q1-1)*(q1-2)*(q1-3)*(q1-4) * firstnut(y, 5)[0]/math.factorial(5)
form5 = q1*(q1-1)*(q1-2)*(q1-3)*(q1-4)*(q1-5) * firstnut(y, 6)[0]/math.factorial(6)
form6 = q1*(q1-1)*(q1-2)*(q1-3)*(q1-4)*(q1-5)*(q1-6) * firstnut(y, 7)[0]/math.factorial(7)
form7 = q1*(q1-1)*(q1-2)*(q1-3)*(q1-4)*(q1-5)*(q1-6)*(q1-7) * firstnut(y, 8)[0]/math.factorial(8)
form8 = q1*(q1-1)*(q1-2)*(q1-3)*(q1-4)*(q1-5)*(q1-6)*(q1-7)*(q1-8) * firstnut(y, 9)[0]/math.factorial(9)
form9 = q1*(q1-1)*(q1-2)*(q1-3)*(q1-4)*(q1-5)*(q1-6)*(q1-7)*(q1-8)*(q1-9) * firstnut(y, 10)[0]/math.factorial(10)
formus = form1 + form2 + form3 + form4 + form5 + form6 + form7 + form8 + form9
print("First Nuton dormula = ",formus)

form01 = y[10] + q1 * firstnut(y, 1)[9] + q1*(q1+1)* firstnut(y, 2)[8]/math.factorial(2)
form02 = q1*(q1+1)*(q1+2)* firstnut(y, 3)[7]/math.factorial(3)
form03 = q1*(q1+1)*(q1+2)*(q1+3)* firstnut(y, 4)[6]/math.factorial(4)
form04 = q1*(q1+1)*(q1+2)*(q1+3)*(q1+4)* firstnut(y, 5)[5]/math.factorial(5)
form05 = q1*(q1+1)*(q1+2)*(q1+3)*(q1+4)*(q1+5)* firstnut(y, 6)[4]/math.factorial(6)
form06 = q1*(q1+1)*(q1+2)*(q1+3)*(q1+4)*(q1+5)*(q1+6)* firstnut(y, 7)[3]/math.factorial(7)
form07 = q1*(q1+1)*(q1+2)*(q1+3)*(q1+4)*(q1+5)*(q1+6)*(q1+7)* firstnut(y, 8)[2]/math.factorial(8)
form08 = q1*(q1+1)*(q1+2)*(q1+3)*(q1+4)*(q1+5)*(q1+6)*(q1+7)*(q1+8)* firstnut(y, 9)[1]/math.factorial(9)
form09 = q1*(q1+1)*(q1+2)*(q1+3)*(q1+4)*(q1+5)*(q1+6)*(q1+7)*(q1+8)*(q1+9)* firstnut(y, 10)[0]/math.factorial(10)
formus01 = form01 + form02 + form03 + form04 + form05 + form06 + form07 + form08 + form09
print("Second Nuton dormula = ",formus01)


sx = linspace(0.101, 0.151, 200)
sy = linspace(1.2618, 1.4157, 200)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Lab. work №9')
plt.plot(sx, 'b--')
plt.plot(sy, 'ro-')
plt.grid()
plt.show()

