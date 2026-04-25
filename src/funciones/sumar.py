def sumar(*numeros):  # Función que recibe múltiples números
    total = 0  # Inicializa la suma
    for numero in numeros:  # Recorre los valores
        total += numero  # Suma cada número
    return total  # Devuelve el total

# Uso con diferentes cantidades de argumentos
print(sumar(1, 2))  # Muestra 3
print(sumar(1, 2, 3, 4, 5))  # Muestra 15
print(sumar())  # Muestra 0

# Este ejemplo muestra cómo usar *args para sumar varios números.

# Salida:
#3
#15
#0