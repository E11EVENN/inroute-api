from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from config import SessionLocal
from models.DataModel import PersonaEmails
from models.PersonaEmails import PersonaEmailsBase
from abstract.AbstractAPI import AbstractAPI

# Crear un enrutador (router) para los endpoints de la API
router = APIRouter(prefix="/v1/persona_emails", tags=["PersonaEmails"])

# Crear una instancia de AbstractAPI para PersonaEmails
persona_emails_api = AbstractAPI(PersonaEmails, SessionLocal)

# Dependencia para obtener la sesión de base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Ruta para crear un nuevo registro en persona_emails
@router.post("/", response_model=PersonaEmailsBase)
def create_persona_emails(persona_emails: PersonaEmailsBase, db: Session = Depends(get_db)):
    return persona_emails_api.create(persona_emails, db)

# Ruta para obtener un registro de persona_emails por ID
@router.get("/{id}", response_model=PersonaEmailsBase)
def get_persona_emails(id: int, db: Session = Depends(get_db)):
    return persona_emails_api.get(id, db)

# Ruta para actualizar un registro de persona_emails existente
@router.put("/{id}", response_model=PersonaEmailsBase)
def update_persona_emails(id: int, persona_emails: PersonaEmailsBase, db: Session = Depends(get_db)):
    return persona_emails_api.update(id, persona_emails, db)

# Ruta para eliminar un registro de persona_emails por ID
@router.delete("/{id}", response_model=dict)
def delete_persona_emails(id: int, db: Session = Depends(get_db)):
    persona_emails_api.delete(id, db)
    return {"message": f"PersonaEmails with ID {id} has been deleted"}

# Ruta para listar todos los registros de persona_emails
@router.get("/", response_model=list[PersonaEmailsBase])
def list_persona_emails(db: Session = Depends(get_db)):
    return persona_emails_api.list()

# Ruta para filtrar registros de persona_emails por un campo y valor
@router.get("/filter/{field}/{value}", response_model=list[PersonaEmailsBase])
def filter_persona_emails(field: str, value: Any, db: Session = Depends(get_db)):
    return persona_emails_api.filter(field, value, db)