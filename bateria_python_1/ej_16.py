d = float(input("introduce la distancia entre los vehiculos: "))
v1 = float(input("introduce la velocidad del primer vehiculo: "))
v2 = float(input("introduce la velocidad del segundo vehiculo: "))
if v2 <= v1 :
    print("Error, la velociadad del segundo debe ser mayor que la del primero.")
else:
    tiempo_total_horas = d / (v2-v1)

    horas = int(tiempo_total_horas)
    minutos = int((tiempo_total_horas - horas) * 60)


    print("el tiempo que tardara en alcanzarlo es de ",horas," horas y ",minutos," minutos")
