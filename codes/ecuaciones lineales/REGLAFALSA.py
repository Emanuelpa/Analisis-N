import sympy as sp
import numpy as np

def encontrar_ec_recta(x1,x2,y1,y2):
    if x2 - x1 != 0:
        m = (y2 - y1) / (x2 - x1)
    else:
        raise ValueError("La pendiente es indefinida (los puntos tienen la misma coordenada x).")

    # Calcular la intersección con el eje y (b)
    b = y1 - m * x1
    rect_equation=0
    

    rect = str(m) + '*x + ' + str(b)
    #print(rect)
    try:
        # Convertir la cadena de ecuación en una expresión simbólica
        rect_equation = sp.sympify(rect)
    
    except sp.SympifyError:
        print("La ecuación ingresada no es válida.")

    return rect_equation



def regla_falsa():
    # Solicitar al usuario que ingrese la ecuación
    input_equation = input("Ingrese la ecuación en terminos de x: ")
    # Crear un símbolo para la variable en la ecuación
    x = sp.symbols('x')

    #Solicitar demás input
    a = float(input("Ingrese el x0: "))
    b = float(input("Ingrese el xf: "))
    tol = float(input("Ingrese la tolerancia: "))
    error_type = input("Qué tipo de error desea utilizar a) Error Absoluto, r) Error relativo").lower()

    try:
        # Convertir la cadena de ecuación en una expresión simbólica
        fx = sp.sympify(input_equation)
        print("La ecuacion tomada es: ")
        print(fx)
        
    except sp.SympifyError:
        print("La ecuación ingresada no es válida.")
    fa = fx.subs(x, a)
    
    #print(fa)
    fb = fx.subs(x, b)
    if fa == 0:
        print(str(a) + ' es una raiz')
    elif fb == 0:
        print(str(b) + ' es una raiz')
    else:
        r = encontrar_ec_recta(a,b,fa,fb)
        print(r)
        xm = sp.solve(r,x)[0]
        
        fm = fx.subs(x, xm)
        e=float("inf")

        while e >= tol and fm != 0:
            if fa*fm <= 0:
                b = xm
                fb = fm
            else:
                a=xm
                fa=fm
            r = encontrar_ec_recta(a,b,fa,fb)
            #print(r)
            xm = sp.solve(r,x)[0]
            fm = fx.subs(x, xm)
            e = abs(xm-a)
            if error_type == "r":
                e = e/xm
        
        if fm == 0:
            print(str(xm) + ' es una raiz')
        else:
            print(str(xm) + ' es una raiz con tolerancia de '+ str(e))


regla_falsa()