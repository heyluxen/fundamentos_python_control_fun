numeros = [4, 6, 7, 8, 10]  # Lista de números (incluye un primo)

for num in numeros:  # Recorre cada número
    if num % 2 != 0 and num % 3 != 0:  # Verifica si podría ser primo
        print(f"¡Encontrado un primo: {num}!")  # Muestra el primo encontrado
        break  # Termina el bucle
else:  # Se ejecuta si no se encuentra ningún primo
    print("No se encontró ningún número primo en la lista")

# Este ejemplo encuentra el primer número primo en la lista y detiene el bucle.

# Salida:
# ¡Encontrado un primo: 7!