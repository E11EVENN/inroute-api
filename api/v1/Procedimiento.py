from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import Any

from config import SessionLocal
from models.DataModel import Procedimiento
from models.Procedimiento import ProcedimientoBase
from abstract.AbstractAPI import AbstractAPI

# Crear un router para la API de Procedimiento
router = APIRouter(prefix="/v1/procedimiento", tags=["Procedimiento"])

# Crear una instancia de AbstractAPI para Procedimiento
procedimiento_api = AbstractAPI(Procedimiento, SessionLocal())

# Dependencia para obtener la sesión de base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Ruta para crear un nuevo procedimiento
@router.post("/", response_model=ProcedimientoBase)
def create_procedimiento(procedimiento: ProcedimientoBase, db: Session = Depends(get_db)):
    return procedimiento_api.create(procedimiento, db)

# Ruta para obtener un procedimiento por ID
@router.get("/{procedimiento_id}", response_model=ProcedimientoBase)
def get_procedimiento(procedimiento_id: str, db: Session = Depends(get_db)):
    return procedimiento_api.get(procedimiento_id, db)

# Ruta para actualizar un procedimiento existente
@router.put("/{procedimiento_id}", response_model=ProcedimientoBase)
def update_procedimiento(procedimiento_id: str, procedimiento: ProcedimientoBase, db: Session = Depends(get_db)):
    return procedimiento_api.update(procedimiento_id, procedimiento, db)

# Ruta para eliminar un procedimiento por ID
@router.delete("/{procedimiento_id}", response_model=dict)
def delete_procedimiento(procedimiento_id: str, db: Session = Depends(get_db)):
    procedimiento_api.delete(procedimiento_id, db)
    return {"message": f"Procedimiento with ID {procedimiento_id} has been deleted"}

# Ruta para listar todos los procedimientos
@router.get("/", response_model=list[ProcedimientoBase])
def list_procedimientos(db: Session = Depends(get_db)):
    return procedimiento_api.list()

# Ruta para filtrar procedimientos por un campo y valor
@router.get("/filter/{field}/{value}", response_model=list[ProcedimientoBase])
def filter_procedimientos(field: str, value: Any, db: Session = Depends(get_db)):
    return procedimiento_api.filter(field, value, db)