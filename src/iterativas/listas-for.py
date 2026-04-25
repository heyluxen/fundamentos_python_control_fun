# Crear una lista con los cuadrados de los números del 1 al 5
cuadrados = [x**2 for x in range(1, 6)] # Utiliza una comprensión de listas para generar una nueva lista "cuadrados" que contiene el resultado de elevar al cuadrado cada número generado por range(1, 6). La función range(1, 6) genera los números del 1 al 5 (excluyendo el 6), y la expresión x**2 calcula el cuadrado de cada número.
print(cuadrados)  # [1, 4, 9, 16, 25] # Imprime la lista "cuadrados" que contiene los cuadrados de los números del 1 al 5.

# En este ejemplo, se utiliza una comprensión de listas para crear una nueva lista llamada "cuadrados". La comprensión de listas es una forma concisa y eficiente de generar listas a partir de iterables. En este caso, se itera sobre los números del 1 al 5 utilizando la función range(), y para cada número x, se calcula su cuadrado (x**2) y se agrega a la lista "cuadrados". Finalmente, se imprime la lista resultante.

# Salida:
# [1, 4, 9, 16, 25]