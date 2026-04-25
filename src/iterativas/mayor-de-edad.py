def es_mayor_de_edad(edad):  # Función que verifica si una persona es mayor de edad
    return edad >= 18  # Devuelve True si la edad es 18 o más, si no False

def es_correo_valido(email):  # Función que valida un correo electrónico
    return "@" in email and "." in email  # Verifica que tenga @ y punto

# Uso de las funciones en una condición
usuario_edad = 16  # Edad del usuario

if es_mayor_de_edad(usuario_edad):  # Si es mayor de edad
    print("Acceso permitido")  # Muestra este mensaje si cumple la condición
else:
    print("Acceso denegado")  # Muestra este mensaje si no cumple la condición

# Salida: 
# Acceso denegado

# Este ejemplo muestra cómo usar funciones que devuelven valores booleanos (True o False) para tomar decisiones en un programa usando condicionales.