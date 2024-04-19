from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import Any

from config import SessionLocal
from models.DataModel import Proceso
from models.Proceso import ProcesoBase
from abstract.AbstractAPI import AbstractAPI

# Crear un router para la API de Proceso
router = APIRouter(prefix="/v1/proceso", tags=["Proceso"])

# Crear una instancia de AbstractAPI para Proceso
proceso_api = AbstractAPI(Proceso, SessionLocal())

# Dependencia para obtener la sesión de base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Ruta para crear un nuevo proceso
@router.post("/", response_model=ProcesoBase)
def create_proceso(proceso: ProcesoBase, db: Session = Depends(get_db)):
    return proceso_api.create(proceso, db)

# Ruta para obtener un proceso por ID
@router.get("/{proceso_id}", response_model=ProcesoBase)
def get_proceso(proceso_id: str, db: Session = Depends(get_db)):
    return proceso_api.get(proceso_id, db)

# Ruta para actualizar un proceso existente
@router.put("/{proceso_id}", response_model=ProcesoBase)
def update_proceso(proceso_id: str, proceso: ProcesoBase, db: Session = Depends(get_db)):
    return proceso_api.update(proceso_id, proceso, db)

# Ruta para eliminar un proceso por ID
@router.delete("/{proceso_id}", response_model=dict)
def delete_proceso(proceso_id: str, db: Session = Depends(get_db)):
    proceso_api.delete(proceso_id, db)
    return {"message": f"Proceso with ID {proceso_id} has been deleted"}

# Ruta para listar todos los procesos
@router.get("/", response_model=list[ProcesoBase])
def list_procesos(db: Session = Depends(get_db)):
    return proceso_api.list()

# Ruta para filtrar procesos por un campo y valor
@router.get("/filter/{field}/{value}", response_model=list[ProcesoBase])
def filter_procesos(field: str, value: Any, db: Session = Depends(get_db)):
    return proceso_api.filter(field, value, db)