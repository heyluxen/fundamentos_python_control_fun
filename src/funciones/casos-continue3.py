datos = ["25", "error", "42", "texto", "17"]  # Lista de valores (números y texto)

suma = 0  # Inicializa la suma
for valor in datos:  # Recorre cada elemento
    if not valor.isdigit():  # Verifica si no es numérico
        print(f"Valor no numérico ignorado: '{valor}'")  # Muestra mensaje
        continue  # Salta ese valor

    suma += int(valor)  # Convierte a entero y suma

print(f"La suma de los valores válidos es: {suma}")  # Muestra resultado

# Este ejemplo suma solo los valores numéricos e ignora los no válidos.

# Salida:
# Valor no numérico ignorado: 'error'
# Valor no numérico ignorado: 'texto'
# La suma de los valores válidos es: 84