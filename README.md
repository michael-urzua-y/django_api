# django_api
django_api



 <!-- Flujo completo de una operación (por ejemplo, crear un producto)
1. Cliente (Frontend o Postman)
Envía una solicitud POST /api/products/ con datos JSON.

2. Capa de Presentación (views.py)
Recibe la solicitud.
Usa ProductSerializer para validar los datos.
Si son válidos, llama a services.create_new_product(data).
3. Capa de Aplicación (services.py)
Orquesta la operación.
Llama a repositories.create_product(data) para guardar en la base de datos.
Luego llama a handlers.notify_product_created(product) para emitir un evento o log.
4. Capa de Persistencia (repositories.py)
Ejecuta la operación con el ORM de Django (Product.objects.create(...)).
5. Capa de Infraestructura (handlers.py)
Ejecuta acciones externas o transversales (logs, notificaciones, etc.).
6. Respuesta
El producto creado se devuelve a views.py, que lo serializa y responde al cliente. -->