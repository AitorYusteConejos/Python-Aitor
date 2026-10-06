print("Introduce las coordenadas del primer punto:")
x1 = float(input("x1: "))
y1 = float(input("y1: "))

print("Introduce las coordenadas del segundo punto:")
x2 = float(input("x2: "))
y2 = float(input("y2: "))

distancia = ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5

print("La distancia entre los dos puntos es: ", distancia)