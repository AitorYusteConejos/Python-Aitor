caracter = input("Introduce un caracter: ")

while caracter != " ":
    if caracter.lower() in "aeiou":
        print("El caracter es una vocal")
    else:
        print("El caracter es una consonante")
    caracter = input("Introduce un caracter: ")