from pydantic import BaseModel

class TipoEmailBase(BaseModel):
    id: str
    nombre: str

    class Config:
        from_attributes = True