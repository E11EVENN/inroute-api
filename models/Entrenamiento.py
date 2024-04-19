from pydantic import BaseModel

class EntrenamientoBase(BaseModel):
    id: str
    nombre: str
    procedimiento_id: str
    tipo_entrenamiento_id: str
    descripcion: str = None
    url_video: str = None
    estado: int = 1

    class Config:
        from_attributes = True