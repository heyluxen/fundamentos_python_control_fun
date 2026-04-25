def validar_edades(lista_edades):  # Función para validar edades
    for edad in lista_edades:  # Recorre cada edad
        if not isinstance(edad, int) or edad < 0:  # Verifica si es inválida
            print(f"Edad inválida encontrada: {edad}")  # Muestra error
            break  # Detiene el bucle
    else:  # Se ejecuta si todas son válidas
        print("Todas las edades son válidas")  # Mensaje de éxito
        return True

    return False  # Retorna False si encontró error

# Pruebas con listas
validar_edades([25, 17, 30, 42])  # Todas válidas
validar_edades([25, -3, 30, 42])  # Contiene una inválida

# Este ejemplo valida una lista de edades y detiene el proceso si encuentra una inválida.

# Salida:
#Todas las edades son válidas
#Edad inválida encontrada: -3