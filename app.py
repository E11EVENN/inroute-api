from fastapi import FastAPI
from api.v1.Pais import router as pais_router
from api.v1.Depto import router as depto_router
from api.v1.Ciudad import router as ciudad_router
from api.v1.TipoServicio import router as tipoServicio_router
from api.v1.Servicio import router as servicio_router
from api.v1.MembresiaServicio import router as membresia_servicio_router
from api.v1.Membresia import router as membresia_router
from api.v1.Proceso import router as proceso_router
from api.v1.Procedimiento import router as procedimiento_router
from api.v1.TipoEntrenamiento import router as tipo_entrenamiento_router
from api.v1.TipoActividad import router as tipo_actividad_router
from api.v1.Entrenamiento import router as entrenamiento_router
from api.v1.EntrenamientoActividad import router as entrenamiento_actividad_router
from api.v1.EntrenamientoPlan import router as entrenamiento_plan_router
from api.v1.EntrenamientoSeguimiento import router as entrenamiento_seguimiento_router
from api.v1.TipoDocumento import router as tipo_documento_router
from api.v1.RolPersona import router as rol_persona_router
from api.v1.TipoEmail import router as tipo_email_router
from api.v1.TipoTelefono import router as tipo_telefono_router
from api.v1.Persona import router as persona_router
from api.v1.PersonaTelefonos import router as persona_telefonos_router
from api.v1.PersonaEmails import router as persona_emails_router
from api.v1.PersonaRoles import router as persona_roles_router

app = FastAPI(
    title="Api InRoute",
    description="Api DAO para el Proyecto InRoute",
    version="1.0",
    docs_url="/docs",  # URL para acceder a Swagger UI
    redoc_url="/redoc",  # URL para acceder a Redoc
)

@app.get("/", include_in_schema=False)
def read_root():
    return {
        "message": "¡Bienvenido a la API de InRoute!",
        "description": "Esta es la API para gestionar los datos de la aplicación InRoute.",
        "routes": "Explora las rutas en /docs para más información sobre los endpoints de la API."
    }

# APIs Geografia
app.include_router(pais_router)
app.include_router(depto_router)
app.include_router(ciudad_router)

# APIs Membresia
app.include_router(tipoServicio_router)
app.include_router(servicio_router)
app.include_router(membresia_servicio_router)
app.include_router(membresia_router)

# APIs Entrenamiento
app.include_router(proceso_router)
app.include_router(procedimiento_router)
app.include_router(tipo_entrenamiento_router)
app.include_router(tipo_actividad_router)
app.include_router(entrenamiento_router)
app.include_router(entrenamiento_actividad_router)
app.include_router(entrenamiento_plan_router)
app.include_router(entrenamiento_seguimiento_router)

# APIs Persona
app.include_router(tipo_documento_router)
app.include_router(rol_persona_router)
app.include_router(tipo_email_router)
app.include_router(tipo_telefono_router)
app.include_router(persona_router)
app.include_router(persona_telefonos_router)
app.include_router(persona_emails_router)
app.include_router(persona_roles_router)

# Inicia el servidor con Uvicorn
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)