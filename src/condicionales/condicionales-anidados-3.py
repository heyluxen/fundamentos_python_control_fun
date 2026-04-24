edad = 16 # Se asigna el valor 16 a la variable edad, lo que indica que la persona tiene 16 años.
permiso_padres = True # Se asigna el valor True a la variable permiso_padres, lo que indica que la persona tiene el permiso de sus padres para obtener la licencia de conducir.

if edad >= 18: 
    print('Puedes obtener la licencia de conducir.') # Si la edad es mayor o igual a 18, se muestra un mensaje indicando que la persona puede obtener la licencia de conducir.
elif edad >= 16 and permiso_padres:
    print('Puedes obtener la licencia con permiso de tus padres.') # Si la edad es mayor o igual a 16 pero menor a 18, se verifica si la persona tiene el permiso de sus padres. Si tiene el permiso, se muestra un mensaje indicando que puede obtener la licencia con el permiso de sus padres.
elif edad >= 16 and not permiso_padres:
    print('Necesitas el permiso de tus padres para obtener la licencia.') # Si la edad es mayor o igual a 16 pero menor a 18, se verifica si la persona tiene el permiso de sus padres. Si no tiene el permiso, se muestra un mensaje indicando que necesita el permiso de sus padres para obtener la licencia.
else:
    print('Eres demasiado joven para conducir.') # Si la edad es menor a 16, se muestra un mensaje indicando que la persona es demasiado joven para conducir.

# aqui se usa and o or para combinar condiciones en lugar de if anidados, lo que hace que el código sea más legible y fácil de entender. En este caso, se verifica si la edad es mayor o igual a 18 para determinar si la persona puede obtener la licencia de conducir, luego se verifica si la edad es mayor o igual a 16 y si tiene el permiso de los padres para determinar si puede obtener la licencia con permiso de los padres, y finalmente se verifica si la edad es mayor o igual a 16 pero no tiene el permiso de los padres para determinar si necesita el permiso de los padres para obtener la licencia. Si ninguna de estas condiciones se cumple, se muestra un mensaje indicando que la persona es demasiado joven para conducir.

# Salida:
# Puedes obtener la licencia con permiso de tus padres.