# Iterando solo sobre valores
usuario = {"nombre": "Laura", "edad": 28, "ciudad": "Madrid"} # Diccionario con información de un usuario

for valor in usuario.values(): # Bucle for que itera sobre los valores del diccionario "usuario" utilizando el método values()
    print(valor) # Imprime cada valor del diccionario en cada iteración del bucle utilizando la sintaxis de formato de cadenas

# En este ejemplo, el bucle for utiliza el método values() del diccionario "usuario" para iterar solo sobre los valores del diccionario. La variable "valor" se asigna a cada valor del diccionario en cada iteración del bucle, y luego se imprime utilizando la sintaxis de formato de cadenas.

# Salida:
# Laura
# 28
# Madrid