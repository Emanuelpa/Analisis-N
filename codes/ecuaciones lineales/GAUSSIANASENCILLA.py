import numpy as np

def gauss_elimination():
    while True:
        try:
            n = int(input("Introduce el número de filas/columnas de la matriz A: "))
            break
        except ValueError:
            print("No ingresaste un valor válido, revisa que si sea un número")

    A = np.array([input(f"Introduce la fila {i+1} de la matriz A separada por espacios: ").split() for i in range(n)], dtype=float)
    b = np.array(input("Introduce el vector b separado por espacios: ").split(), dtype=float)
    

    M = np.hstack([A, b.reshape(-1,1)])  # Combina A y b en una sola matriz M
    print("Matriz ampliada a resolver")
    print(M)
    print("\n\n")

    # Proceso de eliminación
    for i in range(n-1):
        for j in range(i+1, n):
            if M[i, i] != 0:
                M[j, i:] -= (M[j, i] / M[i, i]) * M[i, i:]
            else:
                print("un elemento de la diagonal es cero")
            print(f"Iteración {i},{j}:")
            print(M)
            

    # Sustitución regresiva
    x = np.zeros(n)
    for i in reversed(range(n)):
        x[i] = (M[i, -1] - np.dot(M[i, i+1:n], x[i+1:n])) / M[i, i]
        print(f"Sustitución {i}: x[{i}] = {x[i]}")

    print(x)




gauss_elimination()