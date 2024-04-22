from pydantic import BaseModel

class MonedaBase(BaseModel):
    id: str
    nombre: str
    simbolo: str

    class Config:
        from_attributes = True
