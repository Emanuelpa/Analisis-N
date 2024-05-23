import math
import sympy as sp
        
def punto_fijo():

    # Solicitar al usuario que ingrese la ecuación
    input_equation = input("Ingrese la ecuación f(x) en terminos de x: ")
    input_equation_ = input("Ingrese la ecuación g(x) en terminos de x: ")
    # Crear un símbolo para la variable en la ecuación
    x = sp.symbols('x')

    #Solicitar demás input
    x0 = float(input("Ingrese el x0: "))
    tol = float(input("Ingrese la tolerancia: "))
    it = int(input("Ingrese el numero maximo de iteraciones: "))


    try:
        # Convertir la cadena de ecuación en una expresión simbólica
        fx = sp.sympify(input_equation,locals={'ln': sp.log} )
        gx = sp.sympify(input_equation_, locals={'ln': sp.log})
        print("La ecuacion tomada es g(x)= " + str(gx))
        
    except sp.SympifyError:
        print("La ecuación ingresada no es válida.")
        print(x0)


    g = gx.subs(x, x0)
    e = abs(g-x0)
    ite = 0

    while e>=tol and ite<=it:
        x0=g
        g = gx.subs(x, x0)
        print(g)
        e = abs(g-x0)
        ite+=1
    if e <= tol:
        print(str(g) + " es raiz de " + str(fx) + " con error de " + str(e))
        print(ite)
    else:
        print("Se excedió el número de iteraciones y no se encontró una raiz")
        print(e)
        print(tol)


punto_fijo()