A = float(input("Introduce el lado A del triángulo: "))
B = float(input("Introduce el lado B del triángulo: "))
C = float(input("Introduce el lado C del triángulo: "))
pitagoras = (A**2 + B**2) ** 0.5
isosceles = A == B or A == C or B == C
if pitagoras == C:
    print("El triángulo es rectángulo.")
elif isosceles:
    print("El triángulo es isósceles.")
else:
    print("El triángulo es escaleno.")