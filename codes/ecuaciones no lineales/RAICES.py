import math
import sympy as sp
import matplotlib.pyplot as plt


def print_table(table):
    length = len(table)
    print("it       |   x      |   g(x)      |   error")
    for row_ in table:
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
        
def raices():

    # Solicitar al usuario que ingrese la ecuación
    input_equation = input("Ingrese la ecuación f(x) en terminos de x: ")
    # Crear un símbolo para la variable en la ecuación
    x = sp.symbols('x')

    #Solicitar demás input
    print("Ingrese el x0: ")
    x0 = input_float()
    print("Ingrese la tolerancia: ")
    tol = input_float()
    print("Ingrese el numero maximo de iteraciones: ")
    it = input_int()
    relative_error = False
    error_type = input("Ingrese el tipo de error con el que desea trabajar a) error absoluto r) error relativo \n")
    if error_type.lower() == "r":
        relative_error = True


    try:
        # Convertir la cadena de ecuación en una expresión simbólica
        fx = sp.sympify(input_equation,locals={'ln': sp.log} )
        print("La ecuacion tomada es f(x)= " + str(fx))
        
    except sp.SympifyError:
        print("La ecuación ingresada no es válida.")

    #inicio del metodo
    table = []
    errors = []
    diff = sp.diff(fx, x)
    diff2 = sp.diff(diff, x)
    print(diff)
    print(diff2)
    g = x0 - ((fx.subs(x,x0)*diff.subs(x,x0))/(diff.subs(x,x0)**2 - fx.subs(x,x0)*diff2.subs(x,x0)))
    e = abs(g-x0)
    if relative_error:
        e = e/x0
    row = str(0) + "    |   " + str(x0) + "  |   " + str(g)+ "  |   " + str(e)
    table.append(row)
    errors.append(e)
    ite = 1


    while e>=tol and ite<=it and e!=0:
        x0=g
        g = x0 - ((fx.subs(x,x0)*diff.subs(x,x0))/(diff.subs(x,x0)**2 - fx.subs(x,x0)*diff2.subs(x,x0)))
        e = abs(g-x0)
        if relative_error:
            e = e/x0
        row = str(ite) + "    |   " + str(x0) + "  |   " + str(g)+ "  |   " + str(e)
        table.append(row)
        errors.append(e)
        ite+=1
    if e <= tol:
        print(str(g) + " es raiz de " + str(fx) + " con error de " + str(e))
        print_table(table)
    else:
        print("Se excedió el número de iteraciones y no se encontró una raiz")
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
        





raices()