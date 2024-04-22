from pydantic import BaseModel

class MonedaPaisesBase(BaseModel):
    pais_id: str
    moneda_id: str
    corriente: int = 1
    estado: int = 1

    class Config:
        from_attributes = True