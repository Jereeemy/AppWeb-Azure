
FROM python:3.9-slim

# Installer les dépendances nécessaires pour le pilote ODBC 17 et pyodbc
RUN apt-get update && \
    apt-get install -y \
    curl \
    gnupg2 \
    unixodbc-dev \
    && curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - && \
    curl https://packages.microsoft.com/config/debian/10/prod.list > /etc/apt/sources.list.d/mssql-release.list && \
    apt-get update && \
    ACCEPT_EULA=Y apt-get install -y msodbcsql17


WORKDIR /app


COPY . /app

# Installer FastAPI, Uvicorn et pyodbc
RUN pip install fastapi uvicorn pyodbc

# Rendre le port 8080 accessible depuis l'extérieur du conteneur
EXPOSE 8080

# Lancer l'application avec Uvicorn au démarrage du conteneur
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
