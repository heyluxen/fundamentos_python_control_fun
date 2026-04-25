numeros = [1, 2, 0, 4, 0, 6, 7]  # Lista de números

for num in numeros:  # Recorre cada número
    if num == 0:  # Verifica si es cero
        print("Omitiendo división por cero")  # Evita error
        continue  # Salta ese caso

    resultado = 10 / num  # Realiza la división
    print(f"10 / {num} = {resultado}")  # Muestra el resultado

# Este ejemplo divide 10 entre cada número, evitando dividir por cero.

# Salida:
# 10 / 1 = 10.0
# 10 / 2 = 5.0
# Omitiendo división por cero
# 10 / 4 = 2.5
# Omitiendo división por cero
# 10 / 6 = 1.6666666666666667
# 10 / 7 = 1.4285714285714286