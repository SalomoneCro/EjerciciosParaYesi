import numpy as np

#Defino funciones que voy a usar

def soltrinffil(R, c):
    x = c.copy()
    k = np.min(np.nonzero(x))
    for i in range(k, len(x)):
        x[i] = ((x[i] - R[i, :i] @ x[0:i]) / R[i, i])
    return x

def soltrsupcol(M,n):
    z = n.copy()
    k = np.max(np.nonzero(n))
    for j in reversed(range(k + 1)):
        z[j] = z[j] / M[j,j]
        z[:j] = z[:j] - z[j] * M[: j, j]
    return z

#Descomposicion LU
def dlu(F):
    A = F.copy()
    n = len(A[:,1])
    for i in range(n - 1):
        A[i + 1:, i] = A[i + 1:, i] / A[i,i]
        A[i + 1:, i + 1:] -= np.outer(A[i + 1:, i], A[i, i + 1:])
    L = np.tril(A, -1) + np.eye(n)
    U = np.triu(A)
    return L, U

#Funcion que me hace la matriz dada en el ejercicio de dimension nxn
def M(n):
    M = np.zeros((n,n))
    np.fill_diagonal(M, 2)
    h = - np.ones(n-1)
    K = np.diag(h, 1)
    P = np.diag(h, -1)
    M = M + K + P
    return M

#K dado por la consigna
k = 3
#b dado por la consigna
b = np.array([0,0,6,-24,30], dtype=float)
#Matriz del problema
A = M(5)

#Hago la descomposicion LU
L, U = (dlu(A))

#Con cada iteracion de este for, resolvere un sistema triangular 
for i in range(2*k):

    #Si estoy en una iteracion par, debo resolver un sistema triangular inferior con L como matriz
    if i % 2 == 0:
        b = soltrinffil(L, b)

    #Si estoy en una iteracion impar, debo resolver un sistema triangular superior con U como matriz
    if i % 2 == 1:
        b = soltrsupcol(U, b)
    

#Imprimo en la terminal la solucion de (A**k)x = b
print(b)