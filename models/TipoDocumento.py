from pydantic import BaseModel

class TipoDocumentoBase(BaseModel):
    id: str
    nombre: str

    class Config:
        from_attributes = True