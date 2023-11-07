# Usa una imagen base de Python 3.9
FROM python:3.9

# Establece el directorio de trabajo en /app
WORKDIR /app

# Copia el archivo requirements.txt al contenedor
COPY requirements.txt requirements.txt

# Instala las dependencias del proyecto
RUN pip install -r requirements.txt

# Copia todo el contenido de tu proyecto Django al contenedor
COPY . .

# Expone el puerto en el que se ejecuta tu aplicación Django
EXPOSE 8000

# Inicia tu aplicación Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
