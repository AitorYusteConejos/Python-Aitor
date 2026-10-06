numero = int(input("Resultado del dado (1 a 6): "))

caras_opuestas = {
    1: "seis",
    2: "cinco",
    3: "cuatro",
    4: "tres",
    5: "dos",
    6: "uno"
}

if numero in caras_opuestas:
    print(f"La cara opuesta es: {caras_opuestas[numero]}")
else:
    print("ERROR: número incorrecto.")