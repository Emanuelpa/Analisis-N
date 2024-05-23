import sympy as sp


def biseccion():
    # Solicitar al usuario que ingrese la ecuación
    input_equation = input("Ingrese la ecuación en terminos de x: ")
    # Crear un símbolo para la variable en la ecuación
    x = sp.symbols('x')

    #Solicitar demás input
    a = float(input("Ingrese el x0: "))
    b = float(input("Ingrese el xf: "))
    tol = float(input("Ingrese la tolerancia: "))

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
        xm = (a+b)/2
        fm = fx.subs(x, xm)
        e=float("inf")

        while e >= tol and fm != 0:
            print('entra')
            if fa*fm <= 0:
                b = xm
                fb = fm
            else:
                a=xm
                fa=fm
            xm = (a+b)/2
            fm = fx.subs(x, xm)
            e = abs(xm-a)
        
        if fm == 0:
            print(str(xm) + ' es una raiz')
        else:
            print(str(xm) + ' es una raiz con tolerancia de '+ str(e))


biseccion()