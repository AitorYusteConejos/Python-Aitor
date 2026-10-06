correctas = int(input("Introduce el numero de respuestas correctas: "))
incorrectas = int(input("Introduce el numero de respuestas incorrectas: "))
en_blanco = int(input("Introduce el numero de respuestas en blanco: "))

nota_final = (correctas * 5) + (incorrectas * -1) + (en_blanco * 0)

print("La nota final del estudiante es:", nota_final, "puntos.")