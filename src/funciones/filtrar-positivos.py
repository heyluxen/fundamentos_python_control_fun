# Función que filtra números positivos de una lista
def filtrar_positivos(numeros):
    # Verifica si el dato recibido es una lista
    if not isinstance(numeros, list):
        return []  # Si no es lista, devuelve una lista vacía

    # Filtra y devuelve solo los números mayores a 0
    return [num for num in numeros if num > 0]

# Este ejemplo muestra cómo filtrar únicamente números positivos de una lista, y cómo manejar errores devolviendo una lista vacía si el dato no es válido.