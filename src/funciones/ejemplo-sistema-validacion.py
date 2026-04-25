def validar_formulario(datos):  # Función para validar un formulario
    campos_requeridos = ["nombre", "email", "edad"]  # Campos obligatorios
    errores = []  # Lista de errores

    # Verificar campos requeridos
    for campo in campos_requeridos:  # Recorre cada campo obligatorio
        if campo not in datos:  # Verifica si falta el campo
            errores.append(f"Falta el campo requerido: {campo}")  # Agrega error
            break
        elif not datos[campo]:  # Verifica si está vacío
            errores.append(f"El campo {campo} no puede estar vacío")  # Agrega error
            break
    else:
        # Validaciones si todo lo anterior está correcto

        if "@" not in datos["email"]:  # Verifica formato de email
            errores.append("Email inválido")

        try:
            edad = int(datos["edad"])  # Convierte edad a número
            if edad < 18 or edad > 120:  # Verifica rango válido
                errores.append("La edad debe estar entre 18 y 120")
        except ValueError:  # Si no es número
            errores.append("La edad debe ser un número")

    # Validaciones opcionales
    if "telefono" in datos:  # Verifica si existe teléfono
        if not datos["telefono"].isdigit():  # Valida que sean solo dígitos
            errores.append("El teléfono debe contener solo dígitos")
    else:
        pass  # Campo opcional

    # Resultado final
    if errores:  # Si hay errores
        return {"valido": False, "errores": errores}  # Retorna errores
    else:
        return {"valido": True}  # Retorna válido

# Pruebas
formulario1 = {
    "nombre": "Ana García",
    "email": "ana@ejemplo.com",
    "edad": "28"
}

formulario2 = {
    "nombre": "Carlos López",
    "email": "carlosejemplo.com",
    "edad": "17"
}

print(validar_formulario(formulario1))  # Formulario válido
print(validar_formulario(formulario2))  # Formulario con errores

# Este ejemplo valida un formulario verificando campos obligatorios, formato y valores.

# Salida: 
#{'valido': True}
#{'valido': False, 'errores': ['Email inválido', 'La edad debe estar entre 18 y 120']}