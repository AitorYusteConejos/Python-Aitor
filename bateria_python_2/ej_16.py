minutos = int(input("Duración de la llamada (minutos): "))
dia = input("Día de la semana: ").strip().lower()

# Cálculo del costo base acumulado por tramos
if minutos <= 5:
    costo_base = minutos * 1.00
elif minutos <= 8:
    costo_base = (5 * 1.00) + ((minutos - 5) * 0.80)
elif minutos <= 10:
    costo_base = (5 * 1.00) + (3 * 0.80) + ((minutos - 8) * 0.70)
else:
    costo_base = (5 * 1.00) + (3 * 0.80) + (2 * 0.70) + ((minutos - 10) * 0.50)

# Cálculo de impuestos según el día y turno
if dia == "domingo":
    impuesto_pct = 0.03
else:
    turno = input("Turno (mañana / tarde): ").strip().lower()
    if turno in ["mañana", "manana"]:
        impuesto_pct = 0.15
    else:
        impuesto_pct = 0.10

impuesto = costo_base * impuesto_pct
total = costo_base + impuesto

# Resultados desglosados por concepto
print(f"\nCosto base de la llamada: {costo_base:.2f} €")
print(f"Impuesto aplicado ({int(impuesto_pct * 100)}%): {impuesto:.2f} €")
print(f"Total a pagar: {total:.2f} €")