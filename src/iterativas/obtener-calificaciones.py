# Uso de return temprano:
# Mejora la legibilidad porque se manejan primero los casos especiales

def obtener_calificacion(puntuacion):
    # Caso especial: validar rango de la puntuación
    if puntuacion < 0 or puntuacion > 100:
        return "Puntuación inválida"  # Termina la función inmediatamente

    # Evaluación de calificaciones de mayor a menor
    if puntuacion >= 90:
        return "Sobresaliente"
    if puntuacion >= 70:
        return "Notable"
    if puntuacion >= 60:
        return "Bien"
    if puntuacion >= 50:
        return "Suficiente"

    # Caso final si no cumple ninguna condición anterior
    return "Insuficiente"

# Este ejemplo muestra el uso de return temprano, que permite salir de la función rápidamente cuando ocurre un caso especial (como una puntuación inválida). Esto evita estructuras más largas y hace el código más claro, ordenado y fácil de leer.