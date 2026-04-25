def analizar_datos(valores, umbral):  # Función para analizar valores
    tiene_advertencias = False  # Bandera de advertencias

    for valor in valores:  # Recorre cada valor
        if valor > umbral:  # Verifica si supera el umbral
            tiene_advertencias = True  # Marca advertencia
            print(f"Advertencia: valor {valor} excede el umbral {umbral}")  # Muestra aviso
        else:
            pass  # No hace nada si está dentro del rango
    else:  # Se ejecuta al finalizar el bucle
        if not tiene_advertencias:  # Si no hubo advertencias
            print("Análisis completo: todos los valores están dentro del rango normal")  # Mensaje
            return "OK"

    return "ADVERTENCIA"  # Retorna si hubo valores fuera del rango

# Pruebas
analizar_datos([10, 15, 20, 25], 30)  # Todos normales
analizar_datos([10, 35, 20, 25], 30)  # Uno excede el umbral

# Este ejemplo analiza datos y detecta si alguno supera un valor límite.

# Salida:
#Análisis completo: todos los valores están dentro del rango normal
#Advertencia: valor 35 excede el umbral 30