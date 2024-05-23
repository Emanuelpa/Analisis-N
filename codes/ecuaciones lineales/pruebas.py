import sympy as sp
# Solicitar al usuario que ingrese la ecuación
input_equation_ = input("Ingrese la ecuación g(x) en terminos de x: ")
# Crear un símbolo para la variable en la ecuación
x = sp.symbols('x')

#Solicitar demás input




    # Convertir la cadena de ecuación en una expresión simbólica
equation_ = sp.sympify(input_equation_, locals={'ln': sp.log})
print("La ecuacion tomada es g(x)= " + str(equation_))

    
