nota = float(input("Introduce tu nota: "))
edad = int(input("Introduce tu edad: "))
sexo = input("Introduce tu sexo (F/M): ").strip().upper()

if nota >= 5 and edad >= 18:
    if sexo == 'F':
        print("ACEPTADA")
    elif sexo in ('M', 'H'):
        print("POSIBLE")
    else:
        print("NO ACEPTADA")
else:
    print("NO ACEPTADA")