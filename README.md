# django_api
django_api


# 📘 Flujo de Petición en la API Django con Esquema Dinámico

Este documento describe el flujo completo de una petición HTTP en una API construida con Django, utilizando esquemas dinámicos en PostgreSQL. El ejemplo se basa en una petición a la ruta `/api/users/` con el parámetro `schema=finanzas`.

---

## 🔄 Flujo de la Petición Paso a Paso

### 1. 📨 Petición desde Postman
- Se realiza una petición GET a:
  ```
http://localhost:8000/api/users/?schema=finanzas

- El parámetro `schema=finanzas` indica qué esquema de base de datos se debe usar.

---

### 2. 🌐 Enrutamiento (Routing)
- Django recibe la petición y la procesa a través de `myapi/urls.py`.
- Este archivo incluye las rutas de `api/urls.py`.
- Luego, `api/urls.py` delega a `apps/users/presentation/urls.py`, donde está definida la ruta `/users/`.

---

### 3. 👁️ Vista (View)
- La vista correspondiente en `apps/users/presentation/views.py` se activa.
- Esta vista hereda de `APIView` y ejecuta el método `get()` (u otro según el verbo HTTP).

---

### 4. 🧩 Middleware de esquema dinámico
- Antes de llegar a la vista, el middleware `schema_middleware.py` intercepta la petición.
- Extrae el parámetro `schema` de la URL (`finanzas`) y configura el `search_path` de PostgreSQL dinámicamente:
python
cursor.execute(f"SET search_path TO {schema}")

### 5. 🧠 Capa de servicios (Application Layer)
La vista llama a una función en apps/users/application/services.py para manejar la lógica de negocio.
Esta función se comunica con la capa de persistencia.

### 6. 🗃️ Capa de persistencia (Repositories)
Este archivo define el repositorio para el modelo User.
Encapsula el DAO y agrega lógica para configurar dinámicamente el esquema de base de datos antes de cada operación.
Sirve como puente entre la capa de aplicación y la persistencia, facilitando el acceso desacoplado a los datos.

### 7. 🗃️ Capa de persistencia (DAO)
Este archivo define el Data Access Object (DAO) para el modelo User.
Contiene métodos estáticos que interactúan directamente con la base de datos usando el ORM de Django.
No maneja lógica de negocio ni configuración de esquemas, solo operaciones CRUD básicas.

### 8. 🧱 Modelos (Domain Layer)
Los modelos en apps/users/domain/user_model.py definen la estructura de los datos que se consultan.

### 9. 🔄 Serialización
Los datos obtenidos se pasan a un serializer en apps/users/presentation/serializers.py.
El serializer convierte los datos a formato JSON.

### 10. 📤 Respuesta
Finalmente, la vista devuelve la respuesta serializada a Postman en formato JSON.