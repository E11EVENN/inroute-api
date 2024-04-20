# inroute-api
InRoute's API

## Modo Desarrollo
Para aislar entorno desarrollo utilizar lo siguiente:

1. Iniciar ambiente: python3 -m venv env
2. Cargar ambiente: source env/bin/activate
3. Desactivar ambiente: deactivate

Para cada ambiente de ejecucion se debe usar la variable INROUTE con los valores: DEV, QA, PRO

Lanzamiento de Aplicacion: INROUTE=DEV uvicorn app:app --reload

Ingresar a la aplicacion: http://localhost:8000/

## Modo Implementacion

### Construccion de la imagen

Construir la imagen de docker asi:

docker build --build-arg GIT_COMMIT=$(git rev-parse HEAD) --build-arg GIT_AUTHOR=$(git log -1 --pretty=format:'%an') --build-arg BUILD_DATE=$(date -u +'%Y-%m-%dT%H:%M:%SZ') -t inroute-api .

### Ejecucion del contenedor

Correr el contenedor asi: 

docker run --env INROUTE=DEV inroute-api

Ingresar a la aplicacion: http://localhost:8000/