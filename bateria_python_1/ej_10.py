parcial1 = float(input("ingrese su primera nota parcial "))
parcial2 = float(input("ingrese su segunda nota parcial "))
parcial3 = float(input("ingrese su tercera nota parcial "))


nota1 = float(((parcial1+parcial2+parcial3)/3))
nota2 = float(input("ingrese su nota del examen final"))
nota3 = float(input("ingrese la nota de su trabajo final"))

nota_Final = float((nota1 * 0.55)+(nota2*0.30)+(nota3*0.15))

print("Tu nota final es de, ",nota_Final)