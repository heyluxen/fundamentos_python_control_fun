def crear_usuario(nombre, apellido, edad, email, activo=True):  # Función para crear un usuario
    return {
        "nombre_completo": f"{nombre} {apellido}",  # Une nombre y apellido
        "edad": edad,  # Guarda la edad
        "email": email,  # Guarda el email
        "activo": activo  # Estado del usuario
    }

# Uso con argumentos por nombre (más claro)
usuario = crear_usuario(
    nombre="Juan",
    apellido="Pérez",
    edad=28,
    email="juan@ejemplo.com",
    activo=False
)

# Este ejemplo crea un usuario usando argumentos por nombre para mayor claridad.