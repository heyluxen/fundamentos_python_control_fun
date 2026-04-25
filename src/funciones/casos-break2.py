while True:  # Bucle infinito
    entrada = input("Escribe algo (o 'salir' para terminar): ")  # Pide texto al usuario

    if entrada.lower() == 'salir':  # Verifica si escribió "salir"
        print("Programa terminado.")  # Muestra mensaje de salida
        break  # Termina el bucle

    print(f"Has escrito: {entrada}")  # Muestra lo que escribió

# Este ejemplo repite la entrada hasta que el usuario escriba "salir".

# Salida: 
# Escribe algo (o 'salir' para terminar): hola
# Has escrito: hola
# Escribe algo (o 'salir' para terminar): salir
# Programa terminado.