from sqlalchemy import Column, String, Numeric, Integer, DECIMAL, DateTime, Date, Time, TIMESTAMP, ForeignKey, text, Boolean
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
    ciudadanos = relationship("Persona", back_populates="nacionalidad_pais")

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
    nacidos = relationship("Persona", back_populates="lugar_nacimiento_ciudad")

    def __repr__(self):
        return f"<Ciudad(id={self.id}, nombre={self.nombre})>"

# Modelo Membresia

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

    # Relación con el membresia servicio
    membresia_servicios = relationship("MembresiaServicios", back_populates="servicio")

    # Relación con la tabla Procedimiento
    procedimientos = relationship('Procedimiento', back_populates='servicio')

    def __repr__(self):
        return f"<Servicio(id={self.id}, nombre={self.nombre})>"

class MembresiaServicios(Base):
    __tablename__ = 'membresia_servicios'
    
    id = Column(Numeric(5), primary_key=True)
    membresia_id = Column(String(3), ForeignKey('membresia.id'), nullable=False)
    servicio_id = Column(String(3), ForeignKey('servicio.id'), nullable=False)
    estado = Column(Numeric(1), default=1, nullable=True)
    fecha_registro = Column(TIMESTAMP(timezone=True), server_default=text('CURRENT_TIMESTAMP'))
    fecha_actualizacion = Column(TIMESTAMP(timezone=True), onupdate=text('CURRENT_TIMESTAMP'))
    usuario_id = Column(String(10), nullable=True)
    ip_address = Column(String(15), nullable=True)
    
    # Relación con Membresia
    membresia = relationship('Membresia', back_populates='membresia_servicios')
    
    # Relación con Servicio
    servicio = relationship('Servicio', back_populates='membresia_servicios')

    def __repr__(self):
        return f"<MembresiaServicios(id={self.id}, membresia={self.membresia}, servicio={self.servicio})>"

class Membresia(Base):
    __tablename__ = 'membresia'
    
    id = Column(String(3), primary_key=True, nullable=False)
    nombre = Column(String(20), nullable=False)
    descripcion = Column(String(100), nullable=False)
    vigente_desde = Column(Date, nullable=False)
    vigente_hasta = Column(Date, nullable=True)

    # Relación con el membresia servicio
    membresia_servicios = relationship("MembresiaServicios", back_populates="membresia")

    def __repr__(self):
        return f"<Membresia(id={self.id}, nombre={self.nombre})>"

# Extender Modelo Facturacion 

# Modelo Entrenamiento

class Proceso(Base):
    __tablename__ = 'proceso'

    id = Column(String(2), primary_key=True, nullable=False)
    nombre = Column(String(25), nullable=False)
    descripcion = Column(String(100), nullable=True)

    # Relación con la tabla Procedimiento
    procedimientos = relationship('Procedimiento', back_populates='proceso')

    def __repr__(self):
        return f"<Proceso(id={self.id}, nombre={self.nombre})>"

class Procedimiento(Base):
    __tablename__ = 'procedimiento'
    
    id = Column(String(5), primary_key=True, nullable=False)
    proceso_id = Column(String(2), ForeignKey('proceso.id'), nullable=False)
    servicio_id = Column(String(3), ForeignKey('servicio.id'), nullable=True)
    nombre = Column(String(30), nullable=False)
    descripcion = Column(String(100), nullable=True)

    # Relaciones
    proceso = relationship("Proceso", back_populates="procedimientos")
    servicio = relationship("Servicio", back_populates="procedimientos")
    entrenamientos = relationship("Entrenamiento", back_populates="procedimiento")

    def __repr__(self):
        return f"<Procedimiento(id={self.id}, nombre={self.nombre})>"

class TipoEntrenamiento(Base):
    __tablename__ = 'tipo_entrenamiento'

    id = Column(String(2), primary_key=True, comment='id')
    nombre = Column(String(25), nullable=False, comment='nombre')

    # Relaciones
    entrenamientos = relationship("Entrenamiento", back_populates="tipo_entrenamiento")

    def __repr__(self):
        return f"<TipoEntrenamiento(id={self.id}, nombre={self.nombre})>"

class TipoActividad(Base):
    __tablename__ = 'tipo_actividad'

    id = Column(String(2), primary_key=True, comment='id')
    nombre = Column(String(25), nullable=False, comment='nombre')

    # Relaciones
    entrenamiento_actividades = relationship("EntrenamientoActividad", back_populates="tipo_actividad")

    def __repr__(self):
        return f"<TipoActividad(id={self.id}, nombre={self.nombre})>"

