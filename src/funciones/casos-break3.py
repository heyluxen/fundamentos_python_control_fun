def es_primo(n):  # Función que verifica si un número es primo
    if n < 2:  # Los números menores que 2 no son primos
        return False

    for i in range(2, int(n**0.5) + 1):  # Recorre posibles divisores
        if n % i == 0:  # Verifica si es divisible
            return False  # No es primo

    return True  # Es primo

# Este ejemplo determina si un número es primo o no.