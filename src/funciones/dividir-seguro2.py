# Función que realiza una división de forma segura
def dividir_seguro(a, b):

    # Docstring: explica qué hace la función, qué recibe y qué devuelve
    """
    Realiza una división segura entre dos números.

    Args:
        a: El numerador
        b: El denominador

    Returns:
        El resultado de la división a/b, o None si b es cero

    Ejemplo:
        >>> dividir_seguro(10, 2)
        5.0
        >>> dividir_seguro(10, 0)
        None
    """

    # Si el denominador es 0, no se puede dividir
    if b == 0:
        return None  # Devuelve None para evitar error

    # Si es válido, realiza la división
    return a / b