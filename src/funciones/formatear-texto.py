def formatear_texto(texto, mayusculas=False, prefijo="", sufijo="", separador=" "):  # Función para formatear texto
    if mayusculas:  # Verifica si se debe convertir a mayúsculas
        texto = texto.upper()

    palabras = texto.split()  # Divide el texto en palabras

    palabras_formateadas = [f"{prefijo}{palabra}{sufijo}" for palabra in palabras]  # Aplica formato

    resultado = separador.join(palabras_formateadas)  # Une las palabras

    return resultado  # Devuelve el texto final

# Texto original
texto_original = "python es un lenguaje versátil"

print(formatear_texto(texto_original))  # Sin cambios
print(formatear_texto(texto_original, mayusculas=True))  # Mayúsculas
print(formatear_texto(texto_original, prefijo="«", sufijo="»"))  # Con símbolos
print(formatear_texto(texto_original, separador="-"))  # Cambia separador

print(formatear_texto(  # Combinación de opciones
    texto_original,
    mayusculas=True,
    prefijo="#",
    sufijo="!",
    separador="..."
))

# Este ejemplo formatea texto con diferentes opciones como mayúsculas, prefijos y separadores.

# Salida: 
# python es un lenguaje versátil
# PYTHON ES UN LENGUAJE VERSÁTIL
# «python» «es» «un» «lenguaje» «versátil»
# python-es-un-lenguaje-versátil
# PYTHON!...#ES!...#UN!...#LENGUAJE!...#VERSÁTIL!