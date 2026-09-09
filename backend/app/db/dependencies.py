# Crear una sesión para la petición y asegurarse de cerrarla cuando termine.
from collections.abc import Generator
from sqlalchemy.orm import Session
from app.db.session import SessionLocal

def get_db() -> Generator[Session, None,None]:
    db= SessionLocal()
    try: 
        yield db #la sesión que necesita el endpoin
    finally:
        db.close() # Cuando termine la petición, cierra la sesión.