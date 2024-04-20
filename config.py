import json
import os
from colorama import Fore, Style

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

def log_info(message):
    """Imprime un mensaje de log con formato."""
    print(Style.NORMAL + Fore.LIGHTCYAN_EX + "INFO" + Style.RESET_ALL +":     "+ message)

def log_error(message):
    """Imprime un mensaje de error con formato."""
    print(Style.BRIGHT + Fore.RED + "ERROR" + Style.RESET_ALL +":   "+ message)

def load_settings(env: str):
    """Carga la configuración según el ambiente."""
    with open(f"settings.{env}.json", "r") as f:
        return json.load(f)

def print_env_variables():
    """Imprime todas las variables de entorno."""
    if DEBUG:
        print("INFO:     "+ Style.BRIGHT + Fore.YELLOW + "Environment Variables" + Style.RESET_ALL)
        for key, value in os.environ.items():
            print("INFO:     "+ f"{key}: {value}")

# Lee la variable de entorno INROUTE
environment = os.getenv("INROUTE", "DEV")
log_info(f"Environment: {environment}")

# Carga la configuración apropiada según el ambiente
settings = load_settings(environment.lower())

# Extrae la configuración de la base de datos
db_config = settings.get("DATABASE", {})
user = db_config.get("user")
password = db_config.get("password")
host = db_config.get("host", "localhost")
port = db_config.get("port", 5432)
db = db_config.get("db")

# Construye la URL de la base de datos
DATABASE_URL = f"postgresql://{user}:{password}@{host}:{port}/{db}"

# Crea la conexión a la base de datos
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Otras configuraciones que puedas necesitar
DEBUG = settings.get("DEBUG", False)
SECRET_KEY = settings.get("SECRET_KEY", "your_default_secret_key")

# Aquí puedes agregar otras configuraciones personalizadas que necesites
log_info(f"DEBUG: {DEBUG}")
print_env_variables()