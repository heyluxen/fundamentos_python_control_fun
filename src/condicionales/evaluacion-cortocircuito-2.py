dividendo = 10 # Se asigna el valor 10 a la variable dividendo.
divisor = 0 # Se asigna el valor 0 a la variable divisor, lo que representa un caso de división por cero.

if divisor != 0 and dividendo / divisor > 1:
    print("El resultado de la división es mayor que 1.") # Si el divisor es diferente de cero y el resultado de la división es mayor que 1, se muestra un mensaje indicando que el resultado de la división es mayor que 1.
else:
    print("No es posible dividir entre cero.") # Si el divisor es igual a cero, se muestra un mensaje indicando que no es posible dividir entre cero.

# En este ejemplo, se utiliza un condicional con evaluación de cortocircuito para evitar un error de división por cero. Primero se verifica si el divisor es diferente de cero antes de realizar la división. Si el divisor es igual a cero, la condición se evalúa como falsa y se muestra el mensaje correspondiente sin intentar realizar la división.

# Salida:
# No es posible dividir entre cero.