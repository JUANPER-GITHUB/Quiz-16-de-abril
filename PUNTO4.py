agregar = "si"
def primo(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return False
while agregar == "si":
    numero = int(input("Ingrese un numero que desee que sea evaluado: "))
    if primo(numero):
        print("El numero " + str(numero) + " Si es primo")
    else:
        print("El numero " + str(numero) + " No es primo")
    agregar = input("¿Desea agregar otro numero para que sea evaluado si es primo o no?: ")
    if agregar == "no":
        print("El programa ha finalizado, que vuela pronto :)")
