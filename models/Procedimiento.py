from pydantic import BaseModel

class ProcedimientoBase(BaseModel):
    id: str
    proceso_id: str
    servicio_id: str | None = None
    nombre: str
    descripcion: str | None = None

    class Config:
        from_attributes = True