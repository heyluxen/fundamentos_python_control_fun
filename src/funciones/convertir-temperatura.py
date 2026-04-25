# Función que convierte temperaturas entre Celsius, Fahrenheit y Kelvin
def convertir_temperatura(valor, origen, destino):
    """
    Convierte una temperatura entre diferentes unidades.

    Args:
        valor: El valor de la temperatura a convertir
        origen: Unidad de origen ('C', 'F' o 'K')
        destino: Unidad de destino ('C', 'F' o 'K')

    Returns:
        float: La temperatura convertida, o None si los parámetros son inválidos
    """

    # Conjunto de unidades válidas
    unidades_validas = {'C', 'F', 'K'}

    # Validación: si alguna unidad no es válida, se detiene la función
    if origen not in unidades_validas or destino not in unidades_validas:
        return None

    # Si las unidades son iguales, no se necesita conversión
    if origen == destino:
        return valor

    # Conversión de la temperatura a Celsius como paso intermedio
    if origen == 'F':
        celsius = (valor - 32) * 5/9
    elif origen == 'K':
        celsius = valor - 273.15
    else:  # Si ya está en Celsius
        celsius = valor

    # Conversión desde Celsius a la unidad de destino
    if destino == 'F':
        return celsius * 9/5 + 32
    elif destino == 'K':
        return celsius + 273.15
    else:  # Si el destino es Celsius
        return celsius
    
# Ejemplos de uso de la función

print(convertir_temperatura(25, 'C', 'F'))    # 77.0
print(convertir_temperatura(98.6, 'F', 'C'))  # 37.0
print(convertir_temperatura(0, 'C', 'K'))     # 273.15
print(convertir_temperatura(20, 'X', 'Y'))    # None

# Salida: 
# 77.0
# 37.0
# 273.15
# None