# inroute-api
InRoute's API

## Modo de implementacion
Para aislar entorno desarrollo utilizar lo siguiente:

1. Iniciar ambiente: python3 -m venv env
2. Cargar ambiente: source env/bin/activate
3. Desactivar ambiente: deactivate

Para cada ambiente de ejecucion se debe usar la variable INROUTE con los valores: DEV, QA, PRO

Lanzamiento de Aplicacion: INROUTE=DEV uvicorn app:app --reload

Ingresar a la aplicacion: http://localhost:8000/