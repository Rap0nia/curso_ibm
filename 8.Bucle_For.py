"""

frutas = ["manzana", "pera", "cereza"]
contador = 0

#Bucle for que itera sobre la lista de frutas
for fruta in frutas:
    contador += 1
    print(f"Fruta #{contador}: {fruta}")
    if fruta == "pera":
        break

"""

numero = [1,2,3,4,5]

for num in numero:
    cuadrado = num ** 2
    print(f"El cuadrado de {num} es {cuadrado}")
    