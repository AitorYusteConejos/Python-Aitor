while True:
    try:
        peso = float(input("Introduce el peso en kg: "))

        if peso > 0:
            break
        else:
            print("El peso debe ser mayor que 0")

    except ValueError:
        print("Debes introducir un número")


print("Elige un destino entre una de las opciones")
print("" 
"1-América del norte | 24€\n" 
"2-América Central | 20€\n" 
"3-América del sur | 21€\n" 
"4-Europa | 10€\n" 
"5-Asia | 18€")



destinoCorrecto = False

while not destinoCorrecto:
    try:
        destino = int(input("Introduce el destino: "))

        match destino:
            case 1:
                precio = 24
                destinoCorrecto = True
            case 2:
                precio = 20
                destinoCorrecto = True
            case 3:
                precio = 21
                destinoCorrecto = True
            case 4:
                precio = 10
                destinoCorrecto = True
            case 5:
                precio = 18
                destinoCorrecto = True
            case _:
                print("La opción debe estar entre 1 y 5")

    except ValueError:
        print("Debes introducir un número")
costeEnvio = peso * precio

print("El envio saldra por: ", costeEnvio)