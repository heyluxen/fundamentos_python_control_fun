# Función que obtiene un elemento de una lista por su índice
def obtener_elemento(lista, indice):
    """
    Obtiene un elemento de una lista por su índice.

    Args:
        lista: La lista de elementos
        indice: Posición del elemento a obtener (comienza en 0)

    Returns:
        El elemento en la posición especificada

    Raises:
        IndexError: Si el índice está fuera del rango de la lista
    """

    # Devuelve el elemento en la posición indicada
    return lista[indice]