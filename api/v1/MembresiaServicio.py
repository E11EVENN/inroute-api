from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import Any
from config import SessionLocal
from models.DataModel import MembresiaServicios
from models.MembresiaServicio import MembresiaServiciosBase
from abstract.AbstractAPI import AbstractAPI

# Crear un router para la API de MembresiaServicios
router = APIRouter(prefix="/v1/membresia_servicios", tags=["MembresiaServicios"])

# Crear una instancia de AbstractAPI para MembresiaServicios
membresia_servicios_api = AbstractAPI(MembresiaServicios, SessionLocal())

# Dependencia para obtener la sesión de base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally: 
        db.close()

# Ruta para crear un nuevo membresia_servicios
@router.post("/", response_model=MembresiaServiciosBase)
def create_membresia_servicios(membresia_servicios: MembresiaServiciosBase, db: Session = Depends(get_db)):
    return membresia_servicios_api.create(membresia_servicios, db)

# Ruta para obtener un membresia_servicios por ID
@router.get("/{membresia_servicios_id}", response_model=MembresiaServiciosBase)
def get_membresia_servicios(membresia_servicios_id: int, db: Session = Depends(get_db)):
    return membresia_servicios_api.get(membresia_servicios_id, db)

# Ruta para actualizar un membresia_servicios existente
@router.put("/{membresia_servicios_id}", response_model=MembresiaServiciosBase)
def update_membresia_servicios(membresia_servicios_id: int, membresia_servicios: MembresiaServiciosBase, db: Session = Depends(get_db)):
    return membresia_servicios_api.update(membresia_servicios_id, membresia_servicios, db)

# Ruta para eliminar un membresia_servicios por ID
@router.delete("/{membresia_servicios_id}", response_model=dict)
def delete_membresia_servicios(membresia_servicios_id: int, db: Session = Depends(get_db)):
    membresia_servicios_api.delete(membresia_servicios_id, db)
    return {"message": f"MembresiaServicios with ID {membresia_servicios_id} has been deleted"}

# Ruta para listar todos los membresia_servicios
@router.get("/", response_model=list[MembresiaServiciosBase])
def list_membresia_servicios(db: Session = Depends(get_db)):
    return membresia_servicios_api.list()

# Ruta para filtrar membresia_servicios por un campo y valor
@router.get("/filter/{field}/{value}", response_model=list[MembresiaServiciosBase])
def filter_membresia_servicios(field: str, value: Any, db: Session = Depends(get_db)):
    return membresia_servicios_api.filter(field, value, db)
