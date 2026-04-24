numeros = [1, 2, 3, 4] # Aquí se define una lista de números del 1 al 4 y se asigna a la variable numeros.

match numeros: # Se utiliza la estructura de control match-case para comparar el valor de la variable numeros con diferentes casos.
    case []:
        print("La lista está vacía.") # Si la lista numeros está vacía, se muestra un mensaje indicando que la lista está vacía.
    case [uno]:
        print(f"Un solo elemento: {uno}.") # Si la lista numeros tiene un solo elemento, se muestra un mensaje indicando el valor de ese elemento.
    case [uno, dos]:
        print(f"Dos elementos: {uno} y {dos}.") # Si la lista numeros tiene dos elementos, se muestra un mensaje indicando los valores de esos elementos.
    case [uno, *resto]:
        print(f"Primer elemento: {uno}, resto de la lista: {resto}.") # Si la lista numeros tiene más de dos elementos, se muestra un mensaje indicando el valor del primer elemento y el resto de la lista. Resto es una variable que captura el resto de los elementos de la lista después del primer elemento.

# En este caso, la lista numeros tiene cuatro elementos, por lo que se cumple la última condición y se muestra el mensaje "Primer elemento: 1, resto de la lista: [2, 3, 4].".

# Salida:
# Primer elemento: 1, resto de la lista: [2, 3, 4].