# Visão Geral

Neste desafio, você assumirá a responsabilidade de desenvolver uma série de scripts PySpark armazenados na pasta pyspark_scripts. Cada script é destinado a um papel específico na criação e gerenciamento de um pipeline de dados, abrangendo desde a coleta até o enriquecimento dos dados. Os detalhes para cada script estão elaborados abaixo.


## Conceitos-Chave

- `Data Lake`: É um repositório centralizado que permite armazenar todos os seus dados, sejam eles estruturados ou não.
- `Delta Lake`: Uma camada de armazenamento que traz confiabilidade para Data Lakes.
- `UPSERT`: É uma operação de banco de dados atômica que insere registros em uma tabela se eles não existirem ou atualiza-os se já existirem.

## Scripts

1. `move_bronze.py`

### Objetivo

Desenvolver um script PySpark genérico que transfira dados do estágio inicial (stage) para a camada Bronze do Data Lake.

### Funcionalidades

Recebe parâmetros para especificar as fontes e destinos dos dados.
Adiciona três novas colunas:
- KEY_BRONZE: Uma chave gerada pela concatenação de todas as colunas usando MD5.
- DT_CREATE_BRONZE: Data de criação do registro na camada bronze.
- DT_UPDATE_BRONZE: Data de atualização do registro na camada bronze.

A escrita sera feita na pasta data no formato [DELTA](https://docs.delta.io/latest/delta-intro.html), usando a tecnica de [UPSERT](https://docs.delta.io/latest/delta-update.html#upsert-into-a-table-using-merge) conforme das redomendaçãos do arquivo [data\data.md](/data/data.md). Usando como math a KEY_BRONZE . 

2. `move_silver.py`

### Objetivo
Este script é um módulo PySpark genérico que transfere dados da camada bronze para a camada silver do Data Lake.

### Funcionalidades
Recebe parâmetros para especificar as fontes e destinos dos dados.
Adiciona três novas colunas:
- KEY_SILVER: Uma chave gerada pela concatenação de chaves de negócios ou identificador único usando MD5.
- DT_CREATE_SILVER: Data de criação do registro na camada silver.
- DT_UPDATE_SILVER: Data de atualização do registro na camada silver.

A escrita sera feita na pasta data no formato [DELTA](https://docs.delta.io/latest/delta-intro.html), usando a tecnica de [UPSERT](https://docs.delta.io/latest/delta-update.html#upsert-into-a-table-using-merge) conforme das redomendaçãos do arquivo [data\data.md](/data/data.md). Usando como math a KEY_SILVER . 

3. `move_gold_clientes.py`

### Objetivo
Este script é um módulo PySpark que irá criar o `PRODUTO DE DADOS` cliente. Nessa tabela que irá ser utilizada para o time de negócios.  
Os dados são lidos da camanda silver e assim é construindo os dados gold. 

Eles vão precisar dos seguintes dados/colunas: 
- ID_CLIENTE: Identificador do cliente. 
- NOME_CLIENTE: Nome do cliente
- QT_TOTAL_VENDAS: Coluna contendo o somatorio de vendas do cliente
- PRODUTO_FAVORITO: Coluna contendo o nome do produto favorito do cliente, ou seja, o que ele mais comprou. 
- CLIENTE_PRIME: Uma flag (true ou false) ou (0 ou 1) para cliente que realizaram mais de 20 contas. 

A escrita sera feita na pasta data no formato [DELTA](https://docs.delta.io/latest/delta-intro.html), usando a tecnica de [UPSERT](https://docs.delta.io/latest/delta-update.html#upsert-into-a-table-using-merge) conforme das redomendaçãos do arquivo [data\data.md](/data/data.md). Usando como math a KEY_GOLD . 

