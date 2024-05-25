import sympy as sp

def print_table(table):
    length = len(table)
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
        
def busquedas():
    # Solicitar al usuario que ingrese la ecuación
    input_equation = input("Ingrese la ecuación en terminos de x: ")
    # Crear un símbolo para la variable en la ecuación
    x = sp.symbols('x')

    #Solicitar demás input
    print("Ingrese el x0 (número): ")
    x0 = input_float()
    print("Ingrese el tamaño del intervalo: ")
    deltax = input_float()
    print("Ingrese el numero maximo de iteraciones: ")
    max_ite = input_int()


    try:
        # Convertir la cadena de ecuación en una expresión simbólica
        fx = sp.sympify(input_equation)
        print("La ecuacion tomada es: ")
        print(fx)
        
    except sp.SympifyError:
        print("La ecuación ingresada no es válida.")

    #inicializacion de variables
    xf = 0
    fa = 0
    fb = 0
    it = 1
    evaluations = [] #arreglo para guardar los resultados y mostrar la tabla al final

    fa = fx.subs(x, x0)
    evaluations.append(str(0) + "    |    " + str(x0) + "      |       "  + str(fa))
    #verificamos que fa no sea raiz
    if fa == 0:
        print("\n\n\n")
        print(str(x0) + " es una raiz")
    else:
        xf = x0 + deltax
        fb = fx.subs(x, xf)
        evaluations.append(str(1) + "    |    " + str(xf) + "      |       "  + str(fb))
        
        while it<max_ite and fa*fb > 0:
            fa = fb
            xf+=deltax
            fb = fx.subs(x, xf)
            row = str(it+1) + "    |    " + str(xf) + "      |       "  + str(fb)
            evaluations.append(row)
            it+=1
        
        print("\n\n\n")
        if fa*fb <= 0:
            if fb == 0:
                print(str(xf) + ' es una raiz')
                print_table(evaluations)
            else:
                print("Entre "+ str(xf-deltax) + " y " + str(xf) + " hay una raiz")
                print_table(evaluations)
        else:
            print("Se superó el número de iteraciones")
            print_table(evaluations)






busquedas()