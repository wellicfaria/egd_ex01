CREATE DATABASE loja;
USE loja;
CREATE TABLE clientes (
    Id INT PRIMARY KEY,
    Nome VARCHAR(50)
);
CREATE TABLE vendas (
    Data DATE,
    Produto VARCHAR(50),
    Quantidade INT,
    Preco FLOAT,
    IdCliente INT,
    FOREIGN KEY (IdCliente) REFERENCES clientes(Id)
);
