dividendo = 10 # Se asigna el valor 10 a la variable dividendo.
divisor = 0 # Se asigna el valor 0 a la variable divisor, lo que representa un caso de división por cero.
resultado = dividendo / divisor if divisor != 0 else "División por cero no permitida" # Se utiliza un condicional ternario para realizar la división. Si el divisor es diferente de cero, se realiza la división y se asigna el resultado a la variable resultado. Si el divisor es igual a cero, se asigna el mensaje "División por cero no permitida" a la variable resultado para evitar un error de división por cero.
print(resultado) # Se imprime el valor de la variable resultado, que en este caso será "División por cero no permitida" debido a que el divisor es cero.

# Salida:
# División por cero no permitida