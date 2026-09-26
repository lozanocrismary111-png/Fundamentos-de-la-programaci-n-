# Programa de agenda de contactos usando un diccionario (Mapa)
# clave = nombre, valor = número de teléfono
agenda = {} 

# Insertar datos
agenda["Ana"] = "0991234567"
agenda["Luis"] = "0987654321"
agenda["Maria"] = "0965432189"

print("Contactos guardados:")
for nombre, telefono in agenda.items():
    print(nombre, "->", telefono)

# Buscar un contacto
nombre_buscado = "Luis"
if nombre_buscado in agenda:
    print("Teléfono de", nombre_buscado, ":", agenda[nombre_buscado])
else:
    print(nombre_buscado, "no está en la agenda")

# Eliminar un contacto
agenda.pop("Maria")
print("Agenda después de eliminar a Maria:")
for nombre, telefono in agenda.items():
    print(nombre, "->", telefono)