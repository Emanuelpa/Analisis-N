import sympy as sp
import matplotlib.pyplot as plt

def print_table(table):
    length = len(table)
    print("it           |   xi          |   xm          |   xf          |   error")
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
    print("Ingrese el x0: ")
    a = input_float()
    print("Ingrese el xf: ")
    b = input_float()
    print("Ingrese la tolerancia: ")
    tol = input_float()
    relative_error = False
    while True:
        error_type = input("Qué tipo de error desea utilizar a) Error Absoluto, r) Error relativo").lower()
        if error_type == "a" or error_type == "a":
            relative_error = True
            break
        else:
            print("ingresaste un valor no válido")

    try:
        # Convertir la cadena de ecuación en una expresión simbólica
        fx = sp.sympify(input_equation)
        print("La ecuacion tomada es: ")
        print(fx)
        
    except sp.SympifyError:
        print("La ecuación ingresada no es válida.")


    #empieza el metodo
    iteracion = 0
    table = []
    errors = []

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
        e=abs(xm-a)
        if relative_error:
            e = e/xm
        row = str(iteracion) + "    |   " + str(a) + "  |   " + str(xm)+ "  |   " + str(b) + "  |   " + str(e)
        table.append(row)
        errors.append(e)
        iteracion+=1

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
            if relative_error:
                e = e/xm
            row = str(iteracion) + "    |   " + str(a) + "  |   " + str(xm)+ "  |   " + str(b) + "  |   " + str(e)
            table.append(row)
            errors.append(e)
            iteracion+=1

        
        if fm == 0:
            print(str(xm) + ' es una raiz')
            print_table(table)
        else:
            print(str(xm) + ' es una raiz con tolerancia de '+ str(e))
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


regla_falsa()