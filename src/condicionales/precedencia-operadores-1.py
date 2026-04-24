# Ejemplo sin parentesis.
a = True # Se asigna el valor True a la variable a, lo que indica que a es verdadero.
b = False # Se asigna el valor False a la variable b, lo que indica que b es falso.
c = not b # Se asigna el valor de not b a la variable c. Dado que b es False, not b es True, por lo que c también es True.

resultado = a or b and c
print(resultado)  # Imprime True # El resultado es True porque el operador and tiene mayor precedencia que el operador or. Por lo tanto, se evalúa primero b and c, que es False and True, lo que da como resultado False. Luego, se evalúa a or False, que es True or False, lo que da como resultado True.

# El orden de precedencia de los operadores lógicos es el siguiente:
# 1. not
# 2. and
# 3. or

# Salida:
# True
