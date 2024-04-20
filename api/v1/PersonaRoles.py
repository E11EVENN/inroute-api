from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from config import SessionLocal
from models.DataModel import PersonaRoles
from models.PersonaRoles import PersonaRolesBase
from abstract.AbstractAPI import AbstractAPI
from typing import Any

# Crear un enrutador (router) para los endpoints de la API
router = APIRouter(prefix="/v1/persona_roles", tags=["PersonaRoles"])

# Crear una instancia de AbstractAPI para PersonaRoles
persona_roles_api = AbstractAPI(PersonaRoles, SessionLocal())

# Dependencia para obtener la sesión de base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Ruta para crear un nuevo registro en persona_roles
@router.post("/", response_model=PersonaRolesBase)
def create_persona_roles(persona_roles: PersonaRolesBase, db: Session = Depends(get_db)):
    return persona_roles_api.create(persona_roles, db)

# Ruta para obtener un registro de persona_roles por llave primaria
@router.get("/{persona_id}/{rol_persona_id}", response_model=PersonaRolesBase)
def get_persona_roles(persona_id: int, rol_persona_id: str, db: Session = Depends(get_db)):
    return persona_roles_api.get((persona_id, rol_persona_id), db)

# Ruta para actualizar un registro de persona_roles existente
@router.put("/{persona_id}/{rol_persona_id}", response_model=PersonaRolesBase)
def update_persona_roles(persona_id: int, rol_persona_id: str, persona_roles: PersonaRolesBase, db: Session = Depends(get_db)):
    return persona_roles_api.update((persona_id, rol_persona_id), persona_roles, db)

# Ruta para eliminar un registro de persona_roles por llave primaria
@router.delete("/{persona_id}/{rol_persona_id}", response_model=dict)
def delete_persona_roles(persona_id: int, rol_persona_id: str, db: Session = Depends(get_db)):
    persona_roles_api.delete((persona_id, rol_persona_id), db)
    return {"message": f"PersonaRoles with persona_id {persona_id} and rol_persona_id {rol_persona_id} has been deleted"}

# Ruta para listar todos los registros de persona_roles
@router.get("/", response_model=list[PersonaRolesBase])
def list_persona_roles(db: Session = Depends(get_db)):
    return persona_roles_api.list()

# Ruta para filtrar registros de persona_roles por un campo y valor
@router.get("/filter/{field}/{value}", response_model=list[PersonaRolesBase])
def filter_persona_roles(field: str, value: Any, db: Session = Depends(get_db)):
    return persona_roles_api.filter(field, value, db)