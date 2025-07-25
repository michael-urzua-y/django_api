# 🧠 ¿Qué es?
# Este archivo se encarga de manejar eventos del sistema o integraciones externas. Aquí defines funciones que reaccionan a ciertos eventos, como la creación de un producto, y que podrían, por ejemplo, enviar notificaciones, registrar logs, o interactuar con otros servicios.

# 🧩 ¿Qué debería contener?
# Funciones que actúan como handlers de eventos.
# Lógica que no pertenece directamente al dominio ni a la lógica de negocio.
# Puede estar conectado con signals.py si usas señales de Django.

# apps/products/infrastructure/handlers.py

