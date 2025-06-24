# Docker

Este directorio contiene todo lo necesario para realizar inferencia del modelo usando Docker.

---

## 1. Situarse en la carpeta `docker`

Desde la raíz del repositorio, navega hasta la carpeta `docker`:

```bash
D:/Downloads> cd mlops-docker-example/docker
D:/Downloads/mlops-docker-example/docker>
```

---

## 2. Construir la imagen

Ejecuta el siguiente comando para construir la imagen Docker:

```bash
D:/Downloads/mlops-docker-example/docker> docker build -t inference-python-test .
```

* `-t inference-python-test` etiqueta la imagen con ese nombre.
* El contexto `.` incluye todos los archivos en `docker/` (Dockerfile, `inferencia.py`, `pipeline.pkl`, `transformadores/`).

---

## 3. Ejecutar el contenedor

Para montar la carpeta local `files/` dentro del contenedor en `/files`, usa:

```bash
D:/Downloads/mlops-docker-example/docker> docker run --rm \
  -v "D:/Downloads/mlops-docker-example/files:/files" \
  inference-python-test
```

* `--rm` elimina el contenedor al terminar la ejecución.
* `-v "<host_path>/files:/files"` monta la carpeta de entrada/salida.
* El script leerá `/files/input.csv` y generará `/files/output.csv`.

---

## 4. Verificar resultados

Al finalizar, encontrarás `output.csv` dentro de la carpeta local `files/`.

---

> **Nota:**
>
> * Asegurarase de que en `files/input.csv` estén todas las columnas que el pipeline requiere.
> * Si cambias el nombre de la imagen (etiqueta `-t`), usa ese mismo nombre en el comando `docker run`.
