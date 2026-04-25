def validar_contraseña(contraseña):  # Función para validar una contraseña
    if len(contraseña) < 8:  # Verifica longitud mínima
        return False

    tiene_mayuscula = False  # Bandera para mayúsculas
    tiene_minuscula = False  # Bandera para minúsculas
    tiene_numero = False  # Bandera para números

    for caracter in contraseña:  # Recorre cada carácter
        if caracter.isupper():  # Verifica mayúscula
            tiene_mayuscula = True
            continue  # Pasa al siguiente carácter

        if caracter.islower():  # Verifica minúscula
            tiene_minuscula = True
            continue

        if caracter.isdigit():  # Verifica número
            tiene_numero = True

    return tiene_mayuscula and tiene_minuscula and tiene_numero  # Retorna si cumple todo

# Lista de contraseñas a probar
contraseñas = ["abc123", "Password", "Password1", "pass123", "PASS123"]

for pwd in contraseñas:  # Recorre cada contraseña
    if validar_contraseña(pwd):  # Verifica si es válida
        print(f"'{pwd}' es válida")  # Muestra válida
    else:
        print(f"'{pwd}' NO es válida")  # Muestra no válida

# Este ejemplo valida contraseñas según longitud, mayúsculas, minúsculas y números.

# Salida:
#'abc123' NO es válida
#'Password' NO es válida
#'Password1' es válida
#'pass123' NO es válida
#'PASS123' NO es válida