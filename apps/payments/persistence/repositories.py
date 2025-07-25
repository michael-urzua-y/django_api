from psycopg2 import sql

# inbd 
# metodo cone bd

# meoto listado de esqumas  = comercio entrante del json



def get_payin_query(payload: dict):
    schema_name = payload["esquema_bd"]
    return sql.SQL("""
        SELECT 
            p.reference AS "Referencia",
            cl.fullname AS "Nombre",
            s.statu AS "Estado",
            t.type AS "Tipo",
            m.method AS "Método",
            co.name AS "Comercio",
            cu.name AS "Moneda",
            p.created_at AS "Creado"
        FROM {schema}.payin p
        LEFT JOIN {schema}.client cl ON p.client_id = cl.client_id
        LEFT JOIN {schema}.commerce co ON cl.commerce_id = co.commerce_id
        LEFT JOIN {schema}.status s ON p.statu_id = s.statu_id
        LEFT JOIN {schema}.types t ON p.type_id = t.type_id
        LEFT JOIN {schema}.methods m ON p.method_id = m.method_id
        LEFT JOIN {schema}.currency cu ON p.currency_id = cu.currency_id
    """).format(schema=sql.Identifier(schema_name))


def get_payout_query(payload: dict):
    schema_name = payload["esquema_bd"]
    return sql.SQL("""
        SELECT
            p.reference AS "Referencia",
            u.name AS "Usuario",
            ctry.country AS "Pais",
            s.statu AS "Estado",
            t.type AS "Tipo",
            com.name AS "Comercio",
            cur.name AS "Moneda"
        FROM {schema}.payin p
        JOIN {schema}.client cl ON p.client_id = cl.client_id
        JOIN {schema}.commerce com ON cl.commerce_id = com.commerce_id
        JOIN {schema}.user u ON com.commerce_id = u.commerce_id
        LEFT JOIN {schema}.countrys ctry ON p.country_id = ctry.country_id
        LEFT JOIN {schema}.status s ON p.statu_id = s.statu_id
        LEFT JOIN {schema}.types t ON p.type_id = t.type_id
        LEFT JOIN {schema}.currency cur ON p.currency_id = cur.currency_id
    """).format(schema=sql.Identifier(schema_name))
