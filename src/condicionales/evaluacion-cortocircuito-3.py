acceso_registrado = True # Se asigna el valor True a la variable acceso_registrado, lo que indica que el acceso ha sido registrado.

acceso_permitido = False # Se asigna el valor False a la variable acceso_permitido, lo que indica que el acceso no ha sido permitido.

if acceso_permitido or acceso_registrado:
    print("Acceso concedido.") # Si el acceso es permitido o el acceso ha sido registrado, se muestra un mensaje indicando que el acceso ha sido concedido. En este caso, aunque el acceso no es permitido, el acceso ha sido registrado, por lo que la condición se evalúa como verdadera y se muestra el mensaje de acceso concedido.

# Salida:
# Acceso concedido.