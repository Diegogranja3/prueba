import os
from dotenv import load_dotenv 
import google.generativeai as genai
from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from pydantic import BaseModel, ConfigDict
from database import notasDB, get_db, Base, engine
from typing import Optional

app = FastAPI()
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)

# ⚠️ IMPORTANTE: permite el origen del frontend (Vue)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # o ["*"] para permitir todo (no recomendado en producción)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Pregunta(BaseModel):
    mensaje: str

class NotaCreate(BaseModel):
    titulo: str
    descripcion: str
    ia: str
    etiqueta1: str
    etiqueta2: str
    etiqueta3: str

class NotaSchema(BaseModel):
    titulo: str
    descripcion: str
    ia: Optional[str] = None
    etiqueta1: Optional[str] = ''
    etiqueta2: Optional[str] = ''
    etiqueta3: Optional[str] = ''

    model_config = ConfigDict(from_attributes=True)  #

@app.post("/preguntar_gemini/")
def preguntar_gemini(pregunta: Pregunta):
    print("Mensaje recibido:", pregunta.mensaje)  # <--- Agregado

    try:
        model = genai.GenerativeModel("models/gemini-2.5-pro")
        response = model.generate_content(pregunta.mensaje)
        print("Respuesta IA:", response.text)  # <--- Agregado
        return {"respuesta": response.text}
    except Exception as e:
        print("ERROR AL PROCESAR:", str(e))  # <--- Agregado
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/guardar_nota/")
def guardar_nota(nota: NotaCreate, db: Session = Depends(get_db)):
    nueva_nota = notasDB(**nota.dict())
    db.add(nueva_nota)
    db.commit()
    db.refresh(nueva_nota)
    return {"mensaje": "Nota guardada con éxito", "id": nueva_nota.id}

@app.get("/notas/")
def obtener_notas(db: Session = Depends(get_db)):
    notas = db.query(notasDB).all()
    return notas

@app.delete("/eliminar_nota/{id}")
async def eliminar_nota(id: int, db: Session = Depends(get_db)):
    nota = db.query(notasDB).filter(notasDB.id == id).first()
    if nota:
        db.delete(nota)
        db.commit()
        return {"mensaje": "Nota eliminada"}
    raise HTTPException(status_code=404, detail="Nota no encontrada")

@app.put("/editar_nota/{nota_id}")
def editar_nota(nota_id: int, nota: NotaSchema, db: Session = Depends(get_db)):
    db_nota = db.query(notasDB).filter(notasDB.id == nota_id).first()
    if not db_nota:
        raise HTTPException(status_code=404, detail="Nota no encontrada")

    db_nota.titulo = nota.titulo
    db_nota.descripcion = nota.descripcion
    db_nota.ia = nota.ia
    db_nota.etiqueta1 = nota.etiqueta1
    db_nota.etiqueta2 = nota.etiqueta2
    db_nota.etiqueta3 = nota.etiqueta3
    db.commit()
    db.refresh(db_nota)
    return db_nota
