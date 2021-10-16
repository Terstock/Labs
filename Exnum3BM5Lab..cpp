import numpy as np
matrix = np.matrix([[2, -1, 1], [3, 2, 2], [1, -2, 1]] )
vect = np.matrix([[2], [-2], [1]] )
x = ([[0], [0], [0]] )

def myfunc(matrix, vector) :
    n = len(vect) - 1
    x[n] = vect[n] / matrix[n, n]
    i = n - 1
    while i >= 1 :
        j = i + 1
        sumus = 0
        while j <= n :
            sumus = sumus + matrix[i, j] * x[j]
            j += 1
            x[i] = (vect[i] - sumus) / matrix[i, i]
            print(x[i])
            i = i - 1
            myfunc(matrix, vect)