from sqlalchemy import Column, String, Numeric, Integer, TIMESTAMP, ForeignKey, text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class Pais(Base):
    __tablename__ = "pais"

    id = Column(String(3), primary_key=True, nullable=False)
    nombre = Column(String(40), nullable=False)
    indicativo_telefonico = Column(Numeric(4), nullable=False)
    estado = Column(Numeric(1), default=1)
    fecha_registro = Column(TIMESTAMP(timezone=True), server_default=text('CURRENT_TIMESTAMP'))
    fecha_actualizacion = Column(TIMESTAMP(timezone=True), onupdate=text('CURRENT_TIMESTAMP'))
    usuario_id = Column(String(10), nullable=True)
    ip_address = Column(String(15), nullable=True)

    # Relación con la tabla Depto
    deptos = relationship('Depto', back_populates='pais')

    def __repr__(self):
        return f"<Pais(id={self.id}, nombre={self.nombre})>"

class Depto(Base):
    __tablename__ = "depto"

    id = Column(String(2), primary_key=True, nullable=False)
    nombre = Column(String(30), nullable=False)
    pais_id = Column(String(3), ForeignKey("pais.id"), nullable=False)
    estado = Column(Integer, default=1)
    fecha_registro = Column(TIMESTAMP(timezone=True), server_default=text('CURRENT_TIMESTAMP'))
    fecha_actualizacion = Column(TIMESTAMP(timezone=True), onupdate=text('CURRENT_TIMESTAMP'))
    usuario_id = Column(String(10), nullable=True)
    ip_address = Column(String(15), nullable=True)

    pais = relationship('Pais', back_populates='deptos')
    ciudades = relationship('Ciudad', back_populates='depto')

    def __repr__(self):
        return f"<Depto(id={self.id}, nombre={self.nombre})>"

class Ciudad(Base):
    __tablename__ = 'ciudad'

    id = Column(String(3), primary_key=True)
    nombre = Column(String(30), nullable=False)
    depto_id = Column(String(2), ForeignKey('depto.id'), nullable=False)
    estado = Column(Numeric(1), default=1, nullable=True)
    fecha_registro = Column(TIMESTAMP(timezone=True), server_default=text('CURRENT_TIMESTAMP'))
    fecha_actualizacion = Column(TIMESTAMP(timezone=True), onupdate=text('CURRENT_TIMESTAMP'))
    usuario_id = Column(String(10), nullable=True)
    ip_address = Column(String(15), nullable=True)

    # Relación con Depto
    depto = relationship("Depto", back_populates="ciudades")

    def __repr__(self):
        return f"<Ciudad(id={self.id}, nombre={self.nombre})>"

class TipoServicio(Base):
    __tablename__ = 'tipo_servicio'

    id = Column(String(2), primary_key=True, nullable=False)
    nombre = Column(String(25), nullable=False)

    # Relación con Servicio
    servicios = relationship('Servicio', back_populates='tipo_servicio')

    def __repr__(self):
        return f"<TipoServicio(id={self.id}, nombre={self.nombre})>"

class Servicio(Base):
    __tablename__ = 'servicio'

    id = Column(String(3), primary_key=True, nullable=False)
    nombre = Column(String(30), nullable=False)
    tipo_servicio_id = Column(String(2), ForeignKey('tipo_servicio.id'), nullable=True)

    # Relación con el tipo de servicio
    tipo_servicio = relationship("TipoServicio", back_populates="servicios")

    def __repr__(self):
        return f"<Servicio(id={self.id}, nombre={self.nombre})>"