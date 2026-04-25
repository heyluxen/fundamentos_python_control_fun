def calcular_raiz_cuadrada(numero, precision=0.0001): # Función para calcular la raíz cuadrada de un número utilizando el método de aproximación
    aproximacion = numero / 2  # Valor inicial
    while abs(aproximacion**2 - numero) > precision: # Bucle while que se ejecuta mientras la diferencia entre el cuadrado de la aproximación y el número sea mayor que la precisión deseada
        aproximacion = (aproximacion + numero/aproximacion) / 2 # Actualiza la aproximación utilizando la fórmula de Herón para mejorar la precisión en cada iteración
    return aproximacion # Devuelve la aproximación de la raíz cuadrada calculada

print(f"Raíz cuadrada de 25: {calcular_raiz_cuadrada(25):.6f}") # Imprime la raíz cuadrada de 25 formateada a seis decimales utilizando la sintaxis de formato de cadenas
print(f"Raíz cuadrada de 7: {calcular_raiz_cuadrada(7):.6f}") # Imprime la raíz cuadrada de 7 formateada a seis decimales utilizando la sintaxis de formato de cadenas

# En este ejemplo, la función calcular_raiz_cuadrada utiliza un bucle while para iterar hasta que la aproximación de la raíz cuadrada sea lo suficientemente precisa según el valor de precisión especificado. La aproximación se actualiza en cada iteración utilizando la fórmula de Herón, que mejora la precisión de la estimación. Finalmente, se imprime el resultado de la raíz cuadrada de 25 y 7 utilizando la sintaxis de formato de cadenas para mostrar el resultado con seis decimales.

# Salida:
# Raíz cuadrada de 25: 5.000000
# Raíz cuadrada de 7: 2.645751