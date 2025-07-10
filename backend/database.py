from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base, relationship
from datetime import datetime
from dotenv import load_dotenv
import os

# Cargar variables del .env
load_dotenv()

# Leer la URL de la base de datos
DATABASE_URL = os.getenv("DATABASE_URL")

# Crear el engine
engine = create_engine(DATABASE_URL)

# Crear la sesión
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para tus modelos
Base = declarative_base()

# Dependencia para FastAPI
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class notasDB(Base):
    __tablename__ = "notas"

    id = Column(Integer, primary_key=True, autoincrement=True)
    titulo = Column(String(512), nullable=False)
    descripcion = Column(String(1024), nullable=False)
    ia = Column(String(1024), nullable=False)
    etiqueta1 = Column(String(512), nullable=False)
    etiqueta2 = Column(String(512), nullable=False)
    etiqueta3 = Column(String(512), nullable=False)