CREATE DATABASE IF NOT EXISTS ecommerce_pro;
USE ecommerce_pro;

-- Tabela de Pedidos (O 'Pai')
CREATE TABLE pedidos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    cliente_nome VARCHAR(100),
    valor_bruto DECIMAL(10, 2) NOT NULL,
    status ENUM('PENDENTE', 'PAGO', 'CANCELADO') DEFAULT 'PENDENTE'
);

-- Tabela de Pagamentos (O 'Filho')
CREATE TABLE pagamentos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    pedido_id INT,
    metodo VARCHAR(20),
    valor_final DECIMAL(10, 2),
    data_pagamento DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (pedido_id) REFERENCES pedidos(id)
);

-- Massa de Dados (Pedidos Pendentes)
INSERT INTO pedidos (cliente_nome, valor_bruto) VALUES 
('João Silva', 1000.00),
('Maria Souza', 250.50),
('Carlos Tech', 5000.00);