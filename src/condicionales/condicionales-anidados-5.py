a = 5 # Se asigna el valor 5 a la variable a.
b = 10 # Se asigna el valor 10 a la variable b.
c = 15 # Se asigna el valor 15 a la variable c.

if a > b: 
    if a > c:
        print('a es el mayor.') # Si a es mayor que b y también es mayor que c, se muestra un mensaje indicando que a es el mayor.
    else:
        if c > b:
            print('c es el mayor.') # Si a no es mayor que c, pero c es mayor que b, se muestra un mensaje indicando que c es el mayor.
        else:
            print('b es el mayor.') # Si a no es mayor que c y c no es mayor que b, se muestra un mensaje indicando que b es el mayor.
else:
    if b > c:
        print('b es el mayor.')
    else:
        print('c es el mayor.') # Si a no es mayor que b, se verifica si b es mayor que c. Si b es mayor que c, se muestra un mensaje indicando que b es el mayor. De lo contrario, se muestra un mensaje indicando que c es el mayor.

# En este ejemplo, se utilizan if anidados para comparar tres variables (a, b y c) y determinar cuál de ellas es la mayor. Primero se compara a con b, luego se compara a con c, y finalmente se compara b con c para determinar el resultado final.

# Salida:
# c es el mayor.

mayor = a

if b > mayor:
    mayor = b

if c > mayor:
    mayor = c

print(f'El número mayor es {mayor}.')

# Esta es una forma más sencilla de encontrar el número mayor entre a, b y c utilizando if anidados. Se asigna inicialmente el valor de a a la variable mayor, luego se compara con b y se actualiza si b es mayor, y finalmente se compara con c y se actualiza si c es mayor. Al final, se imprime el número mayor encontrado.

# Salida:
# El número mayor es 15.