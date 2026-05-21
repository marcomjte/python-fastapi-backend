# insertar_usuario.py  (en la raíz de backend/)
from app.database import SessionLocal
from app.models.user import User
from passlib.context import CryptContext

pwd_ctx = CryptContext(schemes=["bcrypt"], deprecated="auto")
db      = SessionLocal()

user = User(
    name     = "Admin",
    email    = "admin@test.com",
    password = pwd_ctx.hash("12345"),
)

db.add(user)
db.commit()
print("User created:", user.email)
db.close()