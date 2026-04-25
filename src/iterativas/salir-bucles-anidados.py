encontrado = False  # Variable para controlar si se encontró el valor

for i in range(5):  # Recorre valores de 0 a 4
    for j in range(5):  # Recorre valores de 0 a 4
        if i * j > 10:  # Verifica si el producto es mayor a 10
            print(f"Valor encontrado: {i} * {j} = {i*j}")  # Muestra resultado
            encontrado = True  # Marca que se encontró
            break  # Sale del bucle interno

    if encontrado:  # Verifica si ya se encontró
        break  # Sale del bucle externo

# Este ejemplo busca el primer producto mayor a 10 y detiene ambos bucles.

# Salida:
# Valor encontrado: 3 * 4 = 12