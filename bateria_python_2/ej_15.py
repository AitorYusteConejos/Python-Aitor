alumnos = int(input("Ingrese el número de alumnos: "))

# Determinación de costos
if alumnos >= 100:
    costo_alumno = 65.0
    pago_compania = alumnos * costo_alumno
elif alumnos >= 50:
    costo_alumno = 70.0
    pago_compania = alumnos * costo_alumno
elif alumnos >= 30:
    costo_alumno = 95.0
    pago_compania = alumnos * costo_alumno
else:
    pago_compania = 4000.0
    costo_alumno = pago_compania / alumnos if alumnos > 0 else 0

print(f"\nPago a la compañía de autobuses: {pago_compania:.2f} €")
print(f"Costo que debe pagar cada alumno: {costo_alumno:.2f} €")