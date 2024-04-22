from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import Any, List

from models.DataModel import Continente
from models.Continente import ContinenteBase
from config import SessionLocal
from abstract.AbstractAPI import AbstractAPI

# Crear un router para la API de Continente
router = APIRouter(prefix="/v1/continente", tags=["Continente"])

# Crear una instancia de ContinenteAPI
continente_api = AbstractAPI(Continente, SessionLocal())

# Dependencia para obtener la sesión de base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Ruta para crear un nuevo continente
@router.post("/", response_model=ContinenteBase)
def create_continente(continente: ContinenteBase, db: Session = Depends(get_db)):
    return continente_api.create(continente)

# Ruta para obtener un continente por ID
@router.get("/{continente_id}", response_model=ContinenteBase)
def get_continente(continente_id: str, db: Session = Depends(get_db)):
    return continente_api.get(continente_id)

# Ruta para actualizar un continente existente
@router.put("/{continente_id}", response_model=ContinenteBase)
def update_continente(continente_id: str, continente: ContinenteBase, db: Session = Depends(get_db)):
    return continente_api.update(continente_id, continente)

# Ruta para eliminar un continente por ID
@router.delete("/{continente_id}", response_model=dict)
def delete_continente(continente_id: str, db: Session = Depends(get_db)):
    continente_api.delete(continente_id)
    return {"message": f"Continente with ID {continente_id} has been deleted"}

# Ruta para listar todos los continentes
@router.get("/", response_model=List[ContinenteBase])
def list_continentes(db: Session = Depends(get_db)):
    return continente_api.list()

# Ruta para filtrar continentes por un campo y valor
@router.get("/filter/{field}/{value}", response_model=List[ContinenteBase])
def filter_continentes(field: str, value: Any, db: Session = Depends(get_db)):
    return continente_api.filter(field, value)