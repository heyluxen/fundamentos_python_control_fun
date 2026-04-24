condiciones = [True, True, False, True] # Se crea una lista llamada condiciones que contiene los valores booleanos True, True, False y True.

if all(condiciones): # Se utiliza la función all() para verificar si todas las condiciones en la lista condiciones son verdaderas. La función all() devuelve True si todas las condiciones son verdaderas, y False si al menos una condición es falsa. En este caso, como hay una condición que es falsa (False), la función all() devolverá False.
    print("Todas las condiciones son verdaderas.")
else:
    print("Al menos una condición es falsa.") # Si la condición se evalúa como falsa, se muestra un mensaje indicando que al menos una condición es falsa. En este caso, como hay una condición que es falsa, se mostrará el mensaje correspondiente.

# Salida:
# Al menos una condición es falsa.