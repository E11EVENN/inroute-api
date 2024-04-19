from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import Any

from config import SessionLocal
from models.DataModel import TipoEntrenamiento
from models.TipoEntrenamiento import TipoEntrenamientoBase
from abstract.AbstractAPI import AbstractAPI

# Crear un router para la API de TipoEntrenamiento
router = APIRouter(prefix="/v1/tipo_entrenamiento", tags=["TipoEntrenamiento"])

# Crear una instancia de AbstractAPI para TipoEntrenamiento
tipo_entrenamiento_api = AbstractAPI(TipoEntrenamiento, SessionLocal())

# Dependencia para obtener la sesión de base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Ruta para crear un nuevo tipo de entrenamiento
@router.post("/", response_model=TipoEntrenamientoBase)
def create_tipo_entrenamiento(tipo_entrenamiento: TipoEntrenamientoBase, db: Session = Depends(get_db)):
    return tipo_entrenamiento_api.create(tipo_entrenamiento, db)

# Ruta para obtener un tipo de entrenamiento por ID
@router.get("/{tipo_entrenamiento_id}", response_model=TipoEntrenamientoBase)
def get_tipo_entrenamiento(tipo_entrenamiento_id: str, db: Session = Depends(get_db)):
    return tipo_entrenamiento_api.get(tipo_entrenamiento_id, db)

# Ruta para actualizar un tipo de entrenamiento existente
@router.put("/{tipo_entrenamiento_id}", response_model=TipoEntrenamientoBase)
def update_tipo_entrenamiento(tipo_entrenamiento_id: str, tipo_entrenamiento: TipoEntrenamientoBase, db: Session = Depends(get_db)):
    return tipo_entrenamiento_api.update(tipo_entrenamiento_id, tipo_entrenamiento, db)

# Ruta para eliminar un tipo de entrenamiento por ID
@router.delete("/{tipo_entrenamiento_id}", response_model=dict)
def delete_tipo_entrenamiento(tipo_entrenamiento_id: str, db: Session = Depends(get_db)):
    tipo_entrenamiento_api.delete(tipo_entrenamiento_id, db)
    return {"message": f"TipoEntrenamiento with ID {tipo_entrenamiento_id} has been deleted"}

# Ruta para listar todos los tipos de entrenamiento
@router.get("/", response_model=list[TipoEntrenamientoBase])
def list_tipos_entrenamiento(db: Session = Depends(get_db)):
    return tipo_entrenamiento_api.list()

# Ruta para filtrar tipos de entrenamiento por un campo y valor
@router.get("/filter/{field}/{value}", response_model=list[TipoEntrenamientoBase])
def filter_tipos_entrenamiento(field: str, value: Any, db: Session = Depends(get_db)):
    return tipo_entrenamiento_api.filter(field, value, db)