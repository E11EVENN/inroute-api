from pydantic import BaseModel
from datetime import date
from typing import Optional

class PersonaBase(BaseModel):
    id: Optional[int]
    nombre: str
    nombre_sec: Optional[str]
    apellido: str
    apellido_sec: Optional[str]
    tipo_documento_id: str
    documento: str
    fecha_nacimiento: date
    nacionalidad_pais_id: str
    lugar_nacimiento_ciudad_id: str
    estado: Optional[int] = 1
    fecha_registro: Optional[date]
    fecha_actualizacion: Optional[date]
    usuario_id: Optional[str]
    ip_address: Optional[str]

    class Config:
        from_attributes = True