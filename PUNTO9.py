cond = "si"
def frecuencia(numero):
    cantidad = 0
    while numero != 0:
        ultDigito = numero%10
        cantidad = cantidad + 1
        numero = numero // 10
    return cantidad
while cond == "si":
    hi=input("""que desea ingresar:
    1.Cedula de ciudadania
    2.Tarjeta de identidad	
      = """)
    num = int(input("Ingrese el número: "))
    if frecuencia(num) < 4 and frecuencia(num) < 12:
        print("el numero  es invalido")
    else:
        print("El número es valido.")
        cond = "no"
    cond = input("¿Desea volver a ingresar?:: ")
    if cond == "no":
        print("Programa finalizado con exito.")
