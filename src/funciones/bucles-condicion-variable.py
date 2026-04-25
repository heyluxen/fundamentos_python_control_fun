saldo = 1000 # Saldo inicial
while saldo > 0: # Bucle while que se ejecuta mientras el saldo sea mayor que 0
    print(f"Saldo actual: {saldo}€") # Imprime el saldo actual utilizando la sintaxis de formato de cadenas
    gasto = float(input("Introduce la cantidad a gastar (0 para salir): ")) # Solicita al usuario que introduzca la cantidad a gastar y la convierte a un número de punto flotante utilizando float()

    if gasto == 0:
        break  # Salimos del bucle inmediatamente si el usuario introduce 0

    if gasto > saldo:
        print("No tienes suficiente saldo.") # Imprime un mensaje de advertencia si el gasto es mayor que el saldo actual
        continue  # Volvemos al inicio del bucle

    saldo -= gasto # Resta el gasto al saldo actual utilizando el operador de asignación -=

print(f"Saldo final: {saldo}€") # Imprime el saldo final después de salir del bucle utilizando la sintaxis de formato de cadenas

# En este ejemplo, se utiliza un bucle while para simular un proceso de gasto de dinero. El bucle se ejecuta mientras el saldo sea mayor que 0. En cada iteración, se muestra el saldo actual y se solicita al usuario que introduzca una cantidad a gastar. Si el usuario introduce 0, el bucle se detiene inmediatamente. Si el gasto es mayor que el saldo, se muestra un mensaje de advertencia y se vuelve al inicio del bucle para solicitar una nueva cantidad. Si el gasto es válido, se resta del saldo actual. Al finalizar el bucle, se muestra el saldo final.

# Salida (ejemplo):
# Saldo actual: 1000€
# Introduce la cantidad a gastar (0 para salir): 200
# Saldo actual: 800€
# Introduce la cantidad a gastar (0 para salir): 300
# Saldo actual: 500€
# Introduce la cantidad a gastar (0 para salir): 600
# No tienes suficiente saldo.
# Saldo actual: 500€
# Introduce la cantidad a gastar (0 para salir): 100
# Saldo actual: 400€
# Introduce la cantidad a gastar (0 para salir): 0
# Saldo final: 400€
