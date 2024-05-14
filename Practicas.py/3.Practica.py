"""
Escribe un programa en Python que calcule el promedio de una lista de números. Debes seguir estos pasos:

    Crea una lista llamada numeros que contenga al menos cinco números enteros.

    Inicializa una variable llamada suma en 0.

    Utiliza un ciclo for para iterar a través de la lista numeros y suma cada número a la variable suma.

    Después del ciclo for, divide la variable suma entre la cantidad de números en la lista (que puedes obtener usando la función len(numeros)).

    Imprime el resultado como el promedio de los números en la lista.

"""



numeros = {7, 12, 66, 32, 99}
suma = 0

for num in numeros:
    suma += num

media = suma / len(numeros)
print("La media de la lista es: ", media)