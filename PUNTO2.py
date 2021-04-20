def sumaDigitos(numero):
    suma = 0
    while numero != 0:
        digito = numero % 10
        suma = suma + digito
        numero = numero // 10
    return suma
num = int(input("Digite numeros menores que 10, se mostrara la suma cada vez, si desea terminar digite 0: "))
while num != 0:
    print("Suma es igual a:", sumaDigitos(num))
    num = int(input("Digite numeros menores que 10, se mostrara la suma cada vez, si desea terminar digite 0: "))
