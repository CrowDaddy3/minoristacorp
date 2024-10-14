# Proyecto Minoristacorp

## Descripción

El proyecto consiste en una aplicación que se encarga de aplicar un descuento especifico para los articulos de diferentes proveedores.

El proyecto esta desarrollado con Python con el framework FastAPI.

## How to run

1. Para ejecutar el proyecto, necesitarás tener instalado Python y pip.

El proyecto fue codificado sobre la version 3.12 de python, en caso de no contar con la version especifica, se puede utilizar este enlace para la instalacion de este mismo.

[Instala Python 3.12](https://ubuntuhandbook.org/index.php/2023/05/install-python-3-12-ubuntu/)

2. Asi mismo es necesario poder crear ambientes virtuales para instalar todas las dependencias necesarias del proyecto, para ello puedes seguir el siguiente enlace.

[Instala virtualenv](https://virtualenv.pypa.io/en/latest/installation.html)

3. Una vez instalado Python 3.12 y virtualenv, puedes crear un ambiente virtual para el proyecto con los siguientes comandos:

```bash
python3.12 -m venv env
source env/bin/activate
```

4. Teniendo el ambiente virtual creado y activo, puedes instalar todas las dependencias necesarias del proyecto con el siguiente comando:

```bash
pip install -r requirements/base.txt
```

5. Una vez instaladas todas las dependenciasv, puedes ejecutar el proyecto con el siguiente comando:

```bash
fastapi dev src/main.py
```

Esto creara un servidor en el cual puedes acceder a la aplicacion. De manera predeterminada, el servidor se ejecuta en el puerto 8000, por lo que puedes ingresar al siguiente enlace [localhost](http://127.0.0.1:8000/) en donde encontraras el inicio por default del proyecto o bien puedes ingresar a la [documentacion](http://127.0.0.1:8000/docs) para poder ejecutar y revisar cada una de las API's contenidas dentro del proyecto.

## Ejecución del proyecto con Doker

1. Es necesario correr los siguientes comandos para poder crear la imagen del proyecto (es necesario estar en la raiz del proyecto con alguna terminal):

```
bash
docker build -t fastapi-app .
```

2. Seguido del siguiente comando para correr el contenedor:
```
bash
docker run -p 8000:8000 fastapi-app
```

3. Al correr el contenedor podemos visitar el sitio [localhost](http://localhost:8000/) en donde podremos acceder a la pagina principal y default del proyecto o bien puedes ingresar a la [documentacion](http://localhost:8000/docs) para ejecutar y revisar cada una de las API's contenidas dentro del proyecto.

## Estrategia de desarrollo

Para este proyecto se utilizaron diferentes tecnologias de las cuales destacan FastAPI, con ellos se logro el cometido de crear una aplicación que calcula el precio con descuento de ciertos articulos, el descuento varia dependiendo del proveedor que este registrando el articulo, asi mismo dentro del proyecto se manejaron varios puntos de programacion orientada a objetos.

### Pasos para el desarrollo del proyecto

- **Definir la estructura del proyecto**: Se definio la estructura del proyecto.
- **Crear los modelos de Pydantic**: Se definieron  los modelos de Pydantic para la estructura de los datos.
- **Crear las clases para calcular los precios con descuento**: Se  definieron las clases para calcular los precios con descuento.
- **Crear la API descuentos**: Se creo la API para calcular los precios acorde al descuento que tiene cada proveedor.
- **Crear Tests**: Se crearon los tests necesarios para validar que las API´s funcionen de manera correcta en ciertos entornos y bajo ciertas condiciones.
- **Contenerización**: Se creo el Dockerfile a partir del proyecto temrinado para proceder a su contenerización.
- **Documentación**: Se completo el README.md y documentación dentro del proyecto
- **Despliegue con GPC**: Se hizo el correspondiente despliegue con GPC.
