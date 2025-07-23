from apps.products.persistence.repositories import (
    get_all_products,
    get_product_by_id,
    create_product,
    update_product,
    delete_product
)
from apps.products.infrastructure.handlers import notify_product_created

def create_new_product(data):
    product = create_product(data)
    notify_product_created(product)
    return product

def get_product(product_id):
    return get_product_by_id(product_id)

def get_products():
    return get_all_products()

def update_existing_product(product_id, data):
    product = get_product_by_id(product_id)
    if not product:
        return None
    return update_product(product, data)

def delete_existing_product(product_id):
    return delete_product(product_id)
