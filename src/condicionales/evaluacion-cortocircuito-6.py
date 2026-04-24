acceso_registrado = True

acceso_permitido = False

if acceso_permitido or (acceso_registrado and True):
    print("Acceso concedido.") # si el acceso es permitido o el acceso ha sido registrado, se muestra un mensaje indicando que el acceso ha sido concedido. En este caso, aunque el acceso no es permitido, el acceso ha sido registrado, por lo que la condición se evalúa como verdadera y se muestra el mensaje de acceso concedido.

# Salida:
# Acceso concedido.