# Case egd_ex01 de Engenharia de Dados para o Canal e Blog DadosBr

## Introdução
Olá, inscritos e seguidores do [canal YouTube](https://www.youtube.com/@DADOSBRASIL) e [blog](https://www.brdados.com.br/) DadosBR! 

Atendendo a inúmeras solicitações, estamos lançando um case prático de Engenharia de Dados que aborda a criação e gerenciamento de um pipeline de dados usando PySpark e Delta Lake. 

Este projeto é uma excelente oportunidade para aprofundar seus conhecimentos e habilidades em áreas fundamentais da engenharia de dados.

## O Que Você Vai Aprender
Neste case, você terá a chance de:
- Entender a estrutura de um Data Lake e suas camadas (Bronze, Silver, Gold).
- Aprender a utilizar Delta Lake para armazenamento de dados confiável.
- Implementar técnicas de UPSERT para manipulação de dados.
- Utilizar PySpark para mover e transformar grandes volumes de dados.
- Orquestração de dados com Airflow

## Detalhes do Case
O projeto consiste em desenvolver quatro scripts PySpark, cada um com objetivos e funcionalidades específicas no pipeline de processamento de dados. Você será guiado em como mover dados entre diferentes camadas do Data Lake, desde a camada inicial até camadas mais refinadas e prontas para análise.

Além dos scripts, forneceremos uma documentação detalhada que explica cada etapa, tornando este case não apenas um exercício prático, mas também uma experiência de aprendizado completa.

## Para Quem É Este Case?
Este case é ideal para quem já possui algum conhecimento em Python e SQL e deseja entrar no mundo da Engenharia de Dados. Também é útil para profissionais da área que desejam aprimorar suas habilidades em ferramentas e técnicas modernas.

## Organização do Projeto
A organização de pastas é crucial para manter o projeto escalável e fácil de entender. Aqui está uma sugestão de estrutura de diretórios para o seu projeto:

```
MeuProjeto/
├── .devcontainer/
│   ├── Dockerfile
│   ├── docker-compose.yml
│   └── devcontainer.json
├── data/
│   └── stage
│   └── bronze
│   └── silver
│   └── gold
├── sql/
│   └── vendas.sql
│   └── clientes.sql
├── dags/
│   └── dag_main.py
├── pyspark_scripts/
│   └── transformacao_de_dados.py
├── requirements.txt
└── README.md
```

### Descrição:
- `.devcontainer/`: Contém todos os arquivos necessários para o DevContainer, como Dockerfile, docker-compose.yml e devcontainer.json. Aqui está a configuração do ambiente para o seu desenvolvimento. 
- `data/`: Armazena os dados do seu projeto. Leia mais clicando [aqui.](/data/data.md)
- `sql/`: Contém scripts SQL, como vendas.sql e clientes.sql para criação de tabelas e inserção de dados. Caso queira mais dados, ou alterar algo nos dados, você pode customizar o `generate_data_sql.py`. 
- `dags/`: Contém os arquivos DAG do Airflow, como dag_main.py.
- `pyspark_scripts/`: Contém os scripts PySpark para transformações de dados, [click aqui](/pyspark_scripts/pyspark_scripts.md) para saber o que voce tem que desenvolver.
- `requirements.txt`: Lista todas as bibliotecas Python necessárias.
- `README.md`: Documentação do projeto, explicando como configurar e executar o projeto.

## Diretrizes para resolver o Case
### 1 . Conectando no banco de dados e inserindo os registros. 
Para executar comandos SQL em um contêiner Docker que está executando o MySQL, você pode usar o seguinte procedimento:
1. Acesse a APPWEB: Primeiro, você precisa acessar o Banco de Dados. Para facilitar o processo, foi disponibilizada uma interface gráfica para você executar os comandos SQL pelo seu navegador. Acesse o site abaixo:

```shell
http://localhost:8080/?server=db
```
2. Acesse o MySQL: Assim que abrir a aplicação web, faça o login. O usuário é `root` e a senha do banco de dados é `mysql123`. Clique em `entrar`.
3. Execute Comandos SQL: Após o login, no canto superior esquerdo tem um link que você deve clicar, clique em `Comando SQL`. Agora você pode criar o banco de dados e colocar os dados. Em baixo você vai encontrar o diagrama desse banco. Copie o script, cole e clique em `executar`. Execute nessa ordem no banco de dados os seguintes scripts:

- 1º [sql/ddls.sql](/sql/ddls.sql)
- 2º [sql/clientes.sql](/sql/clientes.sql)
- 3º [sql/vendas.sql](/sql/vendas.sql)

Clique em `Comando SQL` e repita esse processo até todos os scripts forem executados. Agora você tem uma Base de dados chamada `loja` com 2 tabelas: `clientes` e `vendas`.

```mermaid
---
title: Diagrama do Banco de Dados
---
erDiagram
    CLIENTES ||--o{ VENDAS : tem
    CLIENTES {
        int Id
        string Nome
    }
    VENDAS {
        date Data
        string Produto
        int Quantidade
        float Preco
        int IdCliente
    }
```
### 2 . Iniciando o Airflow Localmente

O Airflow já esta instalado no nosso ambinte Docker. Mas você vai precisar iniciar o mesmo. 

- 1. Abra um terminal(`ctrl + shift+ '`) e rode o comando: `airflow webserver -p 8055`. 
- 2. Abra outro terminal(`ctrl + shift+ '`) e rode o comando: `airflow scheduler`. 

Agora no seu navegador você já consegue acessar a interface web do Airflow, pelo link:

```
http://localhost:8055/
```

Onde a usuário e senha é `admin`.

Pronto, agora você tem seu Arflow funcionando. Voce pode desenvolver agora sua DAG. [Click aqui](/dags/dags.md) para saber mais sobre processo de desenvolvimento da sua DAG. 


## Autores do Case
- `Wellington Faria` - [Linkedin](https://www.linkedin.com/in/wellicfaria/) - [GitHub](https://github.com/wellicfaria)