"""
Escribe un programa Python que solicite al usuario ingresar un número entero
 y luego determine en qué rango se encuentra ese número utilizando la declaración 
 match. El programa debe imprimir un mensaje que indique el rango al que pertenece el número.

"""

numero = int(input("Introduce un número entero de 0 a 100: "))

match numero:
    case numero if numero <=30:
        print("Estas entre los 30 primeros números")
    case numero if numero <=60:
        print("Estas entre el 30 y 60")
    case numero if numero <=90:
        print("EStas entre el 60 y 90")
    case _:
        print("Estas entre el 90 y 100")
        