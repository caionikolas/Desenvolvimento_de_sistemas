/* Comandos PSQL */
psql -h localhost -p 5432 -U postgres -W
/* logo apos é necessario colocar a senha do banco! */


/* comandos dentro do psql */
/*
\l - Lista todas as tabelas do banco

\c - conecta ao banco
    \c nomedobanco

\criar tabela
    create table cliente (cpf numeric(11,0),
    nome varchar(30),
    rg numeric (14,0),
    dt_nasc date,
    ativo boolean
    );
    
create table vendas.produtos (id integer primary key, decricao  varchar(30));

\dt - listar tabelas
\dt nomedoesquema.*

\d - ver a estrutura da tabela

SHOW serach_path;  -  Mostra todos os esquemas que o usuario esteja cadastrado
SET search_path TO vendas,public;   -    escolhar quais esquemas vao para o caminho de busca direto  

\df  -   mostra funções

\du  -   lista de roles

\dv  -   mostra as views

\o   -   destina consulta para um arquivo

\i  -  executar um arquivo com varios comandos dentros dele

*/

--cliando e inserindo dados na tabela clientes e pedidos:
insert into clientes (id, nome, idade, cidade) values (1, 'João da Silva', 32, 'São Paulo'), (2, 'Maria Oliveira', 25, 'Rio de Janeiro'), (3 , 'Carlos Santos', 47, 'Belo Horizonte');

create table pedidos (id integer primary key, data date, valor numeric(10,2), cliente_id integer, foreign key(cliente_id) references clientes(id));

-- selecionar todos os dados da tabela clientes
select * from clientes;

-- Seleciona o nome e a idade dos clientes
select nome, idade  from clientes;

-- selecionar o nome e a cidade dos clientes que moram em São Paulo
SELECT nome, cidade from clientes where cidade = 'São Paulo';

select valor,data from pedidos where valor > 100;
