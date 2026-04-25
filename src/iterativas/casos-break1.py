def buscar_elemento(lista, objetivo):  # Función para buscar un elemento en una lista
    for indice, elemento in enumerate(lista):  # Recorre la lista con índice y valor
        if elemento == objetivo:  # Verifica si es el elemento buscado
            return indice  # Devuelve la posición si lo encuentra

    return -1  # Devuelve -1 si no está en la lista

numeros = [4, 7, 2, 9, 1, 5]  # Lista de números
posicion = buscar_elemento(numeros, 9)  # Busca el número 9
print(f"El elemento se encuentra en la posición: {posicion}")  # Muestra resultado

# Este ejemplo muestra cómo buscar un elemento en una lista y devolver su posición.

# Salida:
# El elemento se encuentra en la posición: 3