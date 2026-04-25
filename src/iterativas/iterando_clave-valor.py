usuario = {"nombre": "Laura", "edad": 28, "ciudad": "Madrid"} # Diccionario con información de un usuario

# Iterando sobre pares clave-valor
for clave, valor in usuario.items(): # Bucle for que itera sobre los pares clave-valor del diccionario "usuario" utilizando el método items()
    print(f"{clave}: {valor}") # Imprime cada clave y su valor correspondiente en cada iteración del bucle utilizando la sintaxis de formato de cadenas

# En este ejemplo, el bucle for utiliza el método items() del diccionario "usuario" para obtener tanto las claves como los valores en cada iteración. La variable "clave" se asigna a la clave actual y la variable "valor" se asigna al valor correspondiente. Luego, se imprime cada clave y su valor utilizando la sintaxis de formato de cadenas.

# Salida:
# nombre: Laura
# edad: 28
# ciudad: Madrid
