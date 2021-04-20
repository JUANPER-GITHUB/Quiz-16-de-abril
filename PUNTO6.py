def factorial(numero):
   f = 1
   if numero != 0:
       for i in range(1, numero + 1):
           f = f * i
   return f
cantidad = 0
num = int(input("Ingrese un número del cual desee conocer su factorial, si ya no desea ingresar mas numeros ingrese el numero -50: "))
while num != -50:
    print("El número factorial de" + " " + str(num) + " es = " + str(factorial(num)))
    cantidad = cantidad + 1
    num = int(input("Ingrese un número del cual desee conocer su factorial, si ya no desea ingresar mas numeros ingrese el numero -50: "))
print("Se leyeron", cantidad, "números")
