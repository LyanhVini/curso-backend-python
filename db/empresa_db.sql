create database empresa_db;
use empresa_db;

create table departamento (
	codigo int PRIMARY KEY auto_increment,
    descricao varchar(100) not null
);

create table funcionario (
	codigo int primary key auto_increment,
    nome varchar(100) not null,
    endereco varchar(200) not null,
    telefone varchar(20),
    cod_departamento int,
    constraint fk_funcionario_departamento
		foreign key (cod_departamento)
        references departamento(codigo)
        ON DELETE SET NULL
        ON UPDATE CASCADE
);

-- inserir dados em departamento
insert into departamento (descricao) values ('TI'), ('RH'), ('Financeiro'), ('vendas');

-- Inserir dados em funcionários
INSERT INTO Funcionario (nome, endereco, telefone, cod_departamento) VALUES 
('João Silva', 'Rua A, 123', '(11) 9999-1111', 1),
('Maria Santos', 'Av. B, 456', '(11) 9999-2222', 2),
('Pedro Oliveira', 'Rua C, 789', '(11) 9999-3333', 1),
('Ana Costa', 'Av. D, 101', '(11) 9999-4444', 3),
('Carlos Lima', 'Rua E, 202', '(11) 9999-5555', 4);