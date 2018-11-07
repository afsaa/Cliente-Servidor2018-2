# Ejercicio hola mundo RESTful

Ejercicio inicial con RESTful.

## Prerequisitos

Es necesario tener instalado python2 o python3.

## Instalación

Es necesario instalar los modulos Spyne y curl.

Para instalar Spyne es necesario usar ```sudo easy_install spyne```

Para instalar curl hay que usar el comando ```sudo apt-get install curl```

## Ejecución

Para ejecutar el código hay que usar ```python rest_server.py``` en una terminal.

Ejecutar en otra terminal el comando ```curl -s http://localhost:8000/ -d \
             '{"say_hello": {"name": "World", "times": 5}}' \
                                        | python -m json.tool```.
