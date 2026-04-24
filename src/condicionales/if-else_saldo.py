saldo = 300
retiro = 500
if saldo >= retiro: 
    saldo -= retiro
    print("Retiro exitoso.")
    print(f"Nuevo saldo: {saldo}")
# Aquí se verifica si el saldo es mayor o igual a lo que se va a retirar, tambien si el saldo es menor o igual a lo que se va a retirar, si la condición es verdadera, se muestra un mensaje de retiro exitoso y el nuevo saldo.
else:
    print("Fondos insuficientes.")
    print(f"Saldo actual: {saldo}")
# Si la condición es falsa, se muestra un mensaje de fondos insuficientes y el saldo actual.

#Salida:
#Fondos insuficientes.
#Saldo actual: 300