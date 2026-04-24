fruta = input("Introduzca una fruta: ") # Aqui se solicita que introduzca una fruta y se asigna a la variable fruta.

match fruta:
    case "manzana":
        print("La fruta es una manzana.") # Si la fruta es igual a "manzana", se muestra un mensaje indicando que la fruta es una manzana.
    case "naranja":
        print("La fruta es una naranja.") # Si la fruta es igual a "naranja", se muestra un mensaje indicando que la fruta es una naranja.
    case "plátano":
        print("La fruta es un plátano.") # Si la fruta es igual a "plátano", se muestra un mensaje indicando que la fruta es un plátano.
    case _:
        print("Fruta desconocida.") # Si la fruta no coincide con ninguno de los casos anteriores, se muestra un mensaje indicando que la fruta es desconocida.
    
# El match-case es una estructura de control que permite comparar el valor de una variable con diferentes casos y ejecutar un bloque de código correspondiente al caso que coincida. En este ejemplo, se compara la variable fruta con los casos "manzana", "naranja" y "plátano", y se muestra un mensaje correspondiente a cada caso. Si la fruta no coincide con ninguno de los casos, se ejecuta el caso por defecto representado por el guion bajo (_).

# Salida:
# Introduzca una fruta: manzana
# La fruta es una manzana.

# Introduzca una fruta: pera
# Fruta desconocida.