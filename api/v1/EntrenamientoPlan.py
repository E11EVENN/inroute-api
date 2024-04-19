from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import Any

from config import SessionLocal
from models.DataModel import EntrenamientoPlan
from models.EntrenamientoPlan import EntrenamientoPlanBase
from abstract.AbstractAPI import AbstractAPI

# Crear un router para la API de EntrenamientoPlan
router = APIRouter(prefix="/v1/entrenamiento_plan", tags=["EntrenamientoPlan"])

# Crear una instancia de AbstractAPI para EntrenamientoPlan
entrenamiento_plan_api = AbstractAPI(EntrenamientoPlan, SessionLocal())

# Dependencia para obtener la sesión de base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Ruta para crear un nuevo plan de entrenamiento
@router.post("/", response_model=EntrenamientoPlanBase)
def create_entrenamiento_plan(entrenamiento_plan: EntrenamientoPlanBase, db: Session = Depends(get_db)):
    return entrenamiento_plan_api.create(entrenamiento_plan, db)

# Ruta para obtener un plan de entrenamiento por ID
@router.get("/{entrenamiento_plan_id}", response_model=EntrenamientoPlanBase)
def get_entrenamiento_plan(entrenamiento_plan_id: int, db: Session = Depends(get_db)):
    return entrenamiento_plan_api.get(entrenamiento_plan_id, db)

# Ruta para actualizar un plan de entrenamiento existente
@router.put("/{entrenamiento_plan_id}", response_model=EntrenamientoPlanBase)
def update_entrenamiento_plan(entrenamiento_plan_id: int, entrenamiento_plan: EntrenamientoPlanBase, db: Session = Depends(get_db)):
    return entrenamiento_plan_api.update(entrenamiento_plan_id, entrenamiento_plan, db)

# Ruta para eliminar un plan de entrenamiento por ID
@router.delete("/{entrenamiento_plan_id}", response_model=dict)
def delete_entrenamiento_plan(entrenamiento_plan_id: int, db: Session = Depends(get_db)):
    entrenamiento_plan_api.delete(entrenamiento_plan_id, db)
    return {"message": f"EntrenamientoPlan with ID {entrenamiento_plan_id} has been deleted"}

# Ruta para listar todos los planes de entrenamiento
@router.get("/", response_model=list[EntrenamientoPlanBase])
def list_entrenamiento_planes(db: Session = Depends(get_db)):
    return entrenamiento_plan_api.list()

# Ruta para filtrar planes de entrenamiento por un campo y valor
@router.get("/filter/{field}/{value}", response_model=list[EntrenamientoPlanBase])
def filter_entrenamiento_planes(field: str, value: Any, db: Session = Depends(get_db)):
    return entrenamiento_plan_api.filter(field, value, db)