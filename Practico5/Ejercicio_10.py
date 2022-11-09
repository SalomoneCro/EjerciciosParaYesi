import numpy as np

def sol_gradcon(A, b, x0, ItMax, tol):
    x = x0
    rs = [b - A @ x]
    p = rs[0]
    for i in range(ItMax):
        if np.sqrt(np.inner(rs[-1],rs[-1])) > tol:
            v = np.dot(A, p)
            alfa = np.inner(rs[i], p) / np.inner(v, p)
            x = x + alfa * p
            rs.append(rs[i] - alfa * v)
            beta = np.inner(rs[i + 1], rs[i + 1]) / np.inner(rs[i], rs[i])
            p = rs[i + 1] + beta * p
        else:
            return x
    return x

A = np.array([[3,1,9],
              [1,4,2],
              [9,2,8]], dtype=float)
b = np.array([1,1,1], dtype=float)

d = sol_gradcon(A,b, [0,0,0], 500, 1e-8)
#print(d)
#print(A @ d)
