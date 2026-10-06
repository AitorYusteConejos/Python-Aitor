numero = int(input("Ingrese un número del 1 al 7: "))

dias = {
    1: "Lunes",
    2: "Martes",
    3: "Miércoles",
    4: "Jueves",
    5: "Viernes",
    6: "Sábado",
    7: "Domingo"
}

if numero in dias:
    print(f"El día correspondiente es: {dias[numero]}")
else:
    print("ERROR: número incorrecto.")