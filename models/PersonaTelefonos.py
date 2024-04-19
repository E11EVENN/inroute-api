from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class PersonaTelefonosBase(BaseModel):
    id: Optional[int]
    tipo_telefono_id: str
    persona_id: int
    numero: int
    whatsapp: Optional[bool] = False
    estado: Optional[int] = 1
    fecha_registro: Optional[datetime]
    fecha_actualizacion: Optional[datetime]
    usuario_id: Optional[str]
    ip_address: Optional[str]

    class Config:
        from_attributes = True