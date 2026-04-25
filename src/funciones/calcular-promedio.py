# Evitar efectos secundarios:
# Las funciones que devuelven valores no deberían modificar el estado global
# ni realizar acciones como imprimir dentro de ellas.

# Mejor práctica: separar el cálculo de la presentación del resultado

# Función que calcula el promedio de una lista de números
def calcular_promedio(numeros):
    return sum(numeros) / len(numeros)  # Retorna el promedio

# Lista de notas
notas = [7, 8, 6, 9]

# Se obtiene el resultado llamando la función
promedio = calcular_promedio(notas)

# Se muestra el resultado fuera de la función
print(f"El promedio es: {promedio}")  # Imprime el promedio calculado

# Este ejemplo muestra la buena práctica de evitar efectos secundarios en las funciones. La función solo realiza el cálculo del promedio y devuelve el resultado, mientras que la impresión se hace fuera de la función, manteniendo el código más limpio, organizado y reutilizable.

# Salida: 
# El promedio es: 7.5