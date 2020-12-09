CREATE DATABASE locadora;
use locadora;

-- Criando tabela genero
CREATE TABLE genero (
  id INT UNIQUE,
  nome VARCHAR(100) NOT NULL,
  dtcriacao DATETIME NULL,
  ativo BIT(1) NOT NULL,
  PRIMARY KEY (id)
  );

-- Craindo Tabela filme 
  CREATE TABLE filme (
  id INT UNIQUE,
  nome VARCHAR(200) NOT NULL,
  dtcriacao DATETIME NOT NULL,
  ativo BIT(1) NOT NULL,
  generoid INT NOT NULL,
  PRIMARY KEY (id),
  FOREIGN KEY (generoid) REFERENCES genero (id)
);

-- Criando a tabela usuario
CREATE TABLE usuario (
  id INT UNIQUE,
  nome VARCHAR(200) NOT NULL,
  email VARCHAR(100) NULL,
  cpf VARCHAR(14) NULL,
  ativo BIT(1) NOT NULL,
  PRIMARY KEY (id)
  );

-- Criando a tabela filmelocacao
CREATE TABLE filmelocacao (
  id INT UNIQUE,
  filmeid INT NOT NULL,
  PRIMARY KEY (id),
  FOREIGN KEY (filmeid) REFERENCES filme (id)
);

-- Criando tabela locacao
CREATE TABLE locacao (
  id INT UNIQUE,
  filmelocacaoid INT NOT NULL,
  usuarioid INT NOT NULL,
  dtLocacao DATETIME NOT NULL,
  PRIMARY KEY (id),
  FOREIGN KEY (filmelocacaoid) REFERENCES filmelocacao (id),
  FOREIGN KEY (usuarioid) REFERENCES usuario (id)
);

-- Inserindo 8 Gêneros em genero
INSERT INTO genero VALUES (1,'Romance', CURRENT_TIMESTAMP,1), (2,'Ficcao', CURRENT_TIMESTAMP,1), (3,'Terror', CURRENT_TIMESTAMP, 0), (4,'Acao',CURRENT_TIMESTAMP, 1), (5, 'Drama', CURRENT_TIMESTAMP, 0), (6,'Comedia', CURRENT_TIMESTAMP,1), (7,'Romances de Fantasia',CURRENT_TIMESTAMP, 1), (8,'Animacao',CURRENT_TIMESTAMP, 1);

-- Iserindo 20 Filmes em filme
INSERT INTO filme VALUES (1, 'Simplismente Amor', CURRENT_TIMESTAMP, 1, 1), (2, 'O Joga da Imitação', CURRENT_TIMESTAMP, 1, 5), (3, 'Interstellar', CURRENT_TIMESTAMP, 1, 2), (4, 'Guerra nas Estrelas', CURRENT_TIMESTAMP, 1, 2),  (5, 'Avatar', CURRENT_TIMESTAMP, 1, 2), (6, 'Minority Report - A nova Lei', CURRENT_TIMESTAMP, 1, 2), (7, 'As Branquelas', CURRENT_TIMESTAMP, 1, 6), (8, 'Tamy - Fora de controle', CURRENT_TIMESTAMP, 0, 6), (9, 'Os Vingadores', CURRENT_TIMESTAMP, 0, 2), (10, 'Harry potter e as relíquias da morte', CURRENT_TIMESTAMP, 1, 7), (11, 'Harry potter e as relíquias da morte', CURRENT_TIMESTAMP, 1, 2), (12, 'À Procura da Felicidade', CURRENT_TIMESTAMP, 1, 5), (13, 'À Procura da Felicidade', CURRENT_TIMESTAMP, 1, 5), (14, 'Sete anso no Tibet', CURRENT_TIMESTAMP, 1, 5), (15, 'A Paixão de Cristo', CURRENT_TIMESTAMP, 1, 5), (16, 'Rock Balboa', CURRENT_TIMESTAMP, 1, 5),(17, 'Brilho Eterno de uma Mente sem Lembranças', CURRENT_TIMESTAMP, 1, 1),(18, '2012', CURRENT_TIMESTAMP, 1, 2),(19, 'Thor: Ragnarok', CURRENT_TIMESTAMP, 1, 4), (20, 'Meu Malvado Favorito ', CURRENT_TIMESTAMP, 1, 8); 

-- Populnado usuarios
INSERT INTO usuario (id, nome, email, ativo) VALUES (1, 'Ana Soares', 'ana@email.com', 1), (2, 'Maria Francisca Madruga', 'Xiquinha@email.com', 0), (3, 'Bobebbi da Bilva', 'nhono@bbb.com', 1), (4, 'Dona Florinda', 'xicaradecafe@garanhao.com', 0), (5, 'Professor Girafales', 'Humildepresente@agoravai.com', 1);

