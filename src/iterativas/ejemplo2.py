def es_primo(num): # Función que verifica si un número es primo
    if num < 2: # Un número menor que 2 no es primo
        return False # Si el número es menor que 2, la función devuelve False, indicando que no es un número primo.
    for i in range(2, int(num**0.5) + 1): # Itera desde 2 hasta la raíz cuadrada de num (inclusive) para verificar si num es divisible por algún número en ese rango
        if num % i == 0: # Si num es divisible por i, entonces no es primo
            return False # Si se encuentra un divisor, la función devuelve False, indicando que num no es un número primo.
    return True # Si num no es divisible por ningún número en el rango, la función devuelve True, indicando que num es un número primo.

primos = [] # Lista para almacenar los números primos encontrados
for num in range(2, 20): # Bucle for que itera desde 2 hasta 19 (inclusive) para verificar cada número en ese rango
    if es_primo(num): # Si el número es primo, se agrega a la lista de primos
        primos.append(num) # Si el número es primo, se agrega a la lista "primos" utilizando el método append().

print(f"Números primos entre 2 y 19: {primos}") # Imprime la lista de números primos encontrados entre 2 y 19 utilizando la sintaxis de formato de cadenas para mostrar el resultado.

# En este ejemplo, se define una función llamada es_primo() que verifica si un número es primo. Luego, se utiliza un bucle for para iterar sobre los números del 2 al 19 y se llama a la función es_primo() para cada número. Si un número es primo, se agrega a la lista primos. Finalmente, se imprime la lista de números primos encontrados entre 2 y 19.

# Salida:
# Números primos entre 2 y 19: [2, 3, 5, 7, 11, 13, 17, 19]