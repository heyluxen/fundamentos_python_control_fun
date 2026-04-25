def crear_lista_pares(maximo):  # Función que crea una lista de números pares
    return [num for num in range(2, maximo + 1, 2)]  # Genera números pares desde 2 hasta el máximo

def crear_diccionario_cuadrados(numeros):  # Función que crea un diccionario de cuadrados
    return {num: num ** 2 for num in numeros}  # Cada número es clave y su cuadrado es el valor

pares = crear_lista_pares(10)  # Genera lista de pares hasta 10
print(pares)  # Muestra la lista de números pares

cuadrados = crear_diccionario_cuadrados([1, 2, 3, 4])  # Crea diccionario de cuadrados
print(cuadrados)  # Muestra el diccionario con números y sus cuadrados

# Este ejemplo muestra cómo crear listas y diccionarios usando comprensión en Python, generando números pares y calculando cuadrados de una lista.

# Salida: 
# [2, 4, 6, 8, 10]
# {1: 1, 2: 4, 3: 9, 4: 16}