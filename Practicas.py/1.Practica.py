"""
Eres un profesor y deseas crear un programa en Python para evaluar las calificaciones de los estudiantes. El programa debe solicitar 
al usuario que ingrese su calificación como un número decimal. Luego, debe mostrar un mensaje que refleje su rendimiento de acuerdo con
 ciertos criterios:


    Si la calificación es igual o mayor a 90, mostrar "¡Felicidades! Has aprobado con una calificación sobresaliente."

    Si la calificación es igual o mayor a 70 pero menor que 90, mostrar "Has aprobado satisfactoriamente."

    Si la calificación es igual o mayor a 60 pero menor que 70, mostrar "Has aprobado, pero necesitas mejorar un poco."

    Si la calificación es menor que 60, mostrar "Lo siento, has suspendido. Debes esforzarte más en la próxima evaluación."

"""

nota = float(input("Introduce tu nota: "))


if nota >= 9:
    print("Has aprobado con una calificación Sobresaliente")
elif nota >= 7:
    print("Has aprobado satisfactoriamente")
elif nota >= 6:
    print("Las aprobado, pero necesitas mejorar")
else:
    print("Has suspendido.Debes esforzarte más en la próxima")