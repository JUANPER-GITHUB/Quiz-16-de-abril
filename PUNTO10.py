def ultimaPalabra(cadena):
   if len(cadena) == 0:
       return 0
   cantidad = 0
   for i in range(len(cadena)):
       if cadena[i]!=' ':
           cantidad = cantidad + 1
       else:
           if i < len(cadena)-1 and cadena[i+1] != ' ':
               cantidad = 0
   return cantidad
cadena = input("Ingrese la cadena o frase = ")
if ultimaPalabra(cadena):
    print(ultimaPalabra(cadena))
