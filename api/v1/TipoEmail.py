from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from config import SessionLocal
from models.DataModel import TipoEmail
from models.TipoEmail import TipoEmailBase
from abstract.AbstractAPI import AbstractAPI
from typing import Any

# Crear un enrutador (router) para los endpoints de la API
router = APIRouter(prefix="/v1/tipo_email", tags=["TipoEmail"])

# Crear una instancia de AbstractAPI para TipoEmail
tipo_email_api = AbstractAPI(TipoEmail, SessionLocal())

# Dependencia para obtener la sesión de base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Ruta para crear un nuevo tipo de email
@router.post("/", response_model=TipoEmailBase)
def create_tipo_email(tipo_email: TipoEmailBase, db: Session = Depends(get_db)):
    return tipo_email_api.create(tipo_email, db)

# Ruta para obtener un tipo de email por ID
@router.get("/{id}", response_model=TipoEmailBase)
def get_tipo_email(id: str, db: Session = Depends(get_db)):
    return tipo_email_api.get(id, db)

# Ruta para actualizar un tipo de email existente
@router.put("/{id}", response_model=TipoEmailBase)
def update_tipo_email(id: str, tipo_email: TipoEmailBase, db: Session = Depends(get_db)):
    return tipo_email_api.update(id, tipo_email, db)

# Ruta para eliminar un tipo de email por ID
@router.delete("/{id}", response_model=dict)
def delete_tipo_email(id: str, db: Session = Depends(get_db)):
    tipo_email_api.delete(id, db)
    return {"message": f"TipoEmail with ID {id} has been deleted"}

# Ruta para listar todos los tipos de email
@router.get("/", response_model=list[TipoEmailBase])
def list_tipo_emails(db: Session = Depends(get_db)):
    return tipo_email_api.list()

# Ruta para filtrar tipos de email por un campo y valor
@router.get("/filter/{field}/{value}", response_model=list[TipoEmailBase])
def filter_tipo_emails(field: str, value: Any, db: Session = Depends(get_db)):
    return tipo_email_api.filter(field, value, db)