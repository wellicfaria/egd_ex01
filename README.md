# egd_ex01
Exerciocio desenvolver um pipeline de dados para ingestão, transformação e análise de dados. 


# Organização do Projeto

```
MeuProjeto/
├── .devcontainer/
│   ├── Dockerfile
│   ├── docker-compose.yml
│   └── devcontainer.json
├── data/
│   └── vendas.csv
├── sql/
│   └── vendas.sql
├── dags/
│   └── meu_dag.py
├── pyspark_scripts/
│   └── transformacao_de_dados.py
├── requirements.txt
└── README.md
```

## Descrição:

.devcontainer/: Contém todos os arquivos necessários para o DevContainer, como Dockerfile, docker-compose.yml e devcontainer.json.

data/: Armazena os dados brutos, como o arquivo vendas.csv.

sql/: Contém scripts SQL, como vendas.sql para criação de tabelas e inserção de dados.

dags/: Contém os arquivos DAG do Airflow, como meu_dag.py.

pyspark_scripts/: Contém os scripts PySpark para transformações de dados, como transformacao_de_dados.py.

requirements.txt: Lista todas as bibliotecas Python necessárias.

README.md: Documentação do projeto, explicando como configurar e executar o projeto.