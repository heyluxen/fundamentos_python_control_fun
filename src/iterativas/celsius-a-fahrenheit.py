# Función que convierte Celsius a Fahrenheit
def celsius_a_fahrenheit(celsius):  # Recibe temperatura en Celsius
    return (celsius * 9/5) + 32  # Aplica la conversión

# Este ejemplo convierte una temperatura de grados Celsius a Fahrenheit.
# Asignar una función a una variable
convertir = celsius_a_fahrenheit
temperatura_f = convertir(25)  # Equivalente a celsius_a_fahrenheit(25)
print(f"25°C equivalen a {temperatura_f}°F")  

# Salida: 
# 25°C equivalen a 77.0°F