usuario = {"nombre": "Laura", "edad": 28, "ciudad": "Madrid"} # Diccionario con información de un usuario

# Iterando sobre claves
for clave in usuario: # Bucle for que itera sobre las claves del diccionario "usuario"
    print(f"Clave: {clave}, Valor: {usuario[clave]}") # Imprime la clave y su valor correspondiente en cada iteración del bucle utilizando la sintaxis de formato de cadenas

# En este ejemplo, el bucle for recorre cada clave del diccionario "usuario" y la asigna a la variable "clave". Luego, se imprime la clave y su valor correspondiente utilizando la sintaxis de formato de cadenas. Al acceder al valor del diccionario, se utiliza la clave entre corchetes (usuario[clave]) para obtener el valor asociado a esa clave.

# Salida:
# Clave: nombre, Valor: Laura
# Clave: edad, Valor: 28
# Clave: ciudad, Valor: Madrid