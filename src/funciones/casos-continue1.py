temperaturas = [22, -5, 28, 31, -15, 19, 26, -8]  # Lista de temperaturas

print("Temperaturas positivas:")  # Título

for temp in temperaturas:  # Recorre cada temperatura
    if temp <= 0:  # Verifica si es 0 o negativa
        continue  # Salta esas temperaturas

    print(f"{temp}°C")  # Muestra solo las positivas

# Este ejemplo imprime únicamente las temperaturas positivas de la lista.

# Salida:
#Temperaturas positivas:
# 22°C
# 28°C
# 31°C
# 19°C
# 26°C