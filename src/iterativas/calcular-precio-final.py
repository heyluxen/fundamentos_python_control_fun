def calcular_precio_final(precio_base, impuesto):  # Función para calcular precio con impuesto
    return precio_base + (precio_base * impuesto)  # Calcula el total

total = calcular_precio_final(100, 0.21)  # Llama a la función con valores
print(f"Precio final: {total}")  # Muestra el resultado

# Este ejemplo calcula el precio final aplicando un impuesto.

# Salida: 
# Precio final: 121.0