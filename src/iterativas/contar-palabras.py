# Función que cuenta palabras en un texto
def contar_palabras(texto):
    """
    Cuenta el número de palabras en un texto.

    Args:
        texto (str): El texto a analizar

    Returns:
        int: El número de palabras encontradas
    """

    # Divide el texto en palabras y cuenta cuántas hay
    return len(texto.split())