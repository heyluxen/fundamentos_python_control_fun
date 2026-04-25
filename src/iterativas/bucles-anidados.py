for i in range(1, 4):  # Recorre grupos del 1 al 3
    print(f"Grupo {i}:")  # Muestra el grupo actual

    for j in range(1, 6):  # Recorre elementos del 1 al 5
        if j == 3:  # Verifica si el elemento es 3
            print("  Saltando el elemento 3")  # Muestra mensaje
            continue  # Salta solo en el bucle interno

        print(f"  Elemento {j}")  # Muestra el elemento

    print("Fin del grupo\n")  # Indica fin del grupo

# Este ejemplo usa bucles anidados y salta el elemento 3 en cada grupo. 

# Salida:
#Grupo 1:
#  Elemento 1
#  Elemento 2
#  Saltando el elemento 3
#  Elemento 4
#  Elemento 5
#Fin del grupo

#Grupo 2:
#  Elemento 1
#  Elemento 2
#  Saltando el elemento 3
#  Elemento 4
#  Elemento 5
#Fin del grupo

#Grupo 3:
#  Elemento 1
#  Elemento 2
#  Saltando el elemento 3
#  Elemento 4
#  Elemento 5
#Fin del grupo