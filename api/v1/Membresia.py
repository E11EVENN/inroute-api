from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import Any

from config import SessionLocal
from models.DataModel import Membresia
from models.Membresia import MembresiaBase
from abstract.AbstractAPI import AbstractAPI

# Crear un router para la API de Membresia
router = APIRouter(prefix="/v1/membresia", tags=["Membresia"])

# Crear una instancia de AbstractAPI para Membresia
membresia_api = AbstractAPI(Membresia, SessionLocal())

# Dependencia para obtener la sesión de base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Ruta para crear una nueva membresia
@router.post("/", response_model=MembresiaBase)
def create_membresia(membresia: MembresiaBase, db: Session = Depends(get_db)):
    return membresia_api.create(membresia, db)

# Ruta para obtener una membresia por ID
@router.get("/{membresia_id}", response_model=MembresiaBase)
def get_membresia(membresia_id: str, db: Session = Depends(get_db)):
    return membresia_api.get(membresia_id, db)

# Ruta para actualizar una membresia existente
@router.put("/{membresia_id}", response_model=MembresiaBase)
def update_membresia(membresia_id: str, membresia: MembresiaBase, db: Session = Depends(get_db)):
    return membresia_api.update(membresia_id, membresia, db)

# Ruta para eliminar una membresia por ID
@router.delete("/{membresia_id}", response_model=dict)
def delete_membresia(membresia_id: str, db: Session = Depends(get_db)):
    membresia_api.delete(membresia_id, db)
    return {"message": f"Membresia with ID {membresia_id} has been deleted"}

# Ruta para listar todas las membresias
@router.get("/", response_model=list[MembresiaBase])
def list_membresias(db: Session = Depends(get_db)):
    return membresia_api.list()

# Ruta para filtrar membresias por un campo y valor
@router.get("/filter/{field}/{value}", response_model=list[MembresiaBase])
def filter_membresias(field: str, value: Any, db: Session = Depends(get_db)):
    return membresia_api.filter(field, value, db)