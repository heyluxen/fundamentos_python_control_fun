edad = 17 # Se asigna el valor 17 a la variable edad.
permiso_parental = True # Se asigna el valor True a la variable permiso_parental, lo que indica que se tiene permiso parental.

if (edad >= 18) or (edad >= 16 and permiso_parental):
    print("Puedes obtener la licencia de conducir.") # Si la edad es mayor o igual a 18, o si la edad es mayor o igual a 16 y se tiene permiso parental, se muestra un mensaje indicando que puedes obtener la licencia de conducir. El operador or se utiliza para combinar ambas condiciones, lo que significa que si cualquiera de las condiciones es verdadera, el bloque de código se ejecutará.
else:
    print("No cumples los requisitos para la licencia.") # Si ninguna de las condiciones se cumple, se muestra un mensaje indicando que no cumples los requisitos para la licencia.

# En este caso, la edad es 17 y se tiene permiso parental, por lo que se cumple la segunda condición (edad >= 16 and permiso_parental), lo que permite obtener la licencia de conducir.

# Salida:
# Puedes obtener la licencia de conducir.