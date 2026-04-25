temperaturas = [22, 19, 24, 25, 21, 23, 20] # Lista de temperaturas registradas durante una semana (de lunes a domingo)
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"] # Lista de días correspondientes a las temperaturas registradas

# Encontrar el día más caluroso
max_temp = max(temperaturas) # Utiliza la función max() para encontrar la temperatura máxima en la lista "temperaturas" y la asigna a la variable "max_temp".
indice_max = temperaturas.index(max_temp) # Utiliza el método index() para encontrar el índice del elemento con la temperatura máxima en la lista "temperaturas" y lo asigna a la variable "indice_max".
print(f"El día más caluroso fue {dias[indice_max]} con {max_temp}°C") # Imprime el día más caluroso junto con su temperatura utilizando la sintaxis de formato de cadenas.

# Calcular la temperatura promedio
promedio = sum(temperaturas) / len(temperaturas) # Utiliza las funciones sum() y len() para calcular la temperatura promedio y la asigna a la variable "promedio".
print(f"Temperatura promedio: {promedio:.1f}°C") # Imprime la temperatura promedio formateada a un decimal utilizando la sintaxis de formato de cadenas.

# Días con temperatura superior al promedio
for i in range(len(dias)): # Bucle for que itera sobre los índices de la lista "dias" utilizando la función range() junto con len() para generar una secuencia de índices.
    if temperaturas[i] > promedio: # Condición que verifica si la temperatura en el índice actual es mayor que el promedio.
        print(f"{dias[i]}: {temperaturas[i]}°C (por encima del promedio)") # Si la condición se cumple, se imprime el día correspondiente junto con su temperatura y una indicación de que está por encima del promedio utilizando la sintaxis de formato de cadenas.

# En este ejemplo, se tiene una lista de temperaturas registradas durante una semana y una lista de días correspondientes. Se utiliza la función max() para encontrar la temperatura máxima y el método index() para obtener el índice del día más caluroso. Luego, se calcula la temperatura promedio utilizando las funciones sum() y len(). Finalmente, se itera sobre los índices de los días para verificar cuáles tienen una temperatura superior al promedio y se imprime esa información.

# Salida:
# El día más caluroso fue Jueves con 25°C
# Temperatura promedio: 22.0°C
# Miércoles: 24°C (por encima del promedio)
# Jueves: 25°C (por encima del promedio)
# Sábado: 23°C (por encima del promedio)