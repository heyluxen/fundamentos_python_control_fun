transacciones = [
    {"id": 1, "monto": 1200, "estado": "completada"},
    {"id": 2, "monto": -50, "estado": "error"},
    {"id": 3, "monto": 800, "estado": "pendiente"},
    {"id": 4, "monto": 1500, "estado": "completada"},
    {"id": 5, "monto": 0, "estado": "cancelada"}
]  # Lista de transacciones

total_procesado = 0  # Acumulador del total

for t in transacciones:  # Recorre cada transacción
    if t["estado"] != "completada":  # Verifica si no está completada
        print(f"Transacción {t['id']}: {t['estado']} - ignorada")  # Muestra mensaje
        continue  # Salta la transacción

    if t["monto"] <= 0:  # Verifica si el monto es inválido
        print(f"Transacción {t['id']}: monto inválido ({t['monto']})")  # Muestra mensaje
        continue  # Salta la transacción

    total_procesado += t["monto"]  # Suma el monto válido
    print(f"Transacción {t['id']}: {t['monto']}€ procesada")  # Muestra mensaje

print(f"Total procesado: {total_procesado}€")  # Muestra total

# Este ejemplo procesa transacciones válidas e ignora las no completadas o con montos inválidos.

# Salida:
#Transacción 1: 1200€ procesada
#Transacción 2: error - ignorada
#Transacción 3: pendiente - ignorada
#Transacción 4: 1500€ procesada
#Transacción 5: cancelada - ignorada
#Total procesado: 2700€