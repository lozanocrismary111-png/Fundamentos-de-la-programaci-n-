def calcular(numero, opcion):
    if opcion == "doble":
      resultado = numero * 2
    elif opcion == "triple":
      resultado = numero * 3
    else:
        resultado = None
    return resultado

if __name__ == "__main__":
     valor = calcular(100, "triple")
     print("El resultado es:", valor)
     if valor is None:
       print("Error, por favor ingrese calculo de doble o triple.")
