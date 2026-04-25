def calcular_factorial(n): # Función para calcular el factorial de un número utilizando un bucle while
    resultado = 1 # Variable para almacenar el resultado del factorial, inicializada en 1
    while n > 0: # Bucle while que se ejecuta mientras n sea mayor que 0
        resultado *= n # Multiplica el valor actual de resultado por n utilizando el operador de asignación *=
        n -= 1 # Decrementa el valor de n en 1 utilizando el operador de asignación -= para avanzar hacia la condición de salida del bucle
    return resultado # Devuelve el resultado del factorial calculado

numero = 5 # Número del cual se desea calcular el factorial
print(f"El factorial de {numero} es {calcular_factorial(numero)}") # Imprime el resultado del factorial utilizando la sintaxis de formato de cadenas para mostrar el número y su factorial calculado

# En este ejemplo, la función calcular_factorial utiliza un bucle while para calcular el factorial de un número n. El bucle se ejecuta mientras n sea mayor que 0, multiplicando el resultado acumulado por n y luego decrementando n en cada iteración. Al finalizar el bucle, se devuelve el resultado del factorial. Finalmente, se llama a la función con un número específico (en este caso, 5) y se imprime el resultado utilizando la sintaxis de formato de cadenas.

# Salida:
# El factorial de 5 es 120