from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class EntrenamientoPlanBase(BaseModel):
    id: Optional[int] = None
    entrenamiento_id: str
    entrenador_id: int
    atleta_id: int
    fecha_registro: Optional[datetime] = None
    fecha_actualizacion: Optional[datetime] = None
    estado: Optional[int] = 1
    usuario_id: Optional[str] = None
    ip_address: Optional[str] = None

    class Config:
        from_attributes = True