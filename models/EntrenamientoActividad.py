from pydantic import BaseModel
from typing import Optional
from datetime import time

class EntrenamientoActividadBase(BaseModel):
    id: Optional[int] = None
    entrenamiento_id: str
    tipo_actividad_id: str
    nombre: str
    descripcion: Optional[str] = None
    url_video: Optional[str] = None
    series: Optional[int] = None
    cantidad: Optional[int] = None
    min_descanso: Optional[time] = None
    tiempo_estimado: Optional[time] = None
    tiempo_marca: Optional[time] = None
    orden: Optional[int] = None
    ubicacion: Optional[int] = 1
    estado: Optional[int] = 1

    class Config:
        from_attributes = True