from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from decimal import Decimal

class EntrenamientoSeguimientoBase(BaseModel):
    id: Optional[int] = None
    fecha_registro: Optional[datetime] = None
    entrenamiento_plan_id: int
    entrenamiento_actividad_id: int
    latitud: Optional[Decimal] = None
    longitud: Optional[Decimal] = None
    respuesta: Optional[str] = None
    usuario_id: Optional[str] = None
    ip_address: Optional[str] = None

    class Config:
        from_attributes = True