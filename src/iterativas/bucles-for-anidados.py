# Crear una matriz de multiplicación 3x3
for i in range(1, 4): # Bucle for externo que itera sobre los números del 1 al 3
    for j in range(1, 4): # Bucle for interno que itera sobre los números del 1 al 3
        print(f"{i} × {j} = {i*j}", end="\t") # Imprime la multiplicación de i y j en formato "i × j = resultado" y utiliza end="\t" para separar cada resultado con una tabulación
    print()  # Salto de línea después de cada fila

# En este ejemplo, se utilizan bucles for anidados para crear una matriz de multiplicación de 3x3. El bucle externo itera sobre los números del 1 al 3, y por cada número i, el bucle interno itera sobre los números del 1 al 3 para calcular la multiplicación de i y j. Los resultados se imprimen en formato "i × j = resultado" y se separan con una tabulación. Después de completar cada fila, se imprime un salto de línea para organizar la salida en forma de matriz.

# Salida:
# 1 × 1 = 1	 1 × 2 = 2	1 × 3 = 3
# 2 × 1 = 2	 2 × 2 = 4	2 × 3 = 6
# 3 × 1 = 3	 3 × 2 = 6	3 × 3 = 9