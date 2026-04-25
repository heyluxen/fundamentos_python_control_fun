def obtener_numero_en_rango(mensaje, minimo, maximo): # Función que solicita al usuario un número entero dentro de un rango específico definido por "minimo" y "maximo". La función continúa solicitando la entrada hasta que el usuario ingresa un número válido dentro del rango.
    while True: # Bucle while que se ejecuta indefinidamente hasta que se encuentra una entrada válida (número entero dentro del rango)
        try: 
            valor = int(input(mensaje)) # Solicita al usuario que introduzca un número utilizando la función input() y lo convierte a un número entero utilizando int(). Si el usuario introduce algo que no se puede convertir a entero, se lanzará una excepción ValueError, que será manejada por el bloque except.
            if minimo <= valor <= maximo: 
                return valor # Si el número ingresado por el usuario está dentro del rango definido por "minimo" y "maximo", la función devuelve ese número, lo que también termina el bucle while.
            print(f"Error: El número debe estar entre {minimo} y {maximo}.") # Si el número ingresado no está dentro del rango, se imprime un mensaje de error indicando el rango válido y el bucle continúa solicitando una nueva entrada.
        except ValueError: 
            print("Error: Debes introducir un número entero.") # Si el usuario introduce algo que no se puede convertir a entero, se captura la excepción ValueError y se imprime un mensaje de error indicando que se debe introducir un número entero. El bucle continúa solicitando una nueva entrada.

edad = obtener_numero_en_rango("Introduce tu edad (0-120): ", 0, 120) # Llama a la función obtener_numero_en_rango() con un mensaje específico y un rango de 0 a 120 para solicitar al usuario que introduzca su edad. El valor ingresado se almacena en la variable "edad".
print(f"Edad registrada: {edad} años") # Imprime la edad registrada utilizando la sintaxis de formato de cadenas para mostrar el valor de "edad" seguido de "años".

# En este ejemplo, la función obtener_numero_en_rango() se utiliza para solicitar al usuario que introduzca su edad, asegurándose de que el valor ingresado sea un número entero dentro del rango de 0 a 120. La función maneja tanto la validación del rango como la validación de que la entrada sea un número entero, proporcionando mensajes de error claros en caso de entradas no válidas. Al finalizar, se muestra la edad registrada.

# Salida (ejemplo):
# Introduce tu edad (0-120): -5
# Error: El número debe estar entre 0 y 120.
# Introduce tu edad (0-120): abc
# Error: Debes introducir un número entero.
# Introduce tu edad (0-120): 25
# Edad registrada: 25 años