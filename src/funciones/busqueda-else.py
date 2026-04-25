def buscar_usuario(usuarios, nombre):  # Función para buscar un usuario
    for usuario in usuarios:  # Recorre la lista de usuarios
        if usuario["nombre"] == nombre:  # Verifica si coincide el nombre
            print(f"Usuario encontrado: {usuario}")  # Muestra el usuario
            return usuario  # Devuelve el usuario encontrado
    else:  # Si no lo encuentra
        print(f"Usuario '{nombre}' no encontrado, creando nuevo perfil...")  # Mensaje
        nuevo_usuario = {"nombre": nombre, "nivel": 1}  # Crea nuevo usuario
        usuarios.append(nuevo_usuario)  # Lo agrega a la lista
        return nuevo_usuario  # Devuelve el nuevo usuario

base_usuarios = [
    {"nombre": "Ana", "nivel": 5},
    {"nombre": "Carlos", "nivel": 3}
]  # Lista de usuarios

buscar_usuario(base_usuarios, "Ana")  # Busca un usuario existente
buscar_usuario(base_usuarios, "Roberto")  # Busca y crea uno nuevo

# Este ejemplo busca un usuario y, si no existe, lo crea automáticamente.
#Usuario encontrado: {'nombre': 'Ana', 'nivel': 5}
#Usuario 'Roberto' no encontrado, creando nuevo perfil...