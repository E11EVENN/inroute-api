from pydantic import BaseModel

class TipoServicioBase(BaseModel):
    id: str
    nombre: str

    class Config:
        from_attributes = True