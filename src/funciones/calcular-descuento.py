def calcular_descuento(precio, porcentaje):  # Función para aplicar descuento con validación
    if not isinstance(precio, (int, float)) or precio < 0:  # Verifica precio válido
        raise ValueError("El precio debe ser un número positivo")  # Lanza error

    if not isinstance(porcentaje, (int, float)) or not (0 <= porcentaje <= 100):  # Verifica porcentaje
        raise ValueError("El porcentaje debe ser un número entre 0 y 100")  # Lanza error

    descuento = precio * (porcentaje / 100)  # Calcula descuento
    return precio - descuento  # Devuelve precio final

try:
    precio_final = calcular_descuento(100, 15)  # Caso válido
    print(f"Precio con descuento: {precio_final}")  # Muestra resultado

    precio_erroneo = calcular_descuento(-50, 10)  # Caso inválido
except ValueError as e:  # Captura el error
    print(f"Error: {e}")  # Muestra mensaje de error

# Este ejemplo valida datos antes de calcular un descuento y maneja errores con try/except.

# Salida: Precio con descuento: 85.0
# Error: El precio debe ser un número positivo