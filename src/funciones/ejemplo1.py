n = 10 # Número hasta el cual se desea calcular la suma de los primeros n números
suma = 0 # Variable para almacenar la suma acumulada
for i in range(1, n+1): # Bucle for que itera desde 1 hasta n (inclusive) utilizando range(1, n+1)
    suma += i # En cada iteración, se agrega el valor de i a la variable suma utilizando el operador de asignación +=
print(f"La suma de los primeros {n} números es: {suma}") # Imprime el resultado de la suma utilizando la sintaxis de formato de cadenas para mostrar el valor de n y la suma calculada

# En este ejemplo, el bucle for utiliza la función range() para generar una secuencia de números desde 1 hasta n (inclusive). En cada iteración del bucle, el valor de i se agrega a la variable suma utilizando el operador de asignación +=. Al finalizar el bucle, se imprime el resultado de la suma utilizando la sintaxis de formato de cadenas.

# Salida:
# La suma de los primeros 10 números es: 55