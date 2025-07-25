from apps.payments.persistence import repositories
from django.db import connection

def get_payment_report(payload: dict):
    metodo = payload.get("metodo")
    esquema = payload.get("esquema_bd")

    if metodo not in REPOSITORY_DISPATCHER:
        raise ValueError(f"Método '{metodo}' no soportado.")

    query_func = REPOSITORY_DISPATCHER[metodo]

    # Permite que cada función reciba todo el payload y use lo que necesite
    query = query_func(payload)

    with connection.cursor() as cursor:
        cursor.execute(f"SET search_path TO {esquema};")
        cursor.execute(query)
        columns = [col[0] for col in cursor.description]
        results = [dict(zip(columns, row)) for row in cursor.fetchall()]
    return results

# Diccionario de funciones para cada método
REPOSITORY_DISPATCHER = {
    "payin": repositories.get_payin_query,
    "payout": repositories.get_payout_query,
    # más métodos aquí
}
