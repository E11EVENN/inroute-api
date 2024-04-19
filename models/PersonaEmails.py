from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class PersonaEmailsBase(BaseModel):
    id: Optional[int]
    persona_id: int
    tipo_email_id: str
    email: str
    estado: Optional[int] = 1
    fecha_registro: Optional[datetime]
    fecha_actualizacion: Optional[datetime]
    usuario_id: Optional[str]
    ip_address: Optional[str]

    class Config:
        from_attributes = True