from pydantic import BaseModel

class TipoTelefonoBase(BaseModel):
    id: str
    nombre: str

    class Config:
        from_attributes = True