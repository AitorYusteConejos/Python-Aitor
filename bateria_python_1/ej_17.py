hh = int(input("Introduce la hora de partida (HH): "))
mm = int(input("Introduce los minutos de partida (MM): "))
ss = int(input("Introduce los segundos de partida (SS): "))
t = int(input("Introduce el tiempo de viaje en segundos (T): "))

# 1. Convertir la hora de salida a segundos totales
segundos_iniciales = hh * 3600 + mm * 60 + ss

# 2. Sumar el tiempo de viaje
segundos_totales = segundos_iniciales + t

# 3. Convertir de nuevo a horas, minutos y segundos
horas_llegada = (segundos_totales // 3600) % 24
minutos_llegada = (segundos_totales % 3600) // 60
segundos_llegada = segundos_totales % 60

print("La hora de llegada es:", horas_llegada, "horas,", minutos_llegada, "minutos y", segundos_llegada, "segundos.")