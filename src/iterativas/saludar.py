def saludar(nombre, mensaje="¡Bienvenido!"):  # Función con parámetro por defecto
    print(f"Hola {nombre}. {mensaje}")  # Muestra saludo

saludar("Carlos")  # Usa el mensaje por defecto
saludar("María", "¿Cómo estás hoy?")  # Usa mensaje personalizado

# Este ejemplo muestra el uso de parámetros con valores por defecto.

# Salida: 
# Hola Carlos. ¡Bienvenido! 
# Hola María. ¿Cómo estás hoy?
