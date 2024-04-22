from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class PaisBase(BaseModel):
    id: str
    nombre: str
    indicativo_telefonico: int
    continente_id: str
    estado: Optional[int] = 1
    fecha_registro: Optional[datetime]
    fecha_actualizacion: Optional[datetime]
    usuario_id: Optional[str]
    ip_address: Optional[str]

    class Config:
        from_attributes = True