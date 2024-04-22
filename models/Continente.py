from pydantic import BaseModel

class ContinenteBase(BaseModel):
    id: str
    nombre: str
    descripcion: str = None

    class Config:
        from_attributes = True
