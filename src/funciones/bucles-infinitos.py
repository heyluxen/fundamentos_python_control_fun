while True: # Bucle infinito que se ejecuta indefinidamente hasta que se encuentra una condición de salida (break)
    respuesta = input("¿Quieres continuar? (s/n): ").lower() # Solicita al usuario que introduzca una respuesta y la convierte a minúsculas utilizando el método lower() para facilitar la comparación

    if respuesta == "n": # Si la respuesta es "n", se imprime un mensaje de finalización y se sale del bucle utilizando break
        print("Programa finalizado.") 
        break # Salimos del bucle si el usuario introduce "n"

    if respuesta == "s": # Si la respuesta es "s", se imprime un mensaje de continuación y el bucle continúa ejecutándose
        print("Continuando...") 
    else:
        print("Respuesta no válida. Introduce 's' o 'n'.") # Si la respuesta no es ni "s" ni "n", se imprime un mensaje de error indicando que la respuesta no es válida y se solicita al usuario que introduzca una respuesta correcta.

# En este ejemplo, el bucle while se ejecuta indefinidamente hasta que el usuario introduce "n" para finalizar el programa. Si el usuario introduce "s", el programa continúa ejecutándose y solicita una nueva respuesta. Si la respuesta no es válida, se muestra un mensaje de error y se vuelve a solicitar una respuesta correcta.

# Salida (ejemplo):
# ¿Quieres continuar? (s/n): s
# Continuando...
# ¿Quieres continuar? (s/n): x
# Respuesta no válida. Introduce 's' o 'n'.
# ¿Quieres continuar? (s/n): n
# Programa finalizado.
