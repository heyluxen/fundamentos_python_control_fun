def calcular_precio_con_iva(precio_base, tasa_iva=0.21):  # Función que calcula el precio con IVA
    return precio_base * (1 + tasa_iva)  # Aplica el IVA al precio base y devuelve el resultado

precio_final = calcular_precio_con_iva(100)  # Calcula el precio final con el IVA por defecto
print(f"Precio con IVA: {precio_final} €")  # Muestra el precio final con IVA

# Este ejemplo calcula el precio final de un producto aplicando el IVA, usando un valor por defecto del 21% si no se especifica otro porcentaje.

# Salida: 
# Precio con IVA: 121.0 €