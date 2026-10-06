mes = int(input("Ingrese el número del mes (1 al 12): "))

if mes in [1, 3, 5, 7, 8, 10, 12]:
    print("El mes tiene 31 días.")
elif mes in [4, 6, 9, 11]:
    print("El mes tiene 30 días.")
elif mes == 2:
    print("El mes tiene 28 días (o 29 si es año bisiesto).")
else:
    print("ERROR: número de mes incorrecto.")