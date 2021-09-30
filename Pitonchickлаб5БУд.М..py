import numpy as np
#am= np.matrix([[2, -1, 1],[3, 2, 2], [1, -2, 1]])
#bm= np.matrix([[2],[-2],[1]])
#print("Матриця A: ",'\n', am, '\n', "Матриця B: ", '\n', bm, '\n' )


def gass(a,b):
    n = len(b)
    for k in range(1,n):
        for i in range (k+1,n):
            if a[i,k] != 0.0:
                a[i,k:n] = a[i,k:n] - a [i,k]/a[k,k] * a[k,k:n]
                b[i] = b[i] - a [i,k]/a[k,k] * b[k]
    for k in range (n-1, -1, -1):
        b[k] = (b[k] - np.dot(a[k,k:n], b[k:n]))/a[k,k]
    print ("Функція солв: ", '\n', np.linalg.solve (am, bm))
    print ("Метод Джордана-Гаусса:", "\n", np.linalg.inv(am) *bm)
    
    return b

print ("Метод Гаусса: ", gass(np.matrix([[2, -1, 1], [3, 2, 2], [1, -2, 1]]), np.matrix([[2],[-2], [1]])))