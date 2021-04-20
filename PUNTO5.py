def frecuencia(numero, digito):
    cantidad = 0
    while numero != 0:
        ultDigito = numero % 10
        if ultDigito == digito:
            cantidad += 1
        numero = numero // 10
    return cantidad
print("Digite a continuación un número y después digite que número desea ver cuantas veces se repite en este: ")
num = int(input("Número: "))
un_digito = int(input("Dígito que desea saber cuantas veces se repite: "))
print("Frecuencia del dígito en el número:", frecuencia(num, un_digito))
