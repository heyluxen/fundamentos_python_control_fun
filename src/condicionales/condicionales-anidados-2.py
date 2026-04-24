edad = 16 # Se asigna el valor 16 a la variable edad, lo que indica que la persona tiene 16 años.
permiso_padres = True # Se asigna el valor True a la variable permiso_padres, lo que indica que la persona tiene el permiso de sus padres para obtener la licencia de conducir.

if edad >= 18:
    print('Puedes obtener la licencia de conducir.') # Si la edad es mayor o igual a 18, se muestra un mensaje indicando que la persona puede obtener la licencia de conducir.
else:
    if edad >= 16:
        if permiso_padres:
            print('Puedes obtener la licencia con permiso de tus padres.') # Si la edad es mayor o igual a 16 pero menor a 18, se verifica si la persona tiene el permiso de sus padres. Si tiene el permiso, se muestra un mensaje indicando que puede obtener la licencia con el permiso de sus padres.
        else:
            print('Necesitas el permiso de tus padres para obtener la licencia.') # Si la edad es mayor o igual a 16 pero menor a 18, se verifica si la persona tiene el permiso de sus padres. Si no tiene el permiso, se muestra un mensaje indicando que necesita el permiso de sus padres para obtener la licencia.
    else:
        print('Eres demasiado joven para conducir.') # Si la edad es menor a 16, se muestra un mensaje indicando que la persona es demasiado joven para conducir.

# En este ejemplo, se utilizan if anidados para verificar múltiples condiciones relacionadas con la edad y el permiso de los padres para determinar si una persona puede obtener una licencia de conducir. Primero se verifica si la persona es mayor o igual a 18 años, luego se verifica si tiene al menos 16 años y si tiene el permiso de sus padres, y finalmente se muestra el mensaje adecuado según las condiciones evaluadas.

# Salida:
# Puedes obtener la licencia con permiso de tus padres.