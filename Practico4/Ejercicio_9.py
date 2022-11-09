import numpy as np
import sys
sys.path.append(r"C:\Users\Pedro\Desktop\LMA\Analisis_Numerico_2")
from Practico1.Ejercicio_13 import M
from Ejercicio_7 import sol_cuadmin

n = np.array([100])

for i in n:
    A = M(i)
    C = A[ : , : -2]
    b = np.zeros(i)
    b[0] = 1
    b[-1] = 1
    x = sol_cuadmin(C,b)

print(b)
print(C @ x[0])

#Esta bien que C @ x[0] no me de b?

