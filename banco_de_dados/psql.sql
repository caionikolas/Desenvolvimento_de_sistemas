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

\dt - listar tabelas

\d - ver a estrutura da tabela





*/

