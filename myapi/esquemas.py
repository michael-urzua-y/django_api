SCHEMA_MAP = {
    "finanzas": "prontopaga_1",
    "Cliente_2": "schema_cliente_2",
    "Cliente_3": "schema_cliente_3",
}

def get_schema_for_client(client_id: str) -> str:
    try:
        return SCHEMA_MAP[client_id]
    except KeyError:
        raise ValueError(f"Cliente '{client_id}' no tiene un esquema asignado.")
