def mostrar_informacion(**datos):  # Función que recibe datos por nombre
    for clave, valor in datos.items():  # Recorre cada par clave-valor
        print(f"{clave}: {valor}")  # Muestra la información

# Uso con argumentos por nombre
mostrar_informacion(nombre="Python", creador="Guido van Rossum", año=1991)

# Este ejemplo muestra cómo usar **kwargs para manejar múltiples datos con nombre.

# Salida: 
# nombre: Python
# creador: Guido van Rossum
# año: 1991