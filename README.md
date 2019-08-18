# Wikidata Game

Requerimientos:

* Python 3
* pip

## Ejecución manual

Para correr uno de los servicios:

```
cd src/<directorio-servicio>/
pip install -r requirements.txt
nameko run --config config.yaml access
```

## Ejecución por Docker Compose

Para hacer build y correr contenedores dockers con los servicios:

```
docker-compose build
docker-compose up -d
```

Los contenedores son los siguientes:

| **Contenedor** | **Servicio** | **Puerto Contenedor** | **Puerto Expuesto** |   |
|----------------|--------------|-----------------------|---------------------|---|
| rabbitmq       | N/A          | 15672                 | 15673               |   |
| playerdb       | N/A          | 5432                  | 5433                |   |
| chat           | chat         | 8000                  | N/A                 |   |
| match          | match        | 8000                  | N/A                 |   |
| player         | player       | 8000                  | N/A                 |   |
| access         | access       | 8000                  | N/A                 |   |
| ticket         | ticket       | 8000                  | N/A                 |   |
| gateway        | N/A          | 8000                  | 8000                |   |
| webapp         | N/A          | 8080                  | 8080                |   | 
