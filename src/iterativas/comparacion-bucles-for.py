# Usando while

# Suma de los números del 1 al 10 usando while
suma = 0 
i = 1
while i <= 10:
    suma += i
    i += 1
print(f"Suma (while): {suma}")

# Equivalente con for

# Suma de los números del 1 al 10 usando for con range
suma = 0
for i in range(1, 11):
    suma += i # del 1 al 10
print(f"Suma (for): {suma}")

# Este ejemplo calcula la suma de los números del 1 al 10 usando dos estructuras: while y for, mostrando que ambas logran el mismo resultado.

# Salida:
# Suma (while): 55
# Suma (for): 55