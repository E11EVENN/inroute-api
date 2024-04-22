from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import Any, List

from models.DataModel import MonedaPaises
from models.MonedaPaises import MonedaPaisesBase
from config import SessionLocal
from abstract.AbstractAPI import AbstractAPI

# Crear un router para la API de MonedaPaises
router = APIRouter(prefix="/v1/moneda_paises", tags=["MonedaPaises"])

# Crear una instancia de AbstractAPI para MonedaPaises
moneda_paises_api = AbstractAPI(MonedaPaises, SessionLocal())

# Dependencia para obtener la sesión de base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Ruta para crear una nueva relación entre moneda y país
@router.post("/", response_model=MonedaPaisesBase)
def create_moneda_paises(moneda_paises: MonedaPaisesBase, db: Session = Depends(get_db)):
    return moneda_paises_api.create(moneda_paises)

# Ruta para obtener una relación entre moneda y país por IDs
@router.get("/{pais_id}/{moneda_id}", response_model=MonedaPaisesBase)
def get_moneda_paises(pais_id: str, moneda_id: str, db: Session = Depends(get_db)):
    return moneda_paises_api.get((pais_id, moneda_id))

# Ruta para actualizar una relación entre moneda y país existente
@router.put("/{pais_id}/{moneda_id}", response_model=MonedaPaisesBase)
def update_moneda_paises(pais_id: str, moneda_id: str, moneda_paises: MonedaPaisesBase, db: Session = Depends(get_db)):
    return moneda_paises_api.update((pais_id, moneda_id), moneda_paises)

# Ruta para eliminar una relación entre moneda y país por IDs
@router.delete("/{pais_id}/{moneda_id}", response_model=dict)
def delete_moneda_paises(pais_id: str, moneda_id: str, db: Session = Depends(get_db)):
    moneda_paises_api.delete((pais_id, moneda_id))
    return {"message": f"Relationship between country {pais_id} and currency {moneda_id} has been deleted"}

# Ruta para listar todas las relaciones entre moneda y país
@router.get("/", response_model=List[MonedaPaisesBase])
def list_moneda_paises(db: Session = Depends(get_db)):
    return moneda_paises_api.list()

# Ruta para filtrar relaciones entre moneda y país por un campo y valor
@router.get("/filter/{field}/{value}", response_model=List[MonedaPaisesBase])
def filter_moneda_paises(field: str, value: Any, db: Session = Depends(get_db)):
    return moneda_paises_api.filter(field, value)