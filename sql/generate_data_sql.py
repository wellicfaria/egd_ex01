import random
from datetime import datetime, timedelta


# Este script Python é usado para gerar registros aleatórios de vendas e clientes, que são então salvos em arquivos SQL separados (vendas.sql e clientes.sql).
## Constantes e Variáveis
### NUMERO_CLIENTES: A quantidade de clientes a serem gerados.
### PRODUTOS = : Lista dos produtos disponíveis junto com os seus preços.

NUMERO_CLIENTES= 20

# Lista de produtos
PRODUTOS = [
    "Produto_A-10.50", 
    "Produto_B-6.00",
    "Produto_D-7.55", 
    "Produto_C-3.50"]

# Arquivo SQL de saída
with open("vendas.sql", "w") as f:
    for i in range(1000):
        data = datetime(2023, 1, 1) + timedelta(days=i % 365)
        data_str = data.strftime("%Y-%m-%d")
        aux = random.choice(PRODUTOS)
        produto = aux.split("-")[0]
        quantidade = random.randint(1, 10)
        preco = float(aux.split("-")[1])
        cliente = random.randint(1, NUMERO_CLIENTES)
        
        f.write(f"INSERT INTO vendas (Data, Produto, Quantidade, Preco, IdCliente) VALUES ('{data_str}', '{produto}', {quantidade}, {preco}, {cliente});\n")
f.close()

# Lista de nomes de clientes
clientes = [f"Cliente_{i+1}" for i in range(NUMERO_CLIENTES)]

# Arquivo SQL de saída para clientes
with open("clientes.sql", "w") as f:
    for i, cliente in enumerate(clientes):
        f.write(f"INSERT INTO clientes (ID, Nome) VALUES ({i + 1}, '{cliente}');\n")
f.close()


