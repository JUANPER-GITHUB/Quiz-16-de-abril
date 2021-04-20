def validar(email):
    caracterBuscado="@"
    emailValido=False
    for c in email:
        if c==caracterBuscado:
            return True
    return False
direccion=input("Ingrese su dirección de correo electronico: ")
if validar(direccion):
    print("¡La dirección de correo electrónico que fue ingresada es válida!")
else:
    print("La dirección de correo electrónico que ingreso no es válida, por favor inténtelo más tarde.")
