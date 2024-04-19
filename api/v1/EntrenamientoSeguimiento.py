from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import Any

from config import SessionLocal
from models.DataModel import EntrenamientoSeguimiento
from models.EntrenamientoSeguimiento import EntrenamientoSeguimientoBase
from abstract.AbstractAPI import AbstractAPI

# Crear un router para la API de EntrenamientoSeguimiento
router = APIRouter(prefix="/v1/entrenamiento_seguimiento", tags=["EntrenamientoSeguimiento"])

# Crear una instancia de AbstractAPI para EntrenamientoSeguimiento
entrenamiento_seguimiento_api = AbstractAPI(EntrenamientoSeguimiento, SessionLocal())

# Dependencia para obtener la sesión de base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Ruta para crear un nuevo seguimiento de entrenamiento
@router.post("/", response_model=EntrenamientoSeguimientoBase)
def create_entrenamiento_seguimiento(entrenamiento_seguimiento: EntrenamientoSeguimientoBase, db: Session = Depends(get_db)):
    return entrenamiento_seguimiento_api.create(entrenamiento_seguimiento, db)

# Ruta para obtener un seguimiento de entrenamiento por ID
@router.get("/{entrenamiento_seguimiento_id}", response_model=EntrenamientoSeguimientoBase)
def get_entrenamiento_seguimiento(entrenamiento_seguimiento_id: int, db: Session = Depends(get_db)):
    return entrenamiento_seguimiento_api.get(entrenamiento_seguimiento_id, db)

# Ruta para actualizar un seguimiento de entrenamiento existente
@router.put("/{entrenamiento_seguimiento_id}", response_model=EntrenamientoSeguimientoBase)
def update_entrenamiento_seguimiento(entrenamiento_seguimiento_id: int, entrenamiento_seguimiento: EntrenamientoSeguimientoBase, db: Session = Depends(get_db)):
    return entrenamiento_seguimiento_api.update(entrenamiento_seguimiento_id, entrenamiento_seguimiento, db)

# Ruta para eliminar un seguimiento de entrenamiento por ID
@router.delete("/{entrenamiento_seguimiento_id}", response_model=dict)
def delete_entrenamiento_seguimiento(entrenamiento_seguimiento_id: int, db: Session = Depends(get_db)):
    entrenamiento_seguimiento_api.delete(entrenamiento_seguimiento_id, db)
    return {"message": f"EntrenamientoSeguimiento with ID {entrenamiento_seguimiento_id} has been deleted"}

# Ruta para listar todos los seguimientos de entrenamiento
@router.get("/", response_model=list[EntrenamientoSeguimientoBase])
def list_entrenamiento_seguimientos(db: Session = Depends(get_db)):
    return entrenamiento_seguimiento_api.list()

# Ruta para filtrar seguimientos de entrenamiento por un campo y valor
@router.get("/filter/{field}/{value}", response_model=list[EntrenamientoSeguimientoBase])
def filter_entrenamiento_seguimientos(field: str, value: Any, db: Session = Depends(get_db)):
    return entrenamiento_seguimiento_api.filter(field, value, db)