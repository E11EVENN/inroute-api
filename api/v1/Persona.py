from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from config import SessionLocal
from models.DataModel import Persona
from models.Persona import PersonaBase
from abstract.AbstractAPI import AbstractAPI
from typing import Any

# Crear un enrutador (router) para los endpoints de la API
router = APIRouter(prefix="/v1/persona", tags=["Persona"])

# Crear una instancia de AbstractAPI para Persona
persona_api = AbstractAPI(Persona, SessionLocal())

# Dependencia para obtener la sesión de base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Ruta para crear una nueva persona
@router.post("/", response_model=PersonaBase)
def create_persona(persona: PersonaBase, db: Session = Depends(get_db)):
    return persona_api.create(persona, db)

# Ruta para obtener una persona por ID
@router.get("/{id}", response_model=PersonaBase)
def get_persona(id: int, db: Session = Depends(get_db)):
    return persona_api.get(id, db)

# Ruta para actualizar una persona existente
@router.put("/{id}", response_model=PersonaBase)
def update_persona(id: int, persona: PersonaBase, db: Session = Depends(get_db)):
    return persona_api.update(id, persona, db)

# Ruta para eliminar una persona por ID
@router.delete("/{id}", response_model=dict)
def delete_persona(id: int, db: Session = Depends(get_db)):
    persona_api.delete(id, db)
    return {"message": f"Persona with ID {id} has been deleted"}

# Ruta para listar todas las personas
@router.get("/", response_model=list[PersonaBase])
def list_personas(db: Session = Depends(get_db)):
    return persona_api.list()

# Ruta para filtrar personas por un campo y valor
@router.get("/filter/{field}/{value}", response_model=list[PersonaBase])
def filter_personas(field: str, value: Any, db: Session = Depends(get_db)):
    return persona_api.filter(field, value, db)