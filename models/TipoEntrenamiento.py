from pydantic import BaseModel

class TipoEntrenamientoBase(BaseModel):
    id: str
    nombre: str

    class Config:
        from_attributes = True