-- Inserindo dados em filmelocacao
INSERT INTO filmelocacao VALUES (1,1), (2,2),(3,3), (4,4), (5,5), (6,6), (7,7), (8,8), (9,9), (10,10), (11,11), (12,12), (13,13), (14,14), (15,15), (16,16), (17,17), (18,18), (19,19), (20,20);

-- Populando locacao
INSERT INTO locacao VALUES  (1, 1, 1, '2020-10-01 01:10:00'), (2, 2, 1, '2020-10-05 05:15:00'), (3, 3, 1, '2020-10-09 09:19:00'), (4, 4, 1, '2020-10-08 08:28:00'), (5, 5, 2, '2020-11-07 07:50:00'), (6, 6, 2, '2020-11-02 02:52:00'), (7, 7, 2, '2020-11-03 03:47:00'), (8, 8, 2, '2020-11-01 01:22:00'), (9, 9, 3, '2020-11-04 04:20:00'), (10, 10, 3, '2020-11-05 05:18:00'), (11, 11, 3, '2020-12-01 01:19:00'), (12, 12, 3, '2020-12-08 08:16:00'), (13, 13, 4, '2020-12-05 05:51:00'), (14, 14, 4, '2020-12-04 04:46:00'), (15, 15, 4, '2020-12-06 06:38:00'), (16, 16, 4, '2020-12-02 02:32:00'), (17, 17, 5, '2020-12-07 07:36:00'), (18, 18, 5, '2020-12-05 05:40:00'), (19, 19, 5, '2020-12-08 08:20:00'), (20, 20, 5, '2020-12-09 09:29:00');


/*
Faça um SQL que busque todas as locações deste mês com as seguintes colunas:
filme.nome, genero.nome, locacao.dtlocacao, usuario.nome, usuario.email

Pegando as principais tabelas da base, utilizando o join entre as mesmas.
Utilizando as chaves estrangeiras, temos as seguintes consultas abaixo.

*/

select filme.nome, genero.nome, locacao.dtlocacao, usuario.nome, usuario.email from filme
inner join genero
on genero.id = filme.generoid
inner join filmelocacao
on filmelocacao.filmeid = filme.id
inner join locacao
on locacao.filmelocacaoid = filmelocacao.id
inner join usuario
on usuario.id = locacao.usuarioid
where month(locacao.dtlocacao) = '12';

/* ou */

select filme.nome, genero.nome, locacao.dtlocacao, usuario.nome, usuario.email
from filme
inner join genero
on genero.id = filme.generoid
inner join filmelocacao
on filmelocacao.filmeid = filme.id
inner join locacao
on locacao.filmelocacaoid = filmelocacao.id
inner join usuario
on usuario.id = locacao.usuarioid
where locacao.dtlocacao between '2020-12-01' and '2020-12-31';

/*

Faça um SQL que apresente todos os usuário inativos que já tiveram alguma locação com as seguintes colunas:
usuario.nome, usuario.cpf

*/

select distinct usuario.nome, usuario.cpf
from filme
inner join filmelocacao
on filmelocacao.filmeid = filme.id
inner join locacao
on locacao.filmelocacaoid = filmelocacao.id
inner join usuario
on usuario.id = locacao.usuarioid
where usuario.ativo = 0;

/*

Faça um SQL que apresente a filmes alugados por usuario que contem a letra "A" em seu email com as seguintes colunas:
filme.id, filme.nome

Usando o comando join, para pegar as tabelas envolvidas para a consulta.
O comando LIKE, é para pegar a letra ou palavras informadas dentro do que foi pedido.
Colocando o "%", a consulta busca na coluna a informação solicitada, exemplo
like '%A%': procura no campo onde a plavra possua a letra "A";
like 'A%': procura no campo onde a palavra comece pela letra "A";
like '%A': procura no campo onde a palavra termine pela letra "A"

*/

select filme.id, filme.nome, usuario.email, usuario.nome from filme
inner join locacao
on locacao.filmelocacaoid = filme.id
inner join usuario
on usuario.id = locacao.usuarioid
where usuario.email like '%A%';

/*

Faça um SQL que apresente os filmes mais alugados:
filme.nome, quantidade de alugueis

*/

select filme.nome, count(1) 'quantidade de alugueis'
from filme
inner join filmelocacao
on filmelocacao.filmeid = filme.id
inner join locacao
on locacao.filmelocacaoid = filmelocacao.id
inner join usuario
on usuario.id = locacao.usuarioid
group by filme.nome
order by count(1) desc