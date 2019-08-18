# Wikidata Game

Requerimientos:

* Python 3
* pip

Instalación de dependencias:

``
pip install -r requirements.txt
``

Para correr uno de los servicios:

```
cd src/<directorio-servicio>/
pip install -r requirements.txt
nameko run --config config.yaml access
```
Para construir los contenedores:
```
docker-compose build
```
Una vez construídos, para correrlos:
```
docker-compose up -d
```
Para ver los Logs de cada contenedor:
```
docker-compose logs <nombre_servicio>
```

