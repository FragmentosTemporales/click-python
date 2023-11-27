# Contenedor Docker Python


## 1. Instalación

Para descargar la aplicación del repo, se debe escribir el siguiente comando:

```
$ git clone https://github.com/FragmentosTemporales/click-python
```


### Instalación de Docker Compose

Para instalar la aplicación debes ejecutar el siguiente código:

```
$ docker compose build
```


### Variables de entorno

Al interior de la carpeta /Sripts debes crear un documento env.env el cual debe contener las siguiente variables, puedes guiarte con el documento example.env :

```
null
```


## 2. Ejecución

Para ejecutar la aplicación debes ingresar el siguiente comando:

```
$ docker compose run --rm scripts sh -c "python manage.py users"
```

Reemplaza *"text"* por texto
```
$ docker compose run --rm scripts sh -c "python manage.py new --first_name <text> --last_name <text>"
```

Reemplaza *"int"* por un entero
```
$ docker compose run --rm scripts sh -c "python manage.py user <int>"
```

Reemplaza *"int"* por un entero
```
$ docker compose run --rm scripts sh -c "python manage.py delete <int>"
```

Reemplaza *"int"* por un entero y *"text"* por texto
```
$ docker compose run --rm scripts sh -c "python manage.py update <int> --first_name <text> --last_name <text>"
```

## 3.- ¿Qué estamos ejecutando?

Al ejecutar el manage.py estamos corriendo un gestor de archivos JSON a través de comandos por consola.


## 4.- Bibliografía

A continuación te dejo el link de la documentación de Click:

```
https://click.palletsprojects.com/en/8.1.x/
```