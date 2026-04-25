def formato_nombre(nombre, apellido):  # Función que formatea un nombre completo
    return f"{apellido.upper()}, {nombre.capitalize()}"  # Apellido en mayúsculas y nombre con inicial en mayúscula

print(formato_nombre("ana", "garcía"))  # Muestra: GARCÍA, Ana

# Este ejemplo muestra cómo dar formato a un nombre, convirtiendo el apellido a mayúsculas y el nombre a formato capitalizado.

# Salida: 
# GARCÍA, Ana