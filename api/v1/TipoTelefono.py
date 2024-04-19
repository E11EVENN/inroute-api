from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from config import SessionLocal
from models.DataModel import TipoTelefono
from models.TipoTelefono import TipoTelefonoBase
from abstract.AbstractAPI import AbstractAPI

# Crear un enrutador (router) para los endpoints de la API
router = APIRouter(prefix="/v1/tipo_telefono", tags=["TipoTelefono"])

# Crear una instancia de AbstractAPI para TipoTelefono
tipo_telefono_api = AbstractAPI(TipoTelefono, SessionLocal)

# Dependencia para obtener la sesión de base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Ruta para crear un nuevo tipo de teléfono
@router.post("/", response_model=TipoTelefonoBase)
def create_tipo_telefono(tipo_telefono: TipoTelefonoBase, db: Session = Depends(get_db)):
    return tipo_telefono_api.create(tipo_telefono, db)

# Ruta para obtener un tipo de teléfono por ID
@router.get("/{id}", response_model=TipoTelefonoBase)
def get_tipo_telefono(id: str, db: Session = Depends(get_db)):
    return tipo_telefono_api.get(id, db)

# Ruta para actualizar un tipo de teléfono existente
@router.put("/{id}", response_model=TipoTelefonoBase)
def update_tipo_telefono(id: str, tipo_telefono: TipoTelefonoBase, db: Session = Depends(get_db)):
    return tipo_telefono_api.update(id, tipo_telefono, db)

# Ruta para eliminar un tipo de teléfono por ID
@router.delete("/{id}", response_model=dict)
def delete_tipo_telefono(id: str, db: Session = Depends(get_db)):
    tipo_telefono_api.delete(id, db)
    return {"message": f"TipoTelefono with ID {id} has been deleted"}

# Ruta para listar todos los tipos de teléfono
@router.get("/", response_model=list[TipoTelefonoBase])
def list_tipo_telefonos(db: Session = Depends(get_db)):
    return tipo_telefono_api.list()

# Ruta para filtrar tipos de teléfono por un campo y valor
@router.get("/filter/{field}/{value}", response_model=list[TipoTelefonoBase])
def filter_tipo_telefonos(field: str, value: Any, db: Session = Depends(get_db)):
    return tipo_telefono_api.filter(field, value, db)