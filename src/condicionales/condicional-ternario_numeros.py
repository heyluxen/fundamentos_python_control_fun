numeros = [1, 2, 3, 4, 5] # Se crea una lista llamada numeros que contiene los números del 1 al 5.
paridad = ["par" if n % 2 == 0 else "impar" for n in numeros] # Se utiliza una comprensión de listas para crear una nueva lista llamada paridad. Para cada número n en la lista numeros, se evalúa si n es par (n % 2 == 0). Si es par, se agrega la cadena "par" a la lista paridad; de lo contrario, se agrega la cadena "impar". El resultado es una lista que indica la paridad de cada número en la lista numeros.
print(paridad)  # Salida: ['impar', 'par', 'impar', 'par', 'impar']

# En este ejemplo, se utiliza un condicional ternario dentro de una comprensión de listas para determinar si cada número en la lista numeros es par o impar. El resultado es una nueva lista que contiene la cadena "par" para los números pares y "impar" para los números impares.

# Salida:
# ['impar', 'par', 'impar', 'par', 'impar']