edad = 20 # Se asigna el valor 20 a la variable edad.
categoria = "Menor" if edad < 18 else ("Joven Adulto" if edad < 30 else "Adulto") # Se utiliza un condicional ternario anidado para asignar una categoría a la variable categoria. Si la edad es menor a 18, se asigna "Menor". Si la edad es mayor o igual a 18 pero menor a 30, se asigna "Joven Adulto". Si la edad es mayor o igual a 30, se asigna "Adulto".
print(categoria) # Se imprime el valor de la variable categoria, que en este caso será "Joven Adulto" porque la edad es 20, que está entre 18 y 30.

# Salida:
# Joven Adulto