usuario = 'admin' # Se asigna el valor 'admin' a la variable usuario, lo que indica que el usuario es un administrador.
contrasena = '1234' # Se asigna el valor '1234' a la variable contrasena, lo que representa la contraseña del usuario.

if usuario == 'admin': 
    if contrasena == '1234':
        print('Acceso concedido.') # Si el usuario es igual a 'admin' y la contraseña es igual a '1234', se muestra un mensaje indicando que el acceso ha sido concedido.
    else:
        print('Contraseña incorrecta.') # Si el usuario es igual a 'admin' pero la contraseña no es igual a '1234', se muestra un mensaje indicando que la contraseña es incorrecta.
else:
    print('Usuario no reconocido.') # Si el usuario no es igual a 'admin', se muestra un mensaje indicando que el usuario no es reconocido.

# Si el usuario es 'admin' y la contraseña es '1234', se muestra el mensaje de acceso concedido. Si el usuario es 'admin' pero la contraseña es incorrecta, se muestra un mensaje de contraseña incorrecta. Si el usuario no es 'admin', se muestra un mensaje de usuario no reconocido.

# Salida:
# Acceso concedido.