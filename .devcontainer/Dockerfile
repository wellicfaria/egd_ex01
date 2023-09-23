# Use uma imagem base do Python
FROM python:3.8-slim

# Instalar dependências do sistema
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Instalar PySpark e Airflow
RUN pip install pyspark==3.1.2 apache-airflow==2.1.2

# Porta padrão do Airflow WebServer
EXPOSE 8080
