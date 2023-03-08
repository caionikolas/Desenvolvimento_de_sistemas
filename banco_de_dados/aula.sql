/*  Criar tabela (venda)                                    */

CREATE TABLE venda (
	codigo_venda integer primary key,
	data_venda date NOT NULL,
	data_total_venda numeric(9,2) NOT NULL,
	desconto numeric(9,2) NOT NULL,
	cpf numeric(11,0),
	CONSTRAINT cliente_fk foreign key (cpf) references cliente(cpf)
);

/* inserido valores na tabela venda                         */
INSERT INTO venda VALUES (1, '01/02/2023', 130.00, 0, 1111112);
INSERT INTO venda VALUES (2, '01/02/2023', 130.00, 0, 1111111);
INSERT INTO venda VALUES (3, '01/02/2023', 400.00, 10, 1111111);
INSERT INTO venda VALUES (4, '01/02/2023', 86.00, 0, 1111112);
INSERT INTO venda VALUES (5, '01/02/2023', 99.30, 0, 2222222);
INSERT INTO venda VALUES (6, '01/02/2023', 213.25, 15, 2222222);
INSERT INTO venda VALUES (7, '01/02/2023', 560.80, 30, 1111112);
INSERT INTO venda VALUES (8, '01/02/2023', 12.50, 0, 1111112);
INSERT INTO venda VALUES (9, '01/02/2023', 76.40, 0, 2222222);
INSERT INTO venda VALUES (10, '01/02/2023', 146.15, 0, 1111111);