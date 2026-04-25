# Función que filtra los números pares de una lista
def filtrar_pares(lista):
    
    # Docstring: explica qué hace la función, qué recibe y qué devuelve
    """
    Filtra los números pares de una lista.

    Parameters
    ----------
    lista : list
        Lista de números enteros

    Returns
    -------
    list
        Nueva lista que contiene solo los números pares
    """
    
    # Recorre la lista y se queda solo con los números que sean divisibles entre 2
    return [num for num in lista if num % 2 == 0]