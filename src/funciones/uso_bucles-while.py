def encontrar_raiz(numero, max_iteraciones=10):  # Calcula la raíz cuadrada aproximada
    aproximacion = numero / 2  # Valor inicial
    iteracion = 0  # Contador de iteraciones

    while abs(aproximacion**2 - numero) > 0.001 and iteracion < max_iteraciones:  # Condición
        aproximacion = (aproximacion + numero/aproximacion) / 2  # Mejora la aproximación
        iteracion += 1  # Aumenta el contador
        print(f"Iteración {iteracion}: {aproximacion:.6f}")  # Muestra progreso
    else:
        if iteracion < max_iteraciones:  # Si converge antes del límite
            print(f"Convergencia alcanzada en {iteracion} iteraciones")  # Mensaje
            return aproximacion  # Devuelve resultado

    print("No se alcanzó convergencia en el número máximo de iteraciones")  # Mensaje
    return aproximacion  # Devuelve la mejor aproximación

encontrar_raiz(25)  # Prueba con 25
encontrar_raiz(612, 5)  # Prueba con límite de iteraciones

# Este ejemplo aproxima la raíz cuadrada usando iteraciones (método de Newton).

# Salida:
#Iteración 1: 7.250000
#Iteración 2: 5.349138
#Iteración 3: 5.011394
#Iteración 4: 5.000013
#Convergencia alcanzada en 4 iteraciones
#Iteración 1: 154.000000
#Iteración 2: 78.987013
#Iteración 3: 43.367561
#Iteración 4: 28.739746
#Iteración 5: 25.017149
#No se alcanzó convergencia en el número máximo de iteraciones