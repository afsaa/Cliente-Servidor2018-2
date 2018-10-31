# Ejercicio hola mundo SOAP

Ejercicio inicial con SOAP.

## Prerequisitos

Es necesario tener instalado python2 o python3.

Tener instalado pip previamente. En caso de que no se encuentre instalado usar el comando en la terminal (linux) ```sudo apt install python-pip``` para la versión 2 de Python. Para la versión 3 usar ```sudo apt install python3-pip```

## Instalación

Para instalar spyne es necesario usar ```sudo easy_install spyne```

## Ejecución

Para ejecutar el código hay que usar ```python helloworld_service.py``` en una terminal.

Ejecutar en otra terminal
```curl 'http://localhost:8000/say_hello?name=World&times=5'\| python -m json.tool``` para recibir las respuestas del servidor.
