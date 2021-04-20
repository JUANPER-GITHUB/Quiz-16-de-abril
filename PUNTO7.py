def sumaDigitos(numero):
  suma = 0
  while numero != 0:
      digito = numero % 10
      suma = suma + digito
      numero = numero // 10
  return suma
cantidad = 0
mayor = -1
agregar = "si"
while agregar == "si":
    numero = int(input("Ingrese un número positivo: "))
    if numero >= 0:
        suma=sumaDigitos(numero)
        if suma > mayor:
              mayor = suma
              n_mayorsuma = numero
        if suma < 10:
            cantidad = cantidad + 1
        print("Sumatoria de dígitos de", n_mayorsuma, "es =", mayor)
        print("Cantidad con sumatoria menor a 10 es =", cantidad)
        agregar = input("¿Desea ingresar otro número? si o no = ")
        if agregar == "no":
            print("Se ha terminado de ejecutar correctamente el programa.")
            break
    else:
        print("El número ingresado no puede ser negativo, vuelva a ingresar números.")
        agregar == "si"
