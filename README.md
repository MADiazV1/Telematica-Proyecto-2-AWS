# 📚 Bookstore - Sistema de Microservicios

Plataforma web distribuida para la gestión de libros, compras y administración de usuarios, implementada con arquitectura de microservicios.

---

## 🧱 Microservicios

- **auth-service**: Registro, login y emisión de tokens JWT.
- **catalog-service**: Catálogo, publicación y gestión de libros.
- **order-service**: Compras, pagos y asignación de entregas.
- **admin-service**: Visualización de usuarios (solo para admin).
- **web-service**: Interfaz web para los usuarios finales (gateway visual).

---

## 🚀 Requisitos

- Docker y Docker Compose instalados
- (Opcional) Python 3.10+ para desarrollo local

---

## 🧪 Configuración

Cada microservicio tiene su propio archivo `.env` para las variables de entorno necesarias, como claves secretas y URLs internas. Asegúrate de definirlos correctamente antes de ejecutar el sistema.

---

## 🐳 Ejecución

El sistema se ejecuta como un conjunto de contenedores Docker conectados por una red compartida. Todos los servicios están definidos en el `docker-compose.yml` principal.

Al iniciarse, los microservicios estarán disponibles en:

- `web-service`: http://localhost:8000
- `auth-service`: http://localhost:5000
- `catalog-service`: http://localhost:5001
- `order-service`: http://localhost:5002
- `admin-service`: http://localhost:5003

---

## 👥 Flujo de uso

1. Registrarse en la plataforma.
2. Iniciar sesión con email y contraseña.
3. Ver el catálogo de libros.
4. Si eres vendedor, agregar/editar tus libros.
5. Comprar un libro desde el catálogo.
6. Pagar la compra.
7. Seleccionar un proveedor de entrega.
8. Si eres administrador, acceder a la lista de usuarios registrados.

---

## 📫 API REST

Puedes probar las APIs directamente desde Postman o tu frontend `web-service`. Cada servicio expone sus endpoints bajo rutas claras y documentadas, y los tokens JWT se manejan mediante cabeceras de autorización estándar.

---

## 💡 Buenas prácticas aplicadas

- Microservicios independientes con sus propias bases de datos.
- Comunicación vía HTTP con tokens JWT.
- Dockerización completa de cada servicio.
- Código limpio, separado por capas (rutas, servicios, modelos).
- Sesión y autenticación persistente en `web-service`.

---
