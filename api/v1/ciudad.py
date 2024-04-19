from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import Any, List

from models.DataModel import Ciudad
from models.Ciudad import CiudadBase
from config import SessionLocal
from abstract.AbstractAPI import AbstractAPI

# Crear un router para la API de Ciudad
router = APIRouter(prefix="/v1/ciudad", tags=["Ciudad"])

# Crear una instancia de AbstractAPI para Ciudad
ciudad_api = AbstractAPI(Ciudad, SessionLocal())

# Dependencia para obtener la sesión de base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Ruta para crear una nueva ciudad
@router.post("/", response_model=CiudadBase)
def create_ciudad(ciudad: CiudadBase, db: Session = Depends(get_db)):
    return ciudad_api.create(ciudad)

# Ruta para obtener una ciudad por ID
@router.get("/{ciudad_id}", response_model=CiudadBase)
def get_ciudad(ciudad_id: str, db: Session = Depends(get_db)):
    return ciudad_api.get(ciudad_id)

# Ruta para actualizar una ciudad existente
@router.put("/{ciudad_id}", response_model=CiudadBase)
def update_ciudad(ciudad_id: str, ciudad: CiudadBase, db: Session = Depends(get_db)):
    return ciudad_api.update(ciudad_id, ciudad)

# Ruta para eliminar una ciudad por ID
@router.delete("/{ciudad_id}", response_model=dict)
def delete_ciudad(ciudad_id: str, db: Session = Depends(get_db)):
    ciudad_api.delete(ciudad_id)
    return {"message": f"Ciudad with ID {ciudad_id} has been deleted"}

# Ruta para listar todas las ciudades
@router.get("/", response_model=List[CiudadBase])
def list_ciudades(db: Session = Depends(get_db)):
    return ciudad_api.list()

# Ruta para filtrar ciudades por un campo y valor
@router.get("/filter/{field}/{value}", response_model=List[CiudadBase])
def filter_ciudades(field: str, value: Any, db: Session = Depends(get_db)):
    return ciudad_api.filter(field, value)