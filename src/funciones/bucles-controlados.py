import random # Importa el módulo random para generar números aleatorios

objetivo = random.randint(1, 10) # Genera un número aleatorio entre 1 y 10 (inclusive) y lo asigna a la variable "objetivo". La función randint(a, b) devuelve un número entero N tal que a <= N <= b.
intentos = 0 # Variable para contar el número de intentos realizados
adivinado = False # Variable booleana para indicar si el número ha sido adivinado o no

while not adivinado and intentos < 3: # Bucle while que continúa ejecutándose mientras el número no haya sido adivinado y el número de intentos sea menor que 3
    intentos += 1 # Incrementa el contador de intentos en 1 cada vez que se realiza un intento
    numero = int(input(f"Intento {intentos}/3: Adivina un número del 1 al 10: ")) # Solicita al usuario que ingrese un número del 1 al 10, mostrando el número de intento actual y el total de intentos permitidos. La función input() se utiliza para obtener la entrada del usuario, y la función int() convierte esa entrada en un número entero.

    if numero == objetivo: # Verifica si el número ingresado por el usuario es igual al número objetivo generado aleatoriamente
        print(f"¡Correcto! Has adivinado en {intentos} intentos.") # Si el número es correcto, se imprime un mensaje de felicitación indicando el número de intentos que se necesitaron para adivinar el número.
        adivinado = True # Si el número es correcto, se establece la variable "adivinado" en True para salir del bucle while. Esto indica que el usuario ha adivinado el número correctamente y no se necesitan más intentos.
    else: 
        pista = "mayor" if numero < objetivo else "menor"
        print(f"Incorrecto. El número es {pista} que {numero}.") # Si el número ingresado es incorrecto, se determina si el número objetivo es mayor o menor que el número ingresado por el usuario. Luego, se imprime un mensaje indicando que el intento fue incorrecto y proporciona una pista sobre si el número objetivo es mayor o menor que el número ingresado.

if not adivinado:
    print(f"Se acabaron los intentos. El número era {objetivo}.") # Si el usuario no adivinó el número después de 3 intentos, se imprime un mensaje indicando que se han agotado los intentos y se revela cuál era el número objetivo.

# En este ejemplo, se utiliza un bucle while para permitir al usuario adivinar un número generado aleatoriamente entre 1 y 10. El usuario tiene un máximo de 3 intentos para adivinar el número. En cada intento, se verifica si el número ingresado es correcto, y si no lo es, se proporciona una pista sobre si el número objetivo es mayor o menor que el número ingresado. Si el usuario adivina correctamente, se muestra un mensaje de felicitación. Si se agotan los intentos sin adivinar el número, se revela cuál era el número objetivo.

# Salida (ejemplo):
# Intento 1/3: Adivina un número del 1 al 10: 5
# Incorrecto. El número es mayor que 5.
# Intento 2/3: Adivina un número del 1 al 10: 7
# Incorrecto. El número es menor que 7.
# Intento 3/3: Adivina un número del 1 al 10: 6
# ¡Correcto! Has adivinado en 3 intentos.