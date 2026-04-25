# Función que calcula el promedio de una lista de números
def calcular_promedio(numeros):
    """
    Calcula el promedio de una lista de números.

    Suma todos los números de la lista y divide el resultado
    entre la cantidad de elementos.

    Args:
        numeros: Una lista de valores numéricos

    Returns:
        El promedio como valor flotante

    Ejemplo:
        >>> calcular_promedio([1, 2, 3, 4])
        2.5
    """

    return sum(numeros) / len(numeros)  # Calcula y devuelve el promedio

# Este ejemplo muestra una función que calcula el promedio de una lista de números. Suma todos los valores y los divide entre la cantidad de elementos, devolviendo un resultado en tipo decimal (float).

# Acceder al docstring (documentación interna de la función)
print(calcular_promedio.__doc__)  # Muestra el texto de ayuda de la función

# Usar help para ver la documentación completa de la función
help(calcular_promedio)  # Muestra información detallada de la función

# Este ejemplo muestra dos formas de ver la documentación de una función en Python. La primera (.__doc__) imprime solo el texto del docstring, y la segunda (help()) muestra una explicación más completa con formato.