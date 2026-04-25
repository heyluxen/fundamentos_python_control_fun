def saludar(nombre):  # Función que recibe un nombre y saluda
    print(f"Hola, {nombre}")  # Muestra el saludo en pantalla
    # No hay return, por lo tanto la función no devuelve un valor

resultado = saludar("Laura")  # Llama la función con el nombre Laura
print(f"La función devolvió: {resultado}")  # Muestra lo que devolvió la función (None)

# Salida: 
# Hola, Laura
# La función devolvió: None