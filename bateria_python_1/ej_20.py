m2e = int(input("Introduce el numero de monedas de 2 euros: "))
m1e = int(input("Introduce el numero de monedas de 1 euro: "))
m50c = int(input("Introduce el numero de monedas de 50 centimos: "))
m20c = int(input("Introduce el numero de monedas de 20 centimos: "))
m10c = int(input("Introduce el numero de monedas de 10 centimos: "))

# Pasamos todo a céntimos para facilitar el cálculo
total_centimos = (m2e * 200) + (m1e * 100) + (m50c * 50) + (m20c * 20) + (m10c * 10)

# Obtenemos los euros y los céntimos restantes
euros = total_centimos // 100
centimos = total_centimos % 100

print("Tienes", euros, "euros y", centimos, "céntimos.")