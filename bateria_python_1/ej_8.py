sueldo = float(input("Introduce tu sueldo base: "))
ventas = []
res = input("has hecho alguna venta este mes: S/n ")
if res == "S":
    while True:
        venta = float(input("Introduce el valor de la venta: "))
        com_venta = venta * 0.10
        print("La comisión de esta venta es: ", com_venta, "€")
        ventas.append(com_venta)
        res = input("¿Deseas introducir otra venta? (S/n): ")
        if res.lower() != "s":
            break
total_comision = sum(ventas)
total_sueldo = sueldo + total_comision
print("Tu sueldo total este mes es: ", total_sueldo, "€")