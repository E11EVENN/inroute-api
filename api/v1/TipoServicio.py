from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import Any, List

from models.DataModel import TipoServicio
from models.TipoServicio import TipoServicioBase
from config import SessionLocal
from abstract.AbstractAPI import AbstractAPI

# Crear un router para la API de TipoServicio
router = APIRouter(prefix="/v1/tipo_servicio", tags=["TipoServicio"])

# Crear una instancia de AbstractAPI para TipoServicio
tipo_servicio_api = AbstractAPI(TipoServicio, SessionLocal())

# Dependencia para obtener la sesión de base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Ruta para crear un nuevo tipo de servicio
@router.post("/", response_model=TipoServicioBase)
def create_tipo_servicio(tipo_servicio: TipoServicioBase, db: Session = Depends(get_db)):
    return tipo_servicio_api.create(tipo_servicio, db)

# Ruta para obtener un tipo de servicio por ID
@router.get("/{tipo_servicio_id}", response_model=TipoServicioBase)
def get_tipo_servicio(tipo_servicio_id: str, db: Session = Depends(get_db)):
    return tipo_servicio_api.get(tipo_servicio_id, db)

# Ruta para actualizar un tipo de servicio existente
@router.put("/{tipo_servicio_id}", response_model=TipoServicioBase)
def update_tipo_servicio(tipo_servicio_id: str, tipo_servicio: TipoServicioBase, db: Session = Depends(get_db)):
    return tipo_servicio_api.update(tipo_servicio_id, tipo_servicio, db)

# Ruta para eliminar un tipo de servicio por ID
@router.delete("/{tipo_servicio_id}", response_model=dict)
def delete_tipo_servicio(tipo_servicio_id: str, db: Session = Depends(get_db)):
    tipo_servicio_api.delete(tipo_servicio_id, db)
    return {"message": f"TipoServicio with ID {tipo_servicio_id} has been deleted"}

# Ruta para listar todos los tipos de servicio
@router.get("/", response_model=List[TipoServicioBase])
def list_tipos_servicio(db: Session = Depends(get_db)):
    return tipo_servicio_api.list()

# Ruta para filtrar tipos de servicio por un campo y valor
@router.get("/filter/{field}/{value}", response_model=List[TipoServicioBase])
def filter_tipos_servicio(field: str, value: Any, db: Session = Depends(get_db)):
    return tipo_servicio_api.filter(field, value)