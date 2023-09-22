-- Criar a tabela de vendas
CREATE TABLE IF NOT EXISTS vendas (
    ID_Venda INT PRIMARY KEY AUTO_INCREMENT,
    Data DATE,
    Produto VARCHAR(255),
    Quantidade INT,
    Preco FLOAT
);

-- Inserir registros de exemplo
INSERT INTO vendas (Data, Produto, Quantidade, Preco) VALUES ('2023-01-01', 'Produto_A', 10, 20.5);
INSERT INTO vendas (Data, Produto, Quantidade, Preco) VALUES ('2023-01-02', 'Produto_B', 5, 15.0);
INSERT INTO vendas (Data, Produto, Quantidade, Preco) VALUES ('2023-01-03', 'Produto_C', 3, 40.0);
INSERT INTO vendas (Data, Produto, Quantidade, Preco) VALUES ('2023-01-04', 'Produto_A', 8, 20.5);
INSERT INTO vendas (Data, Produto, Quantidade, Preco) VALUES ('2023-01-05', 'Produto_B', 6, 15.0);
