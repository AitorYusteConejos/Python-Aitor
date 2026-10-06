varA = float(input("ingresa un numero: "))
varB = float(input("ingresa otro numero: "))

varC = varB
varB = varA
varA = varC

print("El valor actual de la variable A es: ", varA)
print("El valor actual de la variable B es: ", varB)