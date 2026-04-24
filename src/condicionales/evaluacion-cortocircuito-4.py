acceso_registrado = True

acceso_permitido = False

if acceso_permitido:
    print("Acceso concedido.")
else:
    if acceso_registrado:
        print("Acceso concedido.")

# En este ejemplo, se utiliza un condicional anidado para verificar dos condiciones relacionadas con el acceso. Primero se verifica si el acceso es permitido. Si es así, se muestra un mensaje de acceso concedido. Si el acceso no es permitido, se verifica si el acceso ha sido registrado. Si el acceso ha sido registrado, también se muestra un mensaje de acceso concedido. En este caso, aunque el acceso no es permitido, el hecho de que haya sido registrado permite conceder el acceso.    

# Salida:
# Acceso concedido.