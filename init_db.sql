-- Crear esquema 'api'
CREATE SCHEMA IF NOT EXISTS api;

-- Crear tabla 'products' en el esquema 'api'
CREATE TABLE api.products (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    description TEXT,
    price NUMERIC(10, 2),
    stock INTEGER
);

-- Crear tabla 'users' en el esquema 'api'
CREATE TABLE api.users (
    id INTEGER PRIMARY KEY,
    nombre TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL
);

-- Insertar datos en 'products'
INSERT INTO api.products (id, name, description, price, stock) VALUES
(1, 'Silla', 'Silla ergonómica', 49.99, 10),
(2, 'Mesa', 'Mesa de comedor', 89.99, 5);

-- Insertar datos en 'users'
INSERT INTO api.users (id, nombre, email) VALUES
(1, 'Juan', 'juan@example.com'),
(2, 'Ana', 'ana@example.com'),
(3, 'Luis', 'luis@example.com');