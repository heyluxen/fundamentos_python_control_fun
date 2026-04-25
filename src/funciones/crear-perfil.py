# Correcto
def crear_perfil(nombre, edad, ciudad="Madrid"):  # Parámetro por defecto al final
    return f"Perfil: {nombre}, {edad} años, {ciudad}"  # Devuelve el perfil

# Incorrecto: parámetro con valor por defecto antes de uno obligatorio (da error)
# def crear_perfil(nombre, ciudad="Madrid", edad):
#     return f"Perfil: {nombre}, {edad} años, {ciudad}"

# Este ejemplo muestra que los parámetros con valores por defecto deben ir al final.