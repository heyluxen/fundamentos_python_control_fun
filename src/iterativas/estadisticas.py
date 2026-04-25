def estadisticas(numeros):  # Función que calcula estadísticas de una lista de números
    total = sum(numeros)  # Suma todos los números de la lista
    promedio = total / len(numeros)  # Calcula el promedio
    minimo = min(numeros)  # Encuentra el número más pequeño
    maximo = max(numeros)  # Encuentra el número más grande
    return total, promedio, minimo, maximo  # Devuelve todos los resultados

datos = [4, 8, 15, 16, 23, 42]  # Lista de números de ejemplo

suma, media, menor, mayor = estadisticas(datos)  # Llama la función y guarda cada resultado

print(f"Suma: {suma}")        # Muestra la suma total
print(f"Promedio: {media}")   # Muestra el promedio
print(f"Mínimo: {menor}")     # Muestra el número más pequeño
print(f"Máximo: {mayor}")     # Muestra el número más grande

# Este ejemplo calcula estadísticas básicas (suma, promedio, mínimo y máximo) de una lista de números usando una función que devuelve varios valores.

# Salida:
#Suma: 108
#Promedio: 18.0
#Mínimo: 4
#Máximo: 42

resultado = estadisticas(datos)  # Guarda todos los resultados en una sola variable (tupla)
print(type(resultado))  # Muestra el tipo de dato (tuple)
print(resultado)        # Muestra toda la tupla con los resultados

print(resultado[1])     # Muestra el segundo valor de la tupla (el promedio)

# Salida: 
# <class 'tuple'>
# (108, 18.0, 4, 42)
# 18.0
