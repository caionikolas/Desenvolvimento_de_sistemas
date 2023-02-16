var capitalizeTitle = function(title) {
    let words = title.split(' ')
    for(let i = 0; i < words.length; i++){
        if (words[i].length < 3){
            words[i] = words[i].toLowerCase()
        } else{
            words[i] = words[i].toLowerCase()
            let word = words[i]
            word = word.split('')
            word[0] = word[0].toUpperCase()
            word = word.join('')
            words[i] = word
        }
    }
    words = words.join(' ')
    return words
};

console.log(capitalizeTitle("First leTTeR of EACH Word"))



/*
drop table cliente;

CREATE TABLE cliente(
	cpf numeric(11,0) primary key,
	rg numeric(14,0) not null,
	nome varchar (30) not null,
	data_nascimento date not null,
	ativo boolean default true
);

CREATE TABLE produto (
	codigo_produto integer primary key,
	nome_produto varchar(30) not null,
	valor numeric(9,2) check (valor > 10)
);

insert into cliente values (111111, 12345, 'Antonio', '2000/10/25', false);
insert into cliente values (111222, 12345, 'Maria', '2001/11/25', default);
insert into cliente values (222222, 15423, 'Joao', '1999/06/23');

SELECT * FROM public.produto

INSERT INTO produto VALUES (1,'vassoura', 12.60);
INSERT INTO produto VALUES (2,'sabão', 20.30);
INSERT INTO produto VALUES (3,'tapete', 10.01);

*/