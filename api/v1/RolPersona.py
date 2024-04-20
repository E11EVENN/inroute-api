from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from config import SessionLocal
from models.DataModel import RolPersona
from models.RolPersona import RolPersonaBase
from abstract.AbstractAPI import AbstractAPI
from typing import Any

# Crear un enrutador (router) para los endpoints de la API
router = APIRouter(prefix="/v1/rol_persona", tags=["RolPersona"])

# Crear una instancia de AbstractAPI para RolPersona
rol_persona_api = AbstractAPI(RolPersona, SessionLocal())

# Dependencia para obtener la sesión de base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Ruta para crear un nuevo rol de persona
@router.post("/", response_model=RolPersonaBase)
def create_rol_persona(rol_persona: RolPersonaBase, db: Session = Depends(get_db)):
    return rol_persona_api.create(rol_persona, db)

# Ruta para obtener un rol de persona por ID
@router.get("/{id}", response_model=RolPersonaBase)
def get_rol_persona(id: str, db: Session = Depends(get_db)):
    return rol_persona_api.get(id, db)

# Ruta para actualizar un rol de persona existente
@router.put("/{id}", response_model=RolPersonaBase)
def update_rol_persona(id: str, rol_persona: RolPersonaBase, db: Session = Depends(get_db)):
    return rol_persona_api.update(id, rol_persona, db)

# Ruta para eliminar un rol de persona por ID
@router.delete("/{id}", response_model=dict)
def delete_rol_persona(id: str, db: Session = Depends(get_db)):
    rol_persona_api.delete(id, db)
    return {"message": f"RolPersona with ID {id} has been deleted"}

# Ruta para listar todos los roles de persona
@router.get("/", response_model=list[RolPersonaBase])
def list_rol_personas(db: Session = Depends(get_db)):
    return rol_persona_api.list()

# Ruta para filtrar roles de persona por un campo y valor
@router.get("/filter/{field}/{value}", response_model=list[RolPersonaBase])
def filter_rol_personas(field: str, value: Any, db: Session = Depends(get_db)):
    return rol_persona_api.filter(field, value, db)