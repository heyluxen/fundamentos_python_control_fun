# Buscar un número primo en una lista
numeros = [4, 6, 8, 9, 10, 12]  # Lista de números

for num in numeros:  # Recorre cada número
    if num % 2 != 0 and num % 3 != 0:  # Verifica si podría ser primo
        print(f"¡Encontrado un primo: {num}!")  # Muestra mensaje
        break  # Termina el bucle si lo encuentra
else:  # Se ejecuta si no se rompe el bucle
    print("No se encontró ningún número primo en la lista")  # Muestra mensaje

# Este ejemplo busca un número primo y usa else si no encuentra ninguno.

# Salida:
# No se encontró ningún número primo en la lista