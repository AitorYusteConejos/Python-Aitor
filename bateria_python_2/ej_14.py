tipo = input("Tipo de uva (A / B): ").strip().upper()
tamano = int(input("Tamaño (1 / 2): "))
precio = float(input("Precio inicial por kilo: "))
kilos = float(input("Cantidad de kilos: "))

if tipo == "A":
    if tamano == 1:
        precio += 0.20
    else:
        precio += 0.30
elif tipo == "B":
    if tamano == 1:
        precio -= 0.30
    else:
        precio -= 0.50

ganancia = precio * kilos

print(f"\nPrecio final por kilo: {precio:.2f}")
print(f"Ganancia total: {ganancia:.2f}")