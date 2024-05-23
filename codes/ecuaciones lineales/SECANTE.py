import math
import sympy as sp
        
def secante():

    # Solicitar al usuario que ingrese la ecuación
    input_equation = input("Ingrese la ecuación f(x) en terminos de x: ")
    # Crear un símbolo para la variable en la ecuación
    x = sp.symbols('x')

    #Solicitar demás input
    tol = float(input("Ingrese la tolerancia: "))
    it = int(input("Ingrese el numero maximo de iteraciones: "))


    try:
        # Convertir la cadena de ecuación en una expresión simbólica
        fx = sp.sympify(input_equation,locals={'ln': sp.log} )
        print("La ecuacion tomada es f(x)= " + str(fx))
        
    except sp.SympifyError:
        print("La ecuación ingresada no es válida.")
    xant = 0
    xn = 1
    g = (xn - ((fx.subs(x,xn)*(xn-xant))/(fx.subs(x,xn)-fx.subs(x,xant)))).evalf()
    print(g)
    e = abs(g-xn)
    ite = 0
    
    while e>=tol and ite<=it and e !=0:
        xant = xn
        xn=g
        g = (xn - ((fx.subs(x,xn)*(xn-xant))/(fx.subs(x,xn)-fx.subs(x,xant)))).evalf()
        e = abs(g-xn)
        ite+=1
    if e <= tol:
        print(str(g) + " es raiz de " + str(fx) + " con error de " + str(e))
        print(ite)
    else:
        print("Se excedió el número de iteraciones y no se encontró una raiz")

        






secante()