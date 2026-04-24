# Ejemplo con parentesis.

a = True
b = False 
c = not b 

resultado = (a or b) and c
print(resultado)  # Imprime True

# Salida:
# True

# El parentesis se utiliza para cambiar el orden de evaluación de los operadores. En este caso, se evalúa primero a or b, que es True or False, lo que da como resultado True. Luego, se evalúa True and c, que es True and True, lo que da como resultado True.