class Entrenamiento(Base):
    __tablename__ = 'entrenamiento'
    
    id = Column(String(5), primary_key=True, comment='id', nullable=False)
    nombre = Column(String(25), nullable=False, comment='nombre')
    procedimiento_id = Column(String(5), ForeignKey('procedimiento.id'), nullable=False, comment='procedimiento_id')
    tipo_entrenamiento_id = Column(String(2), ForeignKey('tipo_entrenamiento.id'), nullable=False, comment='tipo_entrenamiento_id')
    descripcion = Column(String(100), comment='descripcion')
    url_video = Column(String(200), comment='url_video')
    estado = Column(Numeric(1), default=1, comment='estado')

    # Relaciones
    procedimiento = relationship("Procedimiento", back_populates="entrenamientos")
    tipo_entrenamiento = relationship("TipoEntrenamiento", back_populates="entrenamientos")
    entrenamiento_actividades = relationship("EntrenamientoActividad", back_populates="entrenamiento")
    entrenamiento_planes = relationship("EntrenamientoPlan", back_populates="entrenamiento")

    def __repr__(self):
        return f"<Entrenamiento(id={self.id}, nombre={self.nombre})>"

class EntrenamientoActividad(Base):
    __tablename__ = 'entrenamiento_actividad'
    
    id = Column(Numeric(4), primary_key=True, comment='id')
    entrenamiento_id = Column(String(5), ForeignKey('entrenamiento.id'), nullable=False, comment='entrenamiento_id')
    tipo_actividad_id = Column(String(2), ForeignKey('tipo_actividad.id'), nullable=False, comment='tipo_actividad_id')
    nombre = Column(String(25), nullable=False, comment='nombre')
    descripcion = Column(String(100), comment='descripcion')
    url_video = Column(String(200), comment='url_video')
    series = Column(Numeric(10), comment='series')
    cantidad = Column(Numeric(10), comment='cantidad')
    min_descanso = Column(Time, comment='min_descanso')
    tiempo_estimado = Column(Time, comment='tiempo_estimado')
    tiempo_marca = Column(Time, comment='tiempo_marca')
    orden = Column(Numeric(2), comment='orden')
    ubicacion = Column(Numeric(1), default=1, comment='ubicacion')
    estado = Column(Numeric(1), default=1, comment='estado')

    # Relaciones
    entrenamiento = relationship("Entrenamiento", back_populates="entrenamiento_actividades")
    tipo_actividad = relationship("TipoActividad", back_populates="entrenamiento_actividades")
    entrenamiento_seguimientos = relationship("EntrenamientoSeguimiento", back_populates="entrenamiento_actividad")

    def __repr__(self):
        return f"<EntrenamientoActividad(id={self.id}, nombre={self.nombre})>"

class EntrenamientoPlan(Base):
    __tablename__ = 'entrenamiento_plan'
    
    id = Column(Numeric(15), primary_key=True, comment='id')
    entrenamiento_id = Column(String(5), ForeignKey('entrenamiento.id'), nullable=False, comment='entrenamiento_id')
    entrenador_id = Column(Numeric(10), ForeignKey('persona.id'), nullable=False, comment='entrenador_id')
    atleta_id = Column(Numeric(10), ForeignKey('persona.id'), nullable=False, comment='atleta_id')
    fecha_registro = Column(TIMESTAMP(timezone=True), server_default=text('CURRENT_TIMESTAMP'))
    fecha_actualizacion = Column(TIMESTAMP(timezone=True), onupdate=text('CURRENT_TIMESTAMP'))
    estado = Column(Numeric(1), default=1, comment='estado')
    usuario_id = Column(String(10), comment='usuario_id')
    ip_address = Column(String(15), comment='ip_address')

    # Relaciones
    entrenamiento = relationship("Entrenamiento", back_populates="entrenamiento_planes")
    entrenamiento_seguimientos = relationship("EntrenamientoSeguimiento", back_populates="entrenamiento_plan")
    entrenador = relationship("Persona", back_populates="entrenador_entrenamiento_planes", foreign_keys=[entrenador_id])
    atleta = relationship("Persona", back_populates="atleta_entrenamiento_planes", foreign_keys=[atleta_id])

    def __repr__(self):
        return f"<EntrenamientoPlan(id={self.id}, entrenamiento={self.entrenamiento})>"

