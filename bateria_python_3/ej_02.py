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

