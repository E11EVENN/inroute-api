from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import Any

from config import SessionLocal
from models.DataModel import Entrenamiento
from models.Entrenamiento import EntrenamientoBase
from abstract.AbstractAPI import AbstractAPI

# Crear un router para la API de Entrenamiento
router = APIRouter(prefix="/v1/entrenamiento", tags=["Entrenamiento"])

# Crear una instancia de AbstractAPI para Entrenamiento
entrenamiento_api = AbstractAPI(Entrenamiento, SessionLocal())

# Dependencia para obtener la sesión de base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Ruta para crear un nuevo entrenamiento
@router.post("/", response_model=EntrenamientoBase)
def create_entrenamiento(entrenamiento: EntrenamientoBase, db: Session = Depends(get_db)):
    return entrenamiento_api.create(entrenamiento, db)

# Ruta para obtener un entrenamiento por ID
@router.get("/{entrenamiento_id}", response_model=EntrenamientoBase)
def get_entrenamiento(entrenamiento_id: str, db: Session = Depends(get_db)):
    return entrenamiento_api.get(entrenamiento_id, db)

# Ruta para actualizar un entrenamiento existente
@router.put("/{entrenamiento_id}", response_model=EntrenamientoBase)
def update_entrenamiento(entrenamiento_id: str, entrenamiento: EntrenamientoBase, db: Session = Depends(get_db)):
    return entrenamiento_api.update(entrenamiento_id, entrenamiento, db)

# Ruta para eliminar un entrenamiento por ID
@router.delete("/{entrenamiento_id}", response_model=dict)
def delete_entrenamiento(entrenamiento_id: str, db: Session = Depends(get_db)):
    entrenamiento_api.delete(entrenamiento_id, db)
    return {"message": f"Entrenamiento with ID {entrenamiento_id} has been deleted"}

# Ruta para listar todos los entrenamientos
@router.get("/", response_model=list[EntrenamientoBase])
def list_entrenamientos(db: Session = Depends(get_db)):
    return entrenamiento_api.list()

# Ruta para filtrar entrenamientos por un campo y valor
@router.get("/filter/{field}/{value}", response_model=list[EntrenamientoBase])
def filter_entrenamientos(field: str, value: Any, db: Session = Depends(get_db)):
    return entrenamiento_api.filter(field, value, db)