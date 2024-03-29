/* ===== Boas maneiras para criação de bancos =====		
** Nomes minusculos, sem espaço e caracteres especiais
** Escrita de linguagem SQL sempre em letra maiuscula   			*/

/* Apagar tabela (cliente) 																		*/
drop table cliente;

/* Criar Tabela (cliente)																			*/
CREATE TABLE cliente(
	cpf numeric(11,0) primary key,
	rg numeric(14,0) not null,
	nome varchar (30) not null,
	data_nascimento date not null,
	ativo boolean default true
);

/* Criar Tabela (Produto)	 																		*/
CREATE TABLE produto (
	codigo_produto integer primary key,
	nome_produto varchar(30) not null,
	valor numeric(9,2) check (valor > 10)
);

/* Inserindo dados na tabela (cliente)											 	*/
insert into cliente values (111111, 12345, 'Antonio', '2000/10/25', false);
insert into cliente values (111222, 12345, 'Maria', '2001/11/25', default);
insert into cliente values (222222, 15423, 'Joao', '1999/06/23');

/* Visualizar todas as tabelas															 	*/
SELECT * FROM public.produto

/* Inserindo dados na tabela (produtos)	 											*/
INSERT INTO produto VALUES (1,'vassoura', 12.60);
INSERT INTO produto VALUES (2,'sabão', 20.30);
INSERT INTO produto VALUES (3,'tapete', 10.01);

/* Outra maneira de inserir valores  (escolhendo a ordem que vai inserir no banco)           */
INSERT INTO cliente (nome, cpf, rg, data_nascimento, ativo) VALUES (
	'roberta', 12345678911, 12345678901235, '10/05/2023', True  
);

/* atualizar tabela  (sempre optar por usar o "WHERE" porem é opcional)             */
UPDATE cliente SET ativo = true;

UPDATE cliente SET data_nascimento = '2000/10/02', nome = 'zezinho' , ativo = false
WHERE cpf = 12345678910;

/* Deletar tabela 											*/
DELETE FROM cliente WHERE cpf = 111111;

SELECT * FROM cliente



