numeros = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]  # Lista de números
limite = 50  # Límite máximo
suma = 0  # Inicializa la suma

for num in numeros:  # Recorre cada número
    if num % 3 == 0:  # Verifica si es múltiplo de 3
        print(f"Omitiendo {num} (múltiplo de 3)")  # Muestra mensaje
        continue  # Salta ese número

    suma += num  # Suma el número
    print(f"Añadiendo {num}: suma = {suma}")  # Muestra la suma

    if suma > limite:  # Verifica si supera el límite
        print(f"Límite de {limite} superado")  # Muestra mensaje
        break  # Termina el bucle

# Este ejemplo suma números ignorando múltiplos de 3 y se detiene al superar un límite.

# Salida:
# Añadiendo 1: suma = 1
# Omitiendo 3 (múltiplo de 3)
# Añadiendo 5: suma = 6
# Añadiendo 7: suma = 13
# Omitiendo 9 (múltiplo de 3)
# Añadiendo 11: suma = 24
# Añadiendo 13: suma = 37
# Omitiendo 15 (múltiplo de 3)
# Añadiendo 17: suma = 54
# Límite de 50 superado