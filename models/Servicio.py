from pydantic import BaseModel

class ServicioBase(BaseModel):
    id: str
    nombre: str
    tipo_servicio_id: str | None = None

    class Config:
        from_attributes = True