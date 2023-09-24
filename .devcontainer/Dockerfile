# Use uma imagem base do Python
FROM python:3.8-slim

# Instalar dependências do sistema
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Instale as dependências do Python
RUN pip install --upgrade pip
RUN pip install pyspark==3.1.2
RUN pip install apache-airflow==2.1.2

# Inicialize o banco de dados do Airflow
RUN airflow db init

# Crie um usuário para o Airflow
RUN airflow users create --username admin --password admin --firstname Admin --lastname User --role Admin --email admin@example.com


# Exponha a porta para o webserver do Airflow
EXPOSE 8081

# Comandos para iniciar o webserver e o scheduler do Airflow
CMD ["sh", "-c", "airflow webserver -p 8081 & airflow scheduler"]
