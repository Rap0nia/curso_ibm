# persona = {
#     "nombre": "Juan",
#     "edad": 30,
#     "ciudad": "Madrid"
# }

# perfil = persona

# print(perfil["nombre"])

personas = {
    "persona1":{
        "nombre": "Juan",
        "edad": 30,
        "ciudad": "Cuenca"

    },

    "persona2":{
        "nombre": "Maria",
        "edad": 33,
        "ciudad": "Alcoy"
    },

    "persona3":{
        "nombre": "Barritos",
        "edad": 42,
        "ciudad": "Cerceda"
    }

}

datos = personas["persona1"]
datos2 = personas["persona2"]

print(datos["nombre"])
print(datos2["nombre"])