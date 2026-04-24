edad = 30 # Se asigna el valor 30 a la variable edad, lo que indica que la persona tiene 30 años.
estado_civil = 'soltero' # Se asigna el valor 'soltero' a la variable estado_civil, lo que indica que la persona no está casada.

if edad >= 18: # Se verifica si la edad es mayor o igual a 18, lo que indica que la persona es un adulto.
    if estado_civil == 'casado':
        print('Eres un adulto casado.') # Si la persona es un adulto y su estado civil es 'casado', se muestra un mensaje indicando que es un adulto casado.
    else:
        print('Eres un adulto soltero.') # Si la persona es un adulto pero su estado civil no es 'casado', se muestra un mensaje indicando que es un adulto soltero.
else:
    print('Eres menor de edad.') # Si la edad es menor a 18, se muestra un mensaje indicando que la persona es menor de edad.

# Aqui if anidados se utilizan para verificar múltiples condiciones relacionadas entre sí. En este caso, primero se verifica si la persona es un adulto (edad >= 18) y luego se verifica su estado civil para determinar el mensaje adecuado.

# Salida:
# Eres un adulto soltero.