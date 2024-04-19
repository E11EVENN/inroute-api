from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import Any

from config import SessionLocal
from models.DataModel import TipoActividad
from models.TipoActividad import TipoActividadBase
from abstract.AbstractAPI import AbstractAPI

# Crear un router para la API de TipoActividad
router = APIRouter(prefix="/v1/tipo_actividad", tags=["TipoActividad"])

# Crear una instancia de AbstractAPI para TipoActividad
tipo_actividad_api = AbstractAPI(TipoActividad, SessionLocal())

# Dependencia para obtener la sesión de base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Ruta para crear un nuevo tipo de actividad
@router.post("/", response_model=TipoActividadBase)
def create_tipo_actividad(tipo_actividad: TipoActividadBase, db: Session = Depends(get_db)):
    return tipo_actividad_api.create(tipo_actividad, db)

# Ruta para obtener un tipo de actividad por ID
@router.get("/{tipo_actividad_id}", response_model=TipoActividadBase)
def get_tipo_actividad(tipo_actividad_id: str, db: Session = Depends(get_db)):
    return tipo_actividad_api.get(tipo_actividad_id, db)

# Ruta para actualizar un tipo de actividad existente
@router.put("/{tipo_actividad_id}", response_model=TipoActividadBase)
def update_tipo_actividad(tipo_actividad_id: str, tipo_actividad: TipoActividadBase, db: Session = Depends(get_db)):
    return tipo_actividad_api.update(tipo_actividad_id, tipo_actividad, db)

# Ruta para eliminar un tipo de actividad por ID
@router.delete("/{tipo_actividad_id}", response_model=dict)
def delete_tipo_actividad(tipo_actividad_id: str, db: Session = Depends(get_db)):
    tipo_actividad_api.delete(tipo_actividad_id, db)
    return {"message": f"TipoActividad with ID {tipo_actividad_id} has been deleted"}

# Ruta para listar todos los tipos de actividad
@router.get("/", response_model=list[TipoActividadBase])
def list_tipos_actividad(db: Session = Depends(get_db)):
    return tipo_actividad_api.list()

# Ruta para filtrar tipos de actividad por un campo y valor
@router.get("/filter/{field}/{value}", response_model=list[TipoActividadBase])
def filter_tipos_actividad(field: str, value: Any, db: Session = Depends(get_db)):
    return tipo_actividad_api.filter(field, value, db)