class EntrenamientoSeguimiento(Base):
    __tablename__ = 'entrenamiento_seguimiento'

    id = Column(Numeric(20), primary_key=True, comment='id')
    fecha_registro = Column(TIMESTAMP(timezone=True), server_default=text('CURRENT_TIMESTAMP'))
    entrenamiento_plan_id = Column(Numeric(15), ForeignKey('entrenamiento_plan.id'), nullable=False, comment='entrenamiento_plan_id')
    entrenamiento_actividad_id = Column(Numeric(4), ForeignKey('entrenamiento_actividad.id'), nullable=False, comment='entrenamiento_actividad_id')
    latitud = Column(DECIMAL, comment='latitud')
    longitud = Column(DECIMAL, comment='longitud')
    respuesta = Column(String(100), comment='respuesta')
    usuario_id = Column(String(10), comment='usuario_id')
    ip_address = Column(String(15), comment='ip_address')

    # Relaciones
    entrenamiento_plan = relationship("EntrenamientoPlan", back_populates="entrenamiento_seguimientos")
    entrenamiento_actividad = relationship("EntrenamientoActividad", back_populates="entrenamiento_seguimientos")

    def __repr__(self):
        return f"<EntrenamientoSeguimiento(id={self.id}, entrenamiento_actividad={self.entrenamiento_actividad})>"

# Modelo Persona

class TipoDocumento(Base):
    __tablename__ = 'tipo_documento'

    id = Column(String(2), primary_key=True, nullable=False)
    nombre = Column(String(50), nullable=False)

    # Relaciones
    personas = relationship("Persona", back_populates="tipo_documento")

    def __repr__(self):
        return f"<TipoDocumento(id={self.id}, nombre={self.nombre})>"


class RolPersona(Base):
    __tablename__ = 'rol_persona'

    id = Column(String(3), primary_key=True, nullable=False)
    nombre = Column(String(25), nullable=False)

    # Relaciones con tablas relacionadas
    personas = relationship("PersonaRoles", back_populates="rol_persona")

    def __repr__(self):
        return f"<RolPersona(id={self.id}, nombre={self.nombre})>"

class TipoEmail(Base):
    __tablename__ = 'tipo_email'

    id = Column(String(3), primary_key=True, nullable=False)
    nombre = Column(String(25), nullable=False)

    # Relaciones con tablas relacionadas
    emails = relationship("PersonaEmails", back_populates="tipo_email")

    def __repr__(self):
        return f"<TipoEmail(id={self.id}, nombre={self.nombre})>"

class TipoTelefono(Base):
    __tablename__ = 'tipo_telefono'

    id = Column(String(3), primary_key=True, nullable=False)
    nombre = Column(String(25), nullable=False)

    # Relaciones con tablas relacionadas
    telefonos = relationship("PersonaTelefonos", back_populates="tipo_telefono")

    def __repr__(self):
        return f"<TipoTelefono(id={self.id}, nombre={self.nombre})>"

class Persona(Base):
    __tablename__ = 'persona'
    id = Column(Numeric(10), primary_key=True)
    nombre = Column(String(20), nullable=False)
    nombre_sec = Column(String(20), nullable=True)
    apellido = Column(String(40), nullable=False)
    apellido_sec = Column(String(40), nullable=True)
    tipo_documento_id = Column(String(2), ForeignKey('tipo_documento.id'), nullable=False)
    documento = Column(String(20), nullable=False)
    fecha_nacimiento = Column(Date, nullable=False)
    nacionalidad_pais_id = Column(String(3), ForeignKey('pais.id'), nullable=False)
    lugar_nacimiento_ciudad_id = Column(String(3), ForeignKey('ciudad.id'), nullable=False)
    estado = Column(Numeric(1), default=1, nullable=True)
    fecha_registro = Column(TIMESTAMP(timezone=True), server_default=text('CURRENT_TIMESTAMP'))
    fecha_actualizacion = Column(TIMESTAMP(timezone=True), onupdate=text('CURRENT_TIMESTAMP'))
    usuario_id = Column(String(10), nullable=True)
    ip_address = Column(String(15), nullable=True)

    # Relaciones con tablas relacionadas
    tipo_documento = relationship("TipoDocumento", back_populates="personas")
    nacionalidad_pais = relationship("Pais", back_populates="ciudadanos")
    lugar_nacimiento_ciudad = relationship("Ciudad", back_populates="nacidos")
    telefonos = relationship("PersonaTelefonos", back_populates="persona")
    emails = relationship("PersonaEmails", back_populates="persona")
    roles = relationship("PersonaRoles", back_populates="persona")
    entrenador_entrenamiento_planes = relationship("EntrenamientoPlan", back_populates="entrenador", foreign_keys=[EntrenamientoPlan.entrenador_id])
    atleta_entrenamiento_planes = relationship("EntrenamientoPlan", back_populates="atleta", foreign_keys=[EntrenamientoPlan.atleta_id])

    def __repr__(self):
        return f"<Persona(id={self.id}, nombre={self.nombre}, apellido={self.apellido})>"

