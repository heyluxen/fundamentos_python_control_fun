usuarios = [
    {"nombre": "Ana", "rol": "admin"},
    {"nombre": "Luis", "rol": "usuario"},
    {"nombre": "Marta", "rol": "moderador"}
] # Aquí se define una estructura de datos en forma de lista, donde cada elemento es un diccionario con un nombre y un rol.

for usuario in usuarios: # Se itera sobre cada usuario en la lista de usuarios utilizando un bucle for.
    match usuario:
        case {"rol": "admin"}:
            print(f"{usuario['nombre']} tiene permisos de administrador.") # Si el rol del usuario es "admin", se muestra un mensaje indicando que el usuario tiene permisos de administrador.
        case {"rol": "moderador"}:
            print(f"{usuario['nombre']} puede moderar contenidos.") # Si el rol del usuario es "moderador", se muestra un mensaje indicando que el usuario puede moderar contenidos.
        case {"rol": "usuario"}:
            print(f"{usuario['nombre']} es un usuario regular.") # Si el rol del usuario es "usuario", se muestra un mensaje indicando que el usuario es un usuario regular.
        case _:
            print(f"Rol de {usuario['nombre']} desconocido.") # Y si el rol del usuario no coincide con ninguno de los casos anteriores, se muestra un mensaje indicando que el rol del usuario es desconocido.

# En la salida se muestra el nombre y un mensaje para cada usuario indicando su rol y los permisos asociados a ese rol.

# Salida:
# Ana tiene permisos de administrador.
# Luis es un usuario regular.
# Marta puede moderar contenidos.
