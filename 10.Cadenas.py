nombre = "EVARISTO"
apellido = "Mendoza"
frase = "Las patitas de las moscas"

longitud = len(frase) #Nos cuenta los caracteres
print(longitud)

print(apellido[4]) #Extrae la letra correspondiente del apellido

palabras = frase.split() #Separa las palabras de una frase
print(palabras)

mayusculas = apellido.upper() #Transforma la frase en mayúsculas
print(mayusculas)

minusculas = nombre.lower() #Transforma la frase en minusculas
print(minusculas)

mensaje = "Hola, Mundo"
cambio = mensaje.replace("Hola", "Marco") #Cambia la palabra Hola de la frase por la palabra Marco
print(cambio)

for x in apellido:
    print(x)