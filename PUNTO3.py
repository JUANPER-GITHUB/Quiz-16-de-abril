def sumaDigitos(numero):
    suma = 0
    while numero != 0:
        digito = numero % 10
        suma = suma + digito
        numero = numero // 10
    return suma
while True:
    num = int(input("Digite numeros menores que 10, se mostrara la suma cada vez, si desea terminar digite 0: "))
    if num != 0:
        print("Suma es igual a:", sumaDigitos(num))
        numcomotexto = str(num)
        print("La cantidad de digitos es: ", len(numcomotexto))
    else:
        print("Ha ingresado un 0 y el programa ha terminado")
        break
