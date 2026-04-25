def imprimir_triangulo(altura):  # Define una función llamada imprimir_triangulo que toma un parámetro altura. Esta función se encargará de imprimir un triángulo de asteriscos con la altura especificada.
    fila = 1 # Inicializa la variable fila con el valor 1. Esta variable se utilizará para controlar el número de asteriscos que se imprimirán en cada fila del triángulo.
    while fila <= altura: # Inicia un bucle while que se ejecutará mientras la condición fila <= altura sea verdadera. Esto significa que el bucle se repetirá mientras el valor de fila sea menor o igual a la altura especificada.
        print("*" * fila) # Imprime una cadena de asteriscos cuyo número es igual al valor actual de fila. Esto se logra utilizando el operador de multiplicación (*) para repetir el carácter "*" el número de veces indicado por fila.
        fila += 1 # Incrementa el valor de fila en 1 utilizando el operador de asignación +=. Esto es necesario para avanzar hacia la condición de salida del bucle, ya que eventualmente hará que la condición fila <= altura sea falsa y el bucle se detenga.

imprimir_triangulo(5) # Llama a la función imprimir_triangulo con el argumento 5, lo que hará que se imprima un triángulo de asteriscos con una altura de 5 filas.

# En este ejemplo, la función imprimir_triangulo utiliza un bucle while para imprimir un triángulo de asteriscos. El bucle se ejecuta mientras fila sea menor o igual a altura, y en cada iteración se imprime una fila de asteriscos cuyo número es igual al valor actual de fila. Luego, se incrementa fila en 1 para avanzar hacia la condición de salida del bucle. Al llamar a la función con el argumento 5, se imprimirá un triángulo con 5 filas de asteriscos.

# Salida:
# *
# **
# ***
# ****
# *****

