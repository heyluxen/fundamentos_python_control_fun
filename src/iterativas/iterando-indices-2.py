nombres = ["Ana", "Carlos", "Elena"] # Lista de nombres
for indice, nombre in enumerate(nombres): # Bucle for que itera sobre los índices y nombres de la lista de nombres utilizando enumerate()
    print(f"Posición {indice}: {nombre}") # Imprime la posición (índice) y el nombre correspondiente en cada iteración del bucle utilizando la sintaxis de formato de cadenas

# En este ejemplo, el bucle for utiliza la función enumerate() para iterar sobre la lista "nombres". La función enumerate() devuelve tanto el índice como el valor de cada elemento en la lista. En cada iteración del bucle, se imprime la posición (índice) y el nombre correspondiente utilizando la sintaxis de formato de cadenas.

# Salida:
# Posición 0: Ana
# Posición 1: Carlos
# Posición 2: Elena