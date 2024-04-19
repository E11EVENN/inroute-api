from pydantic import BaseModel
from datetime import date

class MembresiaBase(BaseModel):
    id: str
    nombre: str
    descripcion: str
    vigente_desde: date
    vigente_hasta: date | None = None

    class Config:
        from_attributes = True