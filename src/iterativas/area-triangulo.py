# Función que calcula el área de un triángulo
def area_triangulo(base, altura):

    # Docstring: explica qué hace la función, qué recibe y qué devuelve
    """
    Calcula el área de un triángulo.

    Args:
        base: Longitud de la base del triángulo
        altura: Altura del triángulo

    Returns:
        El área del triángulo

    Ejemplos:
        >>> area_triangulo(4, 3)
        6.0
        >>> area_triangulo(5, 8)
        20.0
    """

    # Fórmula para calcular el área de un triángulo
    return (base * altura) / 2
import doctest
doctest.testmod()  # Ejecuta todos los ejemplos en los docstrings como pruebas