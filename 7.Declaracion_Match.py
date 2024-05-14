'''

numero = 3

match numero:
    case 1:
        print("Uno")
    case 2:
        print("Dos")
    case 3:
        print("Tres")
    case _:
        print("Número no reconocido")

'''

i_numero = int(input("Introduce un número entero: "))

match i_numero:
    case 0:
        print("El número es un cero")
    case i_numero if i_numero %  2 == 0:
        print("El número es par")
    case i_numero if i_numero % 2 != 0:
        print("El número es impar")
    case _:
        print("El número no se reconoce")