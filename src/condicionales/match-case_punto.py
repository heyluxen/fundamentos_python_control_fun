punto = (0, 0) # Aquí se asigna una tupla con las coordenadas (0, 0) a la variable punto.

match punto:
    case (0, 0):
        print("El punto está en el origen.") # Si el punto es igual a (0, 0), se muestra un mensaje indicando que el punto está en el origen.
    case (0, y):
        print(f"El punto está en el eje Y en y={y}.") # Si el punto tiene una coordenada x igual a 0 y una coordenada y, se muestra un mensaje indicando que el punto está en el eje Y y se muestra el valor de y.
    case (x, 0):
        print(f"El punto está en el eje X en x={x}.") # Si el punto tiene una coordenada y igual a 0 y una coordenada x, se muestra un mensaje indicando que el punto está en el eje X y se muestra el valor de x.
    case (x, y):
        print(f"El punto está en coordenadas x={x}, y={y}.") # Si el punto tiene coordenadas x e y diferentes de 0, se muestra un mensaje indicando las coordenadas del punto.

# Como el punto es (0, 0), se cumple la primera condición y se muestra el mensaje "El punto está en el origen.".

# Salida:
# El punto está en el origen.