class PersonaTelefonos(Base):
    __tablename__ = 'persona_telefonos'
    id = Column(Numeric(5), primary_key=True)
    tipo_telefono_id = Column(String(3), ForeignKey('tipo_telefono.id'), nullable=False)
    persona_id = Column(Numeric(10), ForeignKey('persona.id'), nullable=False)
    numero = Column(Numeric(15), nullable=False)
    whatsapp = Column(Boolean, default=False, nullable=True)
    estado = Column(Numeric(1), default=1, nullable=True)
    fecha_registro = Column(TIMESTAMP(timezone=True), server_default=text('CURRENT_TIMESTAMP'))
    fecha_actualizacion = Column(TIMESTAMP(timezone=True), onupdate=text('CURRENT_TIMESTAMP'))
    usuario_id = Column(String(10), nullable=True)
    ip_address = Column(String(15), nullable=True)

    # Relaciones con tablas relacionadas
    persona = relationship("Persona", back_populates="telefonos")
    tipo_telefono = relationship("TipoTelefono", back_populates="telefonos")
    roles = relationship("PersonaRoles", back_populates="persona_telefonos")

    def __repr__(self):
        return f"<PersonaTelefonos(id={self.id}, persona_id={self.persona_id}, numero={self.numero})>"

class PersonaEmails(Base):
    __tablename__ = 'persona_emails'
    id = Column(Numeric(10), primary_key=True)
    persona_id = Column(Numeric(10), ForeignKey('persona.id'), nullable=False)
    tipo_email_id = Column(String(3), ForeignKey('tipo_email.id'), nullable=False)
    email = Column(String(50), nullable=False)
    estado = Column(Numeric(1), default=1, nullable=True)
    fecha_registro = Column(TIMESTAMP(timezone=True), server_default=text('CURRENT_TIMESTAMP'))
    fecha_actualizacion = Column(TIMESTAMP(timezone=True), onupdate=text('CURRENT_TIMESTAMP'))
    usuario_id = Column(String(10), nullable=True)
    ip_address = Column(String(15), nullable=True)

    # Relaciones con tablas relacionadas
    persona = relationship("Persona", back_populates="emails")
    tipo_email = relationship("TipoEmail", back_populates="emails")

    def __repr__(self):
        return f"<PersonaEmails(id={self.id}, persona_id={self.persona_id}, email={self.email})>"

class PersonaRoles(Base):
    __tablename__ = 'persona_roles'
    persona_id = Column(Numeric(10), ForeignKey('persona.id'), primary_key=True)
    rol_persona_id = Column(String(3), ForeignKey('rol_persona.id'), primary_key=True)
    persona_telefonos_id = Column(Numeric(5), ForeignKey('persona_telefonos.id'), nullable=True)
    estado = Column(Numeric(1), default=1, nullable=True)
    fecha_registro = Column(TIMESTAMP(timezone=True), server_default=text('CURRENT_TIMESTAMP'))
    fecha_actualizacion = Column(TIMESTAMP(timezone=True), onupdate=text('CURRENT_TIMESTAMP'))
    usuario_id = Column(String(10), nullable=True)
    ip_address = Column(String(15), nullable=True)

    # Relaciones con tablas relacionadas
    persona = relationship("Persona", back_populates="roles")
    rol_persona = relationship("RolPersona", back_populates="personas")
    persona_telefonos = relationship("PersonaTelefonos", back_populates="roles", uselist=False)

    def __repr__(self):
        return f"<PersonaRoles(persona_id={self.persona_id}, rol_persona_id={self.rol_persona_id})>"