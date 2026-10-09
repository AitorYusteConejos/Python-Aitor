x1 = float(input("Introduce la x del primer punto: "))
y1 = float(input("Introduce la y del primer punto: "))
r1 = float(input("Introduce el radio del primer círculo: "))
x2 = float(input("Introduce la x del segundo punto: "))
y2 = float(input("Introduce la y del segundo punto: "))
r2 = float(input("Introduce el radio del segundo círculo: "))

distancia = ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5

if distancia > (r1 + r2):
    print("Son circunferencias exteriores.")
elif distancia == (r1 + r2):
    print("Son circunferencias tangentes exteriores.")
elif abs(r1 - r2) < distancia < (r1 + r2):
    print("Son circunferencias secantes.")
elif distancia == abs(r1 - r2) and distancia > 0:
    print("Son circunferencias tangentes interiores.")
elif 0 < distancia < abs(r1 - r2):
    print("Son circunferencias interiores.")
elif distancia == 0:
    print("Son circunferencias concéntricas.")