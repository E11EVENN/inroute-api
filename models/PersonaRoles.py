from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class PersonaRolesBase(BaseModel):
    persona_id: int
    rol_persona_id: str
    persona_telefonos_id: Optional[int] = None
    estado: Optional[int] = 1
    fecha_registro: Optional[datetime]
    fecha_actualizacion: Optional[datetime]
    usuario_id: Optional[str]
    ip_address: Optional[str]

    class Config:
        from_attributes = True