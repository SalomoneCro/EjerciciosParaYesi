import numpy as np
from Ejercicio_10 import sol_gradcon
from Ejercicio_9 import sol_Richardson
from Ejercicio_8 import sol_gradopt

#a
A = np.array([[9,-2,0],
              [-2,4,-1],
              [0,-1,1]], dtype=float)

b = np.array([5,1,-5/6], dtype=float)

#print(sol_gradopt(A, b, [0,0,0], 500, 1e-8))
#print(sol_Richardson(A,b, [0,0,0], 500, 1e-8))
#print(sol_gradcon(A,b, [0,0,0], 500, 1e-8))

#b
A = np.array([[4,-1,0],
              [-1,4,-1],
              [0,-1,4]], dtype=float)

b = np.array([2,6,2], dtype=float)

print(sol_gradopt(A, b, [0,0,0], 500, 1e-8))
print(sol_Richardson(A,b, [0,0,0], 500, 1e-8))
print(sol_gradcon(A,b, [0,0,0], 500, 1e-8))