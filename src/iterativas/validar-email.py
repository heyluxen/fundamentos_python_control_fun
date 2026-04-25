def validar_email(email):
    """
    Verifica si una dirección de correo electrónico tiene formato válido.

    Args:
        email (str): La dirección de correo a validar

    Returns:
        bool: True si el formato es válido, False en caso contrario

    Raises:
        TypeError: Si email no es una cadena de texto
    """

    # Validación de tipo de dato
    if not isinstance(email, str):
        raise TypeError("El email debe ser una cadena de texto")

    # Verifica que tenga @ y un punto después del @
    return "@" in email and "." in email.split("@")[-1]

# Este ejemplo valida si un correo electrónico tiene un formato básico correcto y evita errores si el dato no es texto.