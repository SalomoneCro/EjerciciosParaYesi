import numpy as np

def sol_Richardson(A, b, x0, ItMax, tol):
    x = x0
    r = b - A @ x
    w, W = np.linalg.eig(A)
    alfa = 2 / (w[-1]+w[0])
    for i in range(ItMax):
        if np.sqrt(np.inner(r,r)) > tol:
            v = np.dot(A, r)
            x = x + alfa * r
            r = r - alfa * v
        else:
            return x
    return x

A = np.array([[3,1,5],
              [1,4,2],
              [5,2,8]], dtype=float)
b = np.array([1,1,1], dtype=float)

d = sol_Richardson(A,b, [0,0,0], 500, 1e-8)
#print(d)
#print(A @ d)
