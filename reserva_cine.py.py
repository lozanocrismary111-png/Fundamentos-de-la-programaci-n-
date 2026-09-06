# Crear la matriz de asientos (3 filas x 4 columnas), todos libres (valor 0)
asientos = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]

# Pedir al usuario la fila y columna del asiento a reservar
fila = int(input("Ingrese fila (0 a 2): "))
columna = int(input("Ingrese columna (0 a 3): "))

# Marcar el asiento como reservado
asientos[fila][columna] = 1
print("Estado de la sala:")

# Recorrer cada fila y columna
for fila_actual in range(len(asientos)):
    for columna_actual in range(len(asientos[fila_actual])):
        print(asientos[fila_actual][columna_actual], end=" ")
    print() 