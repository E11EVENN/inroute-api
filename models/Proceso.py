from pydantic import BaseModel

class ProcesoBase(BaseModel):
    id: str
    nombre: str
    descripcion: str | None = None

    class Config:
        from_attributes = True