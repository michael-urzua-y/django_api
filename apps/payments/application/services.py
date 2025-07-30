from apps.payments.persistence import repositories

def get_payment_report(payload: dict):
    metodo = payload.get("metodo")

    if metodo not in REPOSITORY_DISPATCHER:
        raise ValueError(f"Método '{metodo}' no soportado.")

    query_func = REPOSITORY_DISPATCHER[metodo]

    # Ejecuta la función ORM y retorna los resultados como lista de diccionarios
    results = query_func(payload)
    return results

# Diccionario de funciones para cada método
REPOSITORY_DISPATCHER = {
    "payin": repositories.get_payin_query,
    "payout": repositories.get_payout_query,
}
