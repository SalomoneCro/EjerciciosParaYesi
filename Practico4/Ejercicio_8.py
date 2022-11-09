import numpy as np
from Ejercicio_3 import soltrsupfil
from Ejercicio_7 import sol_cuadmin
import sys
sys.path.append(r"C:\Users\Pedro\Desktop\LMA\Analisis_Numerico_2")
from Practico2.Ejercicio_9 import dlup



def sol_tradicional(F, s):
    A = F.copy()
    b = s.copy()
    b = A.T @ b
    A = A.T @ A
    L, U, P = dlup(A)
    x = soltrsupfil(L, np.linalg.inv(U) @ b)
    
    return P @ x

def sol_QR(F, s):
    return sol_cuadmin(F, s)




b = np.array([1,1,1], dtype=float)
for k in range(5):

    A = np.array([[1,1],
                [1/(10 ** k),0],
                [0,1/(10 ** k)]], dtype=float)
    

    print(sol_tradicional(A,b))
    print(sol_QR(A, b))

