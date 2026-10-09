while True:
    try:
        num = int(input("Introduce un numero: "))
        if num < 0:
            print("Introduce un numero positivo")
            continue
        break
    except ValueError:
        print("Debes introducir un numero")


cont = 0 
factorial = 1

while cont < num:
    cont = cont + 1
    factorial = factorial * cont

print("El factoriarl de ",num," es: ", factorial)