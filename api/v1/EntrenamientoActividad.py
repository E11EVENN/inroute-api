from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import Any

from config import SessionLocal
from models.DataModel import EntrenamientoActividad
from models.EntrenamientoActividad import EntrenamientoActividadBase
from abstract.AbstractAPI import AbstractAPI

# Crear un router para la API de EntrenamientoActividad
router = APIRouter(prefix="/v1/entrenamiento_actividad", tags=["EntrenamientoActividad"])

# Crear una instancia de AbstractAPI para EntrenamientoActividad
entrenamiento_actividad_api = AbstractAPI(EntrenamientoActividad, SessionLocal())

# Dependencia para obtener la sesión de base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Ruta para crear una nueva actividad de entrenamiento
@router.post("/", response_model=EntrenamientoActividadBase)
def create_entrenamiento_actividad(entrenamiento_actividad: EntrenamientoActividadBase, db: Session = Depends(get_db)):
    return entrenamiento_actividad_api.create(entrenamiento_actividad, db)

# Ruta para obtener una actividad de entrenamiento por ID
@router.get("/{entrenamiento_actividad_id}", response_model=EntrenamientoActividadBase)
def get_entrenamiento_actividad(entrenamiento_actividad_id: int, db: Session = Depends(get_db)):
    return entrenamiento_actividad_api.get(entrenamiento_actividad_id, db)

# Ruta para actualizar una actividad de entrenamiento existente
@router.put("/{entrenamiento_actividad_id}", response_model=EntrenamientoActividadBase)
def update_entrenamiento_actividad(entrenamiento_actividad_id: int, entrenamiento_actividad: EntrenamientoActividadBase, db: Session = Depends(get_db)):
    return entrenamiento_actividad_api.update(entrenamiento_actividad_id, entrenamiento_actividad, db)

# Ruta para eliminar una actividad de entrenamiento por ID
@router.delete("/{entrenamiento_actividad_id}", response_model=dict)
def delete_entrenamiento_actividad(entrenamiento_actividad_id: int, db: Session = Depends(get_db)):
    entrenamiento_actividad_api.delete(entrenamiento_actividad_id, db)
    return {"message": f"EntrenamientoActividad with ID {entrenamiento_actividad_id} has been deleted"}

# Ruta para listar todas las actividades de entrenamiento
@router.get("/", response_model=list[EntrenamientoActividadBase])
def list_entrenamiento_actividades(db: Session = Depends(get_db)):
    return entrenamiento_actividad_api.list()

# Ruta para filtrar actividades de entrenamiento por un campo y valor
@router.get("/filter/{field}/{value}", response_model=list[EntrenamientoActividadBase])
def filter_entrenamiento_actividades(field: str, value: Any, db: Session = Depends(get_db)):
    return entrenamiento_actividad_api.filter(field, value, db)