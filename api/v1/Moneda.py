from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import Any, List

from models.DataModel import Moneda
from models.Moneda import MonedaBase
from config import SessionLocal
from abstract.AbstractAPI import AbstractAPI

# Crear un router para la API de Moneda
router = APIRouter(prefix="/v1/moneda", tags=["Moneda"])

# Crear una instancia de AbstractAPI para Moneda
moneda_api = AbstractAPI(Moneda, SessionLocal())

# Dependencia para obtener la sesión de base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Ruta para crear una nueva moneda
@router.post("/", response_model=MonedaBase)
def create_moneda(moneda: MonedaBase, db: Session = Depends(get_db)):
    return moneda_api.create(moneda)

# Ruta para obtener una moneda por ID
@router.get("/{moneda_id}", response_model=MonedaBase)
def get_moneda(moneda_id: str, db: Session = Depends(get_db)):
    return moneda_api.get(moneda_id)

# Ruta para actualizar una moneda existente
@router.put("/{moneda_id}", response_model=MonedaBase)
def update_moneda(moneda_id: str, moneda: MonedaBase, db: Session = Depends(get_db)):
    return moneda_api.update(moneda_id, moneda)

# Ruta para eliminar una moneda por ID
@router.delete("/{moneda_id}", response_model=dict)
def delete_moneda(moneda_id: str, db: Session = Depends(get_db)):
    moneda_api.delete(moneda_id)
    return {"message": f"Moneda with ID {moneda_id} has been deleted"}

# Ruta para listar todas las monedas
@router.get("/", response_model=List[MonedaBase])
def list_monedas(db: Session = Depends(get_db)):
    return moneda_api.list()

# Ruta para filtrar monedas por un campo y valor
@router.get("/filter/{field}/{value}", response_model=List[MonedaBase])
def filter_monedas(field: str, value: Any, db: Session = Depends(get_db)):
    return moneda_api.filter(field, value)