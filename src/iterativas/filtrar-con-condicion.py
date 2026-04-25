# Filtrar elementos usando una condición
pares = [x for x in range(10) if x % 2 == 0] # Utiliza una comprensión de listas para generar una nueva lista "pares" que contiene solo los números pares del 0 al 9. La función range(10) genera los números del 0 al 9, y la condición if x % 2 == 0 filtra solo aquellos números que son divisibles por 2 (es decir, los pares).
print(pares)  # [0, 2, 4, 6, 8] # Imprime la lista "pares" que contiene los números pares del 0 al 9.

# En este ejemplo, se utiliza una comprensión de listas para crear una nueva lista llamada "pares". La comprensión de listas es una forma concisa y eficiente de generar listas a partir de iterables. En este caso, se itera sobre los números del 0 al 9 utilizando la función range(), y para cada número x, se verifica si es par mediante la condición if x % 2 == 0. Si la condición se cumple, el número se incluye en la lista "pares". Finalmente, se imprime la lista resultante.

# Salida:
# [0, 2, 4, 6, 8]