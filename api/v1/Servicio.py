from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import Any, List

from models.DataModel import Servicio
from models.Servicio import ServicioBase
from config import SessionLocal
from abstract.AbstractAPI import AbstractAPI

# Crear un router para la API de Servicio
router = APIRouter(prefix="/v1/servicio", tags=["Servicio"])

# Crear una instancia de AbstractAPI para Servicio
servicio_api = AbstractAPI(Servicio, SessionLocal())

# Dependencia para obtener la sesión de base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Ruta para crear un nuevo servicio
@router.post("/", response_model=ServicioBase)
def create_servicio(servicio: ServicioBase, db: Session = Depends(get_db)):
    return servicio_api.create(servicio, db)

# Ruta para obtener un servicio por ID
@router.get("/{servicio_id}", response_model=ServicioBase)
def get_servicio(servicio_id: str, db: Session = Depends(get_db)):
    return servicio_api.get(servicio_id, db)

# Ruta para actualizar un servicio existente
@router.put("/{servicio_id}", response_model=ServicioBase)
def update_servicio(servicio_id: str, servicio: ServicioBase, db: Session = Depends(get_db)):
    return servicio_api.update(servicio_id, servicio, db)

# Ruta para eliminar un servicio por ID
@router.delete("/{servicio_id}", response_model=dict)
def delete_servicio(servicio_id: str, db: Session = Depends(get_db)):
    servicio_api.delete(servicio_id, db)
    return {"message": f"Servicio with ID {servicio_id} has been deleted"}

# Ruta para listar todos los servicios
@router.get("/", response_model=List[ServicioBase])
def list_servicios(db: Session = Depends(get_db)):
    return servicio_api.list()

# Ruta para filtrar servicios por un campo y valor
@router.get("/filter/{field}/{value}", response_model=List[ServicioBase])
def filter_servicios(field: str, value: Any, db: Session = Depends(get_db)):
    return servicio_api.filter(field, value)
