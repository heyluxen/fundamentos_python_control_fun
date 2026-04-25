# Función que genera una contraseña aleatoria
def generar_contraseña(longitud=8):

    # Docstring: explica qué hace la función, qué recibe y qué devuelve
    """
    Genera una contraseña aleatoria.

    Args:
        longitud: Número de caracteres de la contraseña (predeterminado: 8)

    Returns:
        Una cadena con la contraseña generada
    """

    # Importa librerías necesarias
    import random  # Para elegir caracteres aleatorios
    import string  # Para usar letras, números y símbolos

    # Conjunto de caracteres permitidos en la contraseña
    caracteres = string.ascii_letters + string.digits + string.punctuation

    # Genera la contraseña eligiendo caracteres aleatorios según la longitud
    return ''.join(random.choice(caracteres) for _ in range(longitud))