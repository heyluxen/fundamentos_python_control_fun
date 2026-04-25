# Documentar el valor de retorno:
# Es importante dejar claro qué devuelve la función.

def calcular_descuento(precio, porcentaje):
    """
    Calcula el precio con descuento.

    Args:
        precio: El precio original
        porcentaje: El porcentaje de descuento (0-100)

    Returns:
        float: El precio después de aplicar el descuento
    """

    return precio - (precio * porcentaje / 100)  # Devuelve el precio final con descuento aplicado

# Este ejemplo muestra cómo documentar correctamente una función usando un docstring. Allí se explica qué recibe la función (precio y porcentaje) y qué devuelve (float con el precio final después del descuento), lo cual hace el código más claro y fácil de entender.