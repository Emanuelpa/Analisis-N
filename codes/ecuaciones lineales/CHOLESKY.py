import numpy as np

def input_int():
    while True:
        try:
            num = int(input())
            return num
            break
        except ValueError:
            print("No ingresaste un valor válido, revisa que si sea un número entero")

def forward_substitution(L, b):
    n = L.shape[0]
    z = np.zeros(n)

    for i in range(n):
        z[i] = (b[i] - np.dot(L[i, :i], z[:i])) / L[i, i]

    return z

def backward_substitution(U, z):
    n = U.shape[0]
    x = np.zeros(n)

    for i in range(n - 1, -1, -1):
        x[i] = (z[i] - np.dot(U[i, i + 1:], x[i + 1:])) / U[i, i]

    return x


def cholesky():
    while True:
        try:
            n = int(input("Introduce el número de filas/columnas de la matriz A: "))
            break
        except ValueError:
            print("No ingresaste un valor válido, revisa que si sea un número")

    A = np.array([input(f"Introduce la fila {i+1} de la matriz A separada por espacios: ").split() for i in range(n)], dtype=float)
    print("cuantos vectores b desea solucionar")
    q = input_int()
    bs = []

    for i in range(q):
        b = np.array(input("Introduce el vector b separado por espacios: ").split(), dtype=float)
        bs.append(b)

    print(A)

    n = A.shape[0]
    L = np.eye(n)
    U = np.eye(n)

    for k in range(n):
        addition1 = 0
        for p in range(k):
            addition1 += L[k,p] * U[p,k]
        L[k,k] = (A[k,k] - addition1)**0.5   #es asi por cholesky
        U[k,k] = L[k,k]

        for i in range (k,n):
            addition2 = 0
            for p in range(k):
                addition2 += L[i,p]*U[p,k]
            L[i,k] = (A[i,k] - addition2)/U[k,k]

        for j in range(k+1,n):
            addition3 = 0
            for p in range(k):
                addition3 += L[k,p]*U[p,j]
            U[k,j] = (A[k,j]-addition3)/L[k,k]

    print("Matrices factorizadas")
    print("L= \n" + str(L) + "\nU= \n"+ str(U))
    print("\n\n")

    #resolver todos los vectores b
    sol = 1
    for b_ in bs:
        z = forward_substitution(L,b_)
        x = backward_substitution(U,z)
        print("Sol 1 vector: " +str(b_))
        print("z = " + str(z))
        print("x = " + str(x))
        sol+=1
        


cholesky()



            



#     for i in range(n-1):
#         for j in range(i, n):
#             L[j, i] = A[j, i] - np.dot(L[j, 0:i], U[0:i, i])
#         for j in range(i+1, n):
#             U[i, j] = (A[i, j] - np.dot(L[i, 0:i], U[0:i, j])) / L[i, i]

#     L[n-1, n-1] = A[n-1, n-1] - np.dot(L[n-1, 0:n-1], U[0:n-1, n-1])

        