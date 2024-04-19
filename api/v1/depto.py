from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import Any, List

from models.DataModel import Depto
from models.Depto import DeptoBase
from config import SessionLocal
from abstract.AbstractAPI import AbstractAPI

# Crear un router para la API de Depto
router = APIRouter(prefix="/v1/depto", tags=["Depto"])

# Crear una instancia de AbstractAPI para Depto
depto_api = AbstractAPI(Depto, SessionLocal())

# Dependencia para obtener la sesión de base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally: 
        db.close()

# Ruta para crear un nuevo departamento
@router.post("/", response_model=DeptoBase)
def create_depto(depto: DeptoBase, db: Session = Depends(get_db)):
    return depto_api.create(depto)

# Ruta para obtener un departamento por ID
@router.get("/{depto_id}", response_model=DeptoBase)
def get_depto(depto_id: str, db: Session = Depends(get_db)):
    return depto_api.get(depto_id)

# Ruta para actualizar un departamento existente
@router.put("/{depto_id}", response_model=DeptoBase)
def update_depto(depto_id: str, depto: DeptoBase, db: Session = Depends(get_db)):
    return depto_api.update(depto_id, depto)

# Ruta para eliminar un departamento por ID
@router.delete("/{depto_id}", response_model=dict)
def delete_depto(depto_id: str, db: Session = Depends(get_db)):
    depto_api.delete(depto_id)
    return {"message": f"Depto with ID {depto_id} has been deleted"}

# Ruta para listar todos los departamentos
@router.get("/", response_model=List[DeptoBase])
def list_deptos(db: Session = Depends(get_db)):
    return depto_api.list()

# Ruta para filtrar departamentos por un campo y valor
@router.get("/filter/{field}/{value}", response_model=List[DeptoBase])
def filter_deptos(field: str, value: Any, db: Session = Depends(get_db)):
    return depto_api.filter(field, value)