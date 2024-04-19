from pydantic import BaseModel

class RolPersonaBase(BaseModel):
    id: str
    nombre: str

    class Config:
        from_attributes = True