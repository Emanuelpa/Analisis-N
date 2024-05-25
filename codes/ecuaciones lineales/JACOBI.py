from matplotlib import pyplot as plt
import numpy as np

def print_table(table):
    length = len(table)
    print("it   |                           x                            |   error")
    for row_ in table[length-5:length]:
        print(row_)


#funciones para capturar errores al ingresar datos
def input_float():
    while True:
        try:
            num = float(input())
            return num
            break
        except ValueError:
            print("No ingresaste un valor válido, revisa que si sea un número")

def input_int():
    while True:
        try:
            num = int(input())
            return num
            break
        except ValueError:
            print("No ingresaste un valor válido, revisa que si sea un número entero")

        

def jacobi():
    while True:
        try:
            n = int(input("Introduce el número de filas/columnas de la matriz A: "))
            break
        except ValueError:
            print("No ingresaste un valor válido, revisa que si sea un número")

    A = np.array([input(f"Introduce la fila {i+1} de la matriz A separada por espacios: ").split() for i in range(n)], dtype=float)
    b = np.array(input("Introduce el vector b separado por espacios: ").split(), dtype=float)
    x0 = np.array(input("Introduce el vector x0 separado por espacios: ").split(), dtype=float)
    print("Ingrese el numero maximo de iteraciones: ")
    it = input_int()
    print("Ingrese la tolerancia: ")
    tol = input_float()


    D = np.diag(np.diag(A))

    L = -np.tril(A) + D
    U = -np.triu(A) + D
    T = np.linalg.inv(D).dot(L + U)
    C = np.linalg.inv(D).dot(b)

    table = []
    errors = []

    xant = x0
    e = float('inf')
    ite = 1

    row = str(0)+ "    |   "  + str(x0)+ "    |   "  + str(e)
    table.append(row)

    while e > tol and ite < it:
        xact = T.dot(xant) + C
        e = np.linalg.norm(xant - xact)
        row = str(ite)+ "    |   "  + str(xact)+ "    |   "  + str(e)
        errors.append(e)
        table.append(row)
        xant = xact
        ite = ite + 1

    if e<tol:
        print(str(xact) + " es aproximacion con una tolerancia de " + str(tol))
    else:
        print("Se excedio el numero de iteraciones")
    


    print_table(table)
    #graficar
    iterations = list(range(len(errors)))
    plt.plot(iterations, errors, marker='o', linestyle='-', color='r', label='Errores')

    plt.xlabel('Iteración')
    plt.ylabel('Error')
    plt.title('Gráfica de Errores')
    plt.legend()

    # Mostrar la gráfica
    plt.show()
        

jacobi()