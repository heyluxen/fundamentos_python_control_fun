edad = 20 # Se define la variable edad y se le asigna el valor 20.

match edad: # Se utiliza la estructura de control match-case para comparar el valor de la variable edad con diferentes casos.
    case edad if edad < 18: # 
        print("Eres menor de edad.") # Si la edad es menor a 18, se muestra un mensaje indicando que eres menor de edad.
    case edad if edad >= 18 and edad < 65:
        print("Eres adulto.") # Si la edad es mayor o igual a 18 y menor a 65, se muestra un mensaje indicando que eres adulto. El and se utiliza para combinar dos condiciones, en este caso, que la edad sea mayor o igual a 18 y menor a 65.
    case edad if edad >= 65:
        print("Eres adulto mayor.") # Si la edad es mayor o igual a 65, se muestra un mensaje indicando que eres adulto mayor.}

# En este caso la edad es 20 y se cumple la segunda condición, por lo que se muestra el mensaje "Eres adulto.".

# Salida:
# Eres adulto.