# python-fastapi-backend

API REST desarrollada en FastAPI + MySQL para el sistema de autenticación y gestión de datos.
Frontend: `https://github.com/marcomjte/nextjs-fastapi-frontend`

---

## Tecnologías

| Tecnología | Versión | Uso |
|---|---|---|
| Python | 3.11+ | Lenguaje base |
| FastAPI | latest | Framework API REST |
| SQLAlchemy | latest | ORM |
| PyMySQL | latest | Conector MySQL |
| Pydantic | v2 | Validación de datos y schemas |
| Passlib + bcrypt | 4.0.1 | Hash de contraseñas |
| Python-Jose | latest | Generación y verificación de JWT |
| Uvicorn | latest | Servidor ASGI |
| python-dotenv | latest | Variables de entorno |

---

## Estructura del proyecto

```
backend/
├── app/
│   ├── __init__.py
│   ├── main.py              # Entrada de la aplicación, CORS, registro de routers
│   ├── database.py          # Conexión a MySQL, sesión y Base declarativa
│   ├── models/
│   │   ├── __init__.py
│   │   └── user.py          # Modelo SQLAlchemy de la tabla users
│   ├── routers/
│   │   ├── __init__.py
│   │   └── auth.py          # Endpoints de autenticación (/auth/login, /auth/me)
│   └── schemas/
│       ├── __init__.py
│       └── user.py          # Schemas Pydantic (request/response)
├── insert_test_user.py      # Script para crear usuario de prueba
├── .env                     # Variables de entorno (no subir a git)
├── .gitignore
└── requirements.txt
```

---

## Endpoints disponibles

| Método | Ruta | Acceso | Descripción |
|---|---|---|---|
| GET | `/health` | Público | Verificación de estado del servidor |
| POST | `/auth/login` | Público | Iniciar sesión, retorna JWT |
| GET | `/auth/me` | Privado (JWT) | Retorna datos del usuario autenticado |

---

## Seguridad implementada

### Contraseñas
- Almacenadas con **hash bcrypt** mediante `passlib`
- Nunca se guarda ni retorna la contraseña en texto plano
- Verificación segura con `pwd_ctx.verify(input, hash)`

### JWT
- Tokens firmados con `python-jose` usando algoritmo **HS256**
- Payload contiene `sub` (ID de usuario), `email` y `exp` (expiración)
- El token **no está cifrado**, solo firmado — no guardar datos sensibles en el payload
- Expiración configurable via variable de entorno (por defecto 8 horas)

### Validación
- Todos los requests se validan automáticamente con **Pydantic v2**
- `EmailStr` valida formato de email antes de llegar al endpoint
- Respuestas tipadas con `response_model` — nunca se exponen campos no declarados

### CORS
- Configurado para aceptar requests solo del origen del frontend
- En producción reemplazar `allow_origins` con el dominio real

---

## Variables de entorno

Creá un archivo `.env` en la raíz del proyecto:

```bash
DB_USER=root
DB_PASSWORD=tu_password
DB_HOST=localhost
DB_PORT=3306
DB_NAME=myapp
JWT_SECRET=     # Mismo valor que NEXTAUTH_SECRET del frontend
JWT_ALGORITHM=HS256
JWT_EXPIRE_HOURS=8
```

> `JWT_SECRET` debe ser el mismo valor que `NEXTAUTH_SECRET` en el frontend para que ambos puedan verificar el mismo token.

---

## Instalación y uso

### Requisitos
- Python 3.11+
- MySQL 8+

### Pasos

```bash
# 1. Crear y activar entorno virtual
python -m venv venv
source venv/bin/activate      # Mac/Linux
venv\Scripts\activate         # Windows

# 2. Instalar dependencias
pip install -r requirements.txt

# 3. Crear la base de datos en MySQL
mysql -u root -p
CREATE DATABASE myapp CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

# 4. Configurar variables de entorno
cp .env.example .env
# Editar .env con tus valores

# 5. Levantar el servidor
uvicorn app.main:app --reload
# → http://localhost:8000
```

---

## Documentación interactiva

Con el servidor corriendo:

| URL | Descripción |
|---|---|
| `http://localhost:8000/docs` | Swagger UI |
| `http://localhost:8000/redoc` | ReDoc |
| `http://localhost:8000/openapi.json` | Schema OpenAPI en JSON |

---

## Crear usuario de prueba

```bash
python insertar_usuario.py
```

---

## Licencia

MIT