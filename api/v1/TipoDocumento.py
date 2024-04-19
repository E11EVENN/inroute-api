from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from config import SessionLocal
from models.DataModel import TipoDocumento
from models.TipoDocumento import TipoDocumentoBase
from abstract.AbstractAPI import AbstractAPI

# Crear un enrutador (router) para los endpoints de la API
router = APIRouter(prefix="/v1/tipo_documento", tags=["TipoDocumento"])

# Crear una instancia de AbstractAPI para TipoDocumento
tipo_documento_api = AbstractAPI(TipoDocumento, SessionLocal)

# Dependencia para obtener la sesión de base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Ruta para crear un nuevo tipo de documento
@router.post("/", response_model=TipoDocumentoBase)
def create_tipo_documento(tipo_documento: TipoDocumentoBase, db: Session = Depends(get_db)):
    return tipo_documento_api.create(tipo_documento, db)

# Ruta para obtener un tipo de documento por ID
@router.get("/{id}", response_model=TipoDocumentoBase)
def get_tipo_documento(id: str, db: Session = Depends(get_db)):
    return tipo_documento_api.get(id, db)

# Ruta para actualizar un tipo de documento existente
@router.put("/{id}", response_model=TipoDocumentoBase)
def update_tipo_documento(id: str, tipo_documento: TipoDocumentoBase, db: Session = Depends(get_db)):
    return tipo_documento_api.update(id, tipo_documento, db)

# Ruta para eliminar un tipo de documento por ID
@router.delete("/{id}", response_model=dict)
def delete_tipo_documento(id: str, db: Session = Depends(get_db)):
    tipo_documento_api.delete(id, db)
    return {"message": f"TipoDocumento with ID {id} has been deleted"}

# Ruta para listar todos los tipos de documentos
@router.get("/", response_model=list[TipoDocumentoBase])
def list_tipo_documentos(db: Session = Depends(get_db)):
    return tipo_documento_api.list()

# Ruta para filtrar tipos de documentos por un campo y valor
@router.get("/filter/{field}/{value}", response_model=list[TipoDocumentoBase])
def filter_tipo_documentos(field: str, value: Any, db: Session = Depends(get_db)):
    return tipo_documento_api.filter(field, value, db)