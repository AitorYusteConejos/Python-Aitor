anio = int(input("Introduce un anio: "))
mes = int(input("Introduce el mes: "))
dia = int(input("Introduce el dia: "))

if mes == 2:
    if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
        if dia <= 29:
            print("La fecha es correcta.")
        else:
            print("La fecha es incorrecta.")
    else:
        if dia <= 28:
            print("La fecha es correcta.")
        else:
            print("La fecha es incorrecta.")
elif mes in [4, 6, 9, 11]:
    if dia <= 30:
        print("La fecha es correcta.")
    else:
        print("La fecha es incorrecta.")
elif mes in [1, 3, 5, 7, 8, 10, 12]:
    if dia <= 31:
        print("La fecha es correcta.")
    else:
        print("La fecha es incorrecta.")
