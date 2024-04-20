from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from config import SessionLocal
from models.DataModel import PersonaTelefonos
from models.PersonaTelefonos import PersonaTelefonosBase
from abstract.AbstractAPI import AbstractAPI
from typing import Any

# Crear un enrutador (router) para los endpoints de la API
router = APIRouter(prefix="/v1/persona_telefonos", tags=["PersonaTelefonos"])

# Crear una instancia de AbstractAPI para PersonaTelefonos
persona_telefonos_api = AbstractAPI(PersonaTelefonos, SessionLocal())

# Dependencia para obtener la sesión de base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Ruta para crear un nuevo registro en persona_telefonos
@router.post("/", response_model=PersonaTelefonosBase)
def create_persona_telefonos(persona_telefonos: PersonaTelefonosBase, db: Session = Depends(get_db)):
    return persona_telefonos_api.create(persona_telefonos, db)

# Ruta para obtener un registro de persona_telefonos por ID
@router.get("/{id}", response_model=PersonaTelefonosBase)
def get_persona_telefonos(id: int, db: Session = Depends(get_db)):
    return persona_telefonos_api.get(id, db)

# Ruta para actualizar un registro de persona_telefonos existente
@router.put("/{id}", response_model=PersonaTelefonosBase)
def update_persona_telefonos(id: int, persona_telefonos: PersonaTelefonosBase, db: Session = Depends(get_db)):
    return persona_telefonos_api.update(id, persona_telefonos, db)

# Ruta para eliminar un registro de persona_telefonos por ID
@router.delete("/{id}", response_model=dict)
def delete_persona_telefonos(id: int, db: Session = Depends(get_db)):
    persona_telefonos_api.delete(id, db)
    return {"message": f"PersonaTelefonos with ID {id} has been deleted"}

# Ruta para listar todos los registros de persona_telefonos
@router.get("/", response_model=list[PersonaTelefonosBase])
def list_persona_telefonos(db: Session = Depends(get_db)):
    return persona_telefonos_api.list()

# Ruta para filtrar registros de persona_telefonos por un campo y valor
@router.get("/filter/{field}/{value}", response_model=list[PersonaTelefonosBase])
def filter_persona_telefonos(field: str, value: Any, db: Session = Depends(get_db)):
    return persona_telefonos_api.filter(field, value, db)