def dividir_seguro(a, b):  # Función que divide dos números de forma segura
    # Verificación de seguridad para evitar errores
    if b == 0:  # Si el divisor es cero
        print("Error: División por cero")  # Muestra un mensaje de error
        return None  # Termina la función sin hacer la división

    # Si b no es cero, se realiza la división
    resultado = a / b  # Calcula la división
    return resultado  # Devuelve el resultado

print(dividir_seguro(10, 2))  # Muestra 5.0
print(dividir_seguro(10, 0))  # Muestra error y luego None

# Este ejemplo muestra cómo evitar errores al dividir números, controlando el caso en el que el divisor es cero para no romper el programa.

#Salida
#5.0
#Error: División por cero
